import PIL.Image, PIL.ImageTk

class PlayerController:
    def __init__(self, playerLayout, playerService, videoController):
        self.playerService = playerService
        self.videoController = videoController

        self.playerLayout = playerLayout
        self.playerLayout.setController(self)
        self.playerLayout.update()

        self.photo = None
        self.roundReview = False


    def getNewPhoto(self):
        if roundReview: return self.photo

        # Get a frame from the video source
        ret, frame = self.videoController.getFrame()

        if ret:
            self.photo = PIL.ImageTk.\
                PhotoImage(image = PIL.Image.fromarray(frame))

        return self.photo


    def showResult(self):
        roundReview = True
        if self.playerService.isWinner():
            self.playerLayout.showWin()
        else:
            self.playerLayout.showLose()


    def unsetRoundReview(self):
        roundReview = False
