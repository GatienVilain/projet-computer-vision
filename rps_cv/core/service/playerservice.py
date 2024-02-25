import time

from rps_cv.core.config.coreconfig import CoreConfig

from rps_cv.core.entity.modelentity import ModelEntity
from rps_cv.core.service.userservice import UserService

class PlayerService(UserService):
    def __init__(self, videoService):
        super().__init__()

        self.videoService = videoService
        self.frame = None
        self.shape = None

        self.model = ModelEntity()

        self.delay = CoreConfig['player_choice_delay']
        self.gettingShape = False


    def makeAChoice(self):
        super().makeAChoice()

        self.gettingShape = True
        while self.gettingShape:

            self.frame = self.videoService.getFrame()
            self.shape = self.model.predict(self.frame)
            print("player shape: ", self.shape)

            time.sleep(self.delay / 1000)


    def getChoice(self):
        self.gettingShape = False
        time.sleep(self.delay / 1000)
        return self.shape


    def getFrame(self):
        return self.frame