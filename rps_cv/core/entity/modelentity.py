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

    def predict(self, file_path):
        # Predicting images
        img = image.load_img(file_path, target_size=(150, 150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)

        # Class labels
        class_labels = [Shape.ROCK, Shape.PAPER, Shape.SCISSORS]

        # Finding the index of the predicted class
        predicted_index = np.argmax(classes[0])

        # Returning the predicted class from the Shape enumeration
        return class_labels[predicted_index]

    def prepare_frame(self, frame):
        cv2.imwrite("photo_capturee.jpg", frame)
        return ("photo_capturee.jpg")


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


    def _prepare_frame(self, frame):
        pass # TODO: implement

'''

