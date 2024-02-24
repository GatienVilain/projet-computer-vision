import random

from rps_cv.core.service.userservice import UserService
from rps_cv.core.utils.shape import Shape

class ComputerService(UserService):
    def __init__(self):
        super().__init__()

    def makeAChoice(self):
        super().makeAChoice()

        self.shape = Shape.NONE
        while self.shape is Shape.NONE:
            self.shape = random.choice(list(Shape))