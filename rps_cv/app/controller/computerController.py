
class ComputerController:
    def __init__(self, computerLayout, computerService):
        self.computerLayout = computerLayout
        self.computerLayout.setController(self)

        self.computerService = computerService

    def showResult(self):
        if self.computerService.isWinner():
            self.computerLayout.showWin()
        else:
            self.computerLayout.showLose()
