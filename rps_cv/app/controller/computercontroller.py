
from rps_cv.core.utils.shape import Shape

class ComputerController:
    def __init__(self, computerLayout, computerService):
        self.computerLayout = computerLayout
        self.computerLayout.setController(self)

        self.computerService = computerService


    def newRound(self):
        self.computerLayout.hideChoice()


    def revealChoice(self):
        self.shape = self.computerService.getChoice()
        self.computerLayout.showChoice(self.shape)