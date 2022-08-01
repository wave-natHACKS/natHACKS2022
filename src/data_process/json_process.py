"""Read and clean the data from processed json files."""
import io
import json
import os
from typing import Tuple

import cv2
import gensim
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def read_json(path: str) -> dict:
    """Read json file and convert to dictionary."""

    with open(path, 'r') as jf:
        dict_string = json.load(jf)
        data = json.loads(dict_string)
    
    return data


def wave_to_img(
    wave_dict: dict,
    save_path: str = None,
    dpi: int = 100
) -> np.ndarray:
    """Convert numerical wave data into 4-channeled image."""

    img = []
    for wave_type, wave_values in wave_dict.items():
        # Plot the wave normally with pyplot
        fig = plt.figure(dpi=dpi)
        ax = fig.add_subplot()
        
        ax.plot(range(len(wave_values)), wave_values, 'k')
        ax.axis("off")
        ax.set_axis_off()

        # Save plot as np array
        buffer = io.BytesIO()
        fig.savefig(buffer, format="raw", dpi=dpi)
        buffer.seek(0)
        img_arr = np.frombuffer(buffer.getvalue(), dtype=np.uint8)
        img_arr = np.reshape(img_arr, (int(fig.bbox.bounds[3]), int(fig.bbox.bounds[2]), -1))
        buffer.close()

        # Convert buffer image into grayscale and save
        channel = cv2.cvtColor(img_arr, cv2.COLOR_RGBA2GRAY)
        img.append(channel)

    # Convert list of channels into single np array image
    img = np.transpose(np.array(img, dtype=np.uint8), (1, 2, 0))
    
    # Save image if path for image is provided
    if save_path:
        np.save(save_path, img)
    
    return img


def str_to_onehot(str_arr: np.ndarray) -> Tuple[np.ndarray, list]:
    """Convert string categories into one-hot-encoded labels."""

    # Use sklearn onehot encoder to encode the labels
    enc = OneHotEncoder(handle_unknown="ignore")
    ohe = enc.fit_transform(str_arr).toarray()
    # Get categories in correct order
    categories = enc.categories_[0].tolist()
    return ohe, categories


def get_emotion(
    word: str,
    emotion_classes: np.ndarray,
    word2vec: Word2Vec
) -> str:
    """Relabel the word with similar emotion."""
    
    apply_w2v = lambda cls: word2vec.wv.similarity(word.lower(), cls)
    vec_apply = np.vectorize(apply_w2v)
    similarities = vec_apply(emotion_classes)
    return emotion_classes[np.argmax(similarities)]


def removeSymbol(word: str) -> str:
    """Remove special symbols other than alphabets."""
    special_charact = "!-$%&'()*+,./:;<=>?_[]^`{|}~@#"
    noSymbolWord = ""
    for w in word:
        if w not in special_charact:
            noSymbolWord += w
    return noSymbolWord


def make_df(
    data: dict,
    img_dir: str,
    idx: int,
    emotion_classes: np.ndarray
) -> pd.DataFrame:
    """Make dataframe for single file."""

    # Initialize word2vec with given sentence
    list_ = []  # no symbol
    for word in data.keys():
        word = removeSymbol(word.lower())
        list_.append(word)

    word2vec = Word2Vec([list_ + emotion_classes.tolist()],
                        min_count=1,
                        size=32)

    words = []
    cols = []
    fnames = []
    emo = []
    for i, word_dict in enumerate(data.values()):
        # Skip words without brainwave data
        if list(word_dict.values())[0] == []:
            continue
        noSymbolWord = list_[i]
        words.append(noSymbolWord)
        
        # Convert numerical wave data into image
        f_path = img_dir + f"{noSymbolWord}_{idx}.npy"
        print(f_path)
        _ = wave_to_img(word_dict, save_path=f_path, dpi=75)
        fnames.append(f_path)

        # Get the emotion label
        emotion = get_emotion(noSymbolWord, emotion_classes, word2vec)
        emo.append(emotion)
    
    fnames = np.asarray(fnames)
    fnames = np.expand_dims(fnames, axis=1)
    onehot_emotions, emo_list = str_to_onehot(np.expand_dims(emo, axis=1))
    cols = ["fname"] + emo_list   # columns name are ["path", "sadness", etc]
    contents = np.concatenate((fnames, onehot_emotions), axis=1)

    df = pd.DataFrame(contents, columns=cols)
    return df


def make_df_files(
    json_dir: str,
    img_dir: str,
    emotion_classes: np.ndarray
) -> pd.DataFrame:
    """Create dataframe with multiple json files."""
    assert os.path.isdir(json_dir), f"Invalid directory: {json_dir} given."

    if json_dir[-1] != '/':
        json_dir += '/'

    res_df = None
    for i, fn in enumerate(os.listdir(json_dir)):
        # Read json file and get data
        data = read_json(json_dir + fn)
        
        # Create dataframe from data
        df = make_df(data, img_dir, i, emotion_classes)

        # Concatenate dataframes
        if res_df is None:
            res_df = df
        else:
            res_df = pd.concat([res_df, df])
    
    res_df = res_df.fillna(0.)
    return res_df