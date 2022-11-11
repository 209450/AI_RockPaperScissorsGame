# import tensorflow.compat.v1 as tf
from pathlib import Path

import keras
import os
import cv2
import numpy as np


class RockPaperScissorsClassifier:
    img_size = (64, 64)
    input_size = (1, 64, 64, 3)
    labels = {0: 'paper', 1: 'rock', 2: 'scissors'}

    def __init__(self):
        self.model = None

    def load_model(self, path):
        path = Path(path)
        assert path.is_file(), "wrong image path"

        self.model = keras.models.load_model(path)

    def predict(self, img):
        output = int(np.argmax(self.model.predict(img)))
        return self.labels[output]

    @classmethod
    def load_image(cls, path):
        path = Path(path)
        assert path.is_file(), "wrong image path"

        img = cv2.imread(str(path))
        img = cls.reshape_image(img)
        return img

    @classmethod
    def reshape_image(cls, img):
        img = cv2.resize(img, cls.img_size)
        img = np.reshape(img, cls.input_size)
        return img
