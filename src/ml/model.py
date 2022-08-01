"""Module related to tensorflow model."""
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


def get_cnn_classifier(
    in_height: int,
    in_width: int,
    in_channels: int,
    out_shape: int
) -> Sequential:
    """Construct a simple CNN model for the project.
    Reference: https://www.tensorflow.org/tutorials/images/classification
    """

    model = Sequential([
        layers.Rescaling(1./255, input_shape=(in_height, in_width, in_channels)),
        layers.Conv2D(16, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding="same", activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(out_shape, activation="softmax")
    ])

    return model
