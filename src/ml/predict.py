import numpy as np
from tensorflow.keras.models import Sequential

from .model import get_cnn_classifier


def load_model(path: str) -> Sequential:
    """Load trained model with saved weights."""
    model = get_cnn_classifier(300, 450, 4, 6)
    model.load_weights(path)
    return model


def predict(img: np.ndarray, model: Sequential) -> int:
    """Predict the emotion with trained model."""
    assert img.shape == (300, 450, 4), "The shape of image is not suitable. It must be (300, 450, 4)"
    
    # Expand a dimension to suite the model
    img = np.expand_dims(img, axis=0)

    # Make prediction
    pred = model.predict(img)
    return np.argmax(pred)