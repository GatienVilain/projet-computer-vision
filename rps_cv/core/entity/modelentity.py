from keras.models import load_model

from rps_cv.core.config.coreconfig import CoreConfig
from rps_cv.core.utils.shape import Shape
from keras.preprocessing import image

import cv2
import numpy as np

class ModelEntity:
    def __init__(self,
                 model_path = CoreConfig['model_path']):
        self.model_path = model_path
        self.model = load_model(self.model_path)


    def predict(self, frame):
        # Predicting images
        image = self._prepare_frame(frame)

        classes = self.model.predict(image, batch_size=10)

        # Class labels
        class_labels = [Shape.PAPER, Shape.ROCK, Shape.SCISSORS]

        # Finding the index of the predicted class
        predicted_index = np.argmax(classes[0])

        # Returning the predicted class from the Shape enumeration
        return class_labels[predicted_index]


    def _prepare_frame(self, frame):
        img = cv2.resize(frame, (150, 150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        return np.vstack([x])


"""    def predict(self, frame):
        import random

        shape = Shape.NONE
        while shape is Shape.NONE:
            shape = random.choice(list(Shape))
        print(shape)
        return shape"""

'''
    def predict(self, frame):

        frame = self._prepare_frame(frame)
        shape = self.model.predict(frame)

        if shape is 0:
            return Shape.ROCK
        elif shape is 1:
            return Shape.PAPER
        elif shape is 2:
            return Shape.SCISSORS
'''
