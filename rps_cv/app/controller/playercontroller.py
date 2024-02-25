import PIL.Image, PIL.ImageTk

class PlayerController:
    def __init__(self, playerLayout, playerService, videoService):
        self.playerLayout = playerLayout
        self.playerLayout.setController(self)

        self.playerService = playerService
        self.videoService = videoService

        self.photo = None
        self.roundReview = False

        self.playerLayout.update()

    def getNewPhoto(self):
        if self.roundReview: return self.photo

        # Get a frame from the video source
        ret, frame = self.videoService.getFrame()

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
