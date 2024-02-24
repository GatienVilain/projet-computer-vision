import random

#from keras.models import load_model

from rps_cv.core.config.coreconfig import CoreConfig
from rps_cv.core.utils.shape import Shape

class ModelEntity:
    def __init__(self,
                 model_path = CoreConfig['model_path']):
        self.model_path = model_path
        #self.model = load_model(self.model_path)

    def predict(self, frame):
        # TODO: Implement prediction

        shape = Shape.NONE
        while shape is Shape.NONE:
            shape = random.choice(list(Shape))
        return shape