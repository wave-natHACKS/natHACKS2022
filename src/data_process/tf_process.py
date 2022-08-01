from typing import Tuple

import numpy as np
import pandas as pd
import tensorflow as tf


def train_test_data(
    df: pd.DataFrame,
    train_ratio: float = 0.8,
) -> Tuple[tf.data.Dataset, tf.data.Dataset]:
    """Split the given csv format data into train and validation set by ratio.
    """
    n_data = df.shape[0]

    # Compute indices for train data
    test_idx = np.random.choice(n_data, size=int(n_data * train_ratio))

    # Extract file names and labels for train/test
    train_f_names = df.iloc[test_idx, 0]
    train_labels = df.iloc[test_idx, 1:].to_numpy()
    test_f_names = df.iloc[~test_idx, 0]
    test_labels = df.iloc[~test_idx, 1:].to_numpy()
    
    # From file name, Get hte image data
    train_data, test_data = [], []
    for fn in train_f_names:
        img = np.load(fn)
        img = img.astype(np.float32)
        train_data.append(img)

    for fn in test_f_names:
        img = np.load(fn)
        img = img.astype(np.float32)
        test_data.append(img)
    
    train_data = np.array(train_data)
    test_data = np.array(test_data)

    # Expand dimensions for datasets
    train_d = np.expand_dims(train_data, axis=1)
    test_d = np.expand_dims(test_data, axis=1)
    train_labels = np.expand_dims(train_labels, axis=1)
    test_labels = np.expand_dims(test_labels, axis=1)
    
    # Convert numpy array data into tensorflow Datasets
    return tf.data.Dataset.from_tensor_slices((train_d, train_labels)), tf.data.Dataset.from_tensor_slices((test_d, test_labels))
