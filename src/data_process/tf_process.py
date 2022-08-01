from typing import Union

import numpy as np
import pandas 
import tensorflow as tf


def train_test_data(
    df: pd.DataFrame,
    train_ratio: 0.8,
    target_cols: Union[list, np.ndarray]
):
    n_data = df.shape[0]

    test_idx = np.random.choice(n_data, size=int(n_data * train_ratio))
    train_f_names = df.iloc[test_idx, 0]
    train_labels = df.iloc[test_idx, 1:]
    test_f_names = df.iloc[~test_idx, 0]
    test_labels = df.iloc[~test_idx, 1:]

    