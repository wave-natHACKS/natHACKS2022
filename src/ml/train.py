"""Functions related to training."""
import tensorflow as tf
from tensorflow.keras import losses
from tensorflow.keras.models import Sequential


def train(
    model: Sequential,
    train_data: tf.data.Dataset,
    test_data: tf.data.Dataset,
    optim: str,
    loss: losses,
    save_path: str,
    epochs: int = 20
) -> None:
    """Train a given model with the given dataset."""

    # Compile and train a model
    model.compile(optimizer=optim, loss=loss, metrics=["accuracy"])
    model.fit(train_data, validation_data=test_data, epochs=epochs)

    # Save weights of trained model
    model.save_weights(save_path)
