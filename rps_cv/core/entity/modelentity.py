from keras.models import load_model

from rps_cv.core.config.coreconfig import CoreConfig
from rps_cv.core.utils.shape import Shape


class ModelEntity:
    def __init__(self,
                 model_path = CoreConfig['model_path']):
        self.model_path = model_path
        #self.model = load_model(self.model_path)


    def predict(self, frame):
        import random

        shape = Shape.NONE
        while shape is Shape.NONE:
            shape = random.choice(list(Shape))
        return shape

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