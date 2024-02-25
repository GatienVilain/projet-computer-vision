import PIL.Image, PIL.ImageTk

class PlayerController:
    def __init__(self, playerLayout, playerService, videoService):
        self.playerLayout = playerLayout
        self.playerLayout.setController(self)

        self.playerService = playerService
        self.videoService = videoService

        self.photo = None
        self.roundReview = False

        self.update()


    def update(self):
        if not self.roundReview:
            self.getNewPhoto()

        self.shape = self.playerService.shape
        self.playerLayout.update(self.photo, self.shape)


    def getNewPhoto(self):
        # Get a frame from the video source
        ret, frame = self.videoService.getFrame()

        if ret:
            self.photo = PIL.ImageTk.\
                PhotoImage(image = PIL.Image.fromarray(frame))

        return self.photo


    def setRoundReview(self):
        self.roundReview = True


    def unsetRoundReview(self):
        self.roundReview = False
