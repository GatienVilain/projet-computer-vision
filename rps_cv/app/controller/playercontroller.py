import PIL.Image, PIL.ImageTk

class PlayerController:
    def __init__(self, playerLayout, videoController):
        self.videoController = videoController

        self.playerLayout = playerLayout
        self.playerLayout.setController(self)
        self.playerLayout.update()

        self.photo = None

    def getNewPhoto(self):
        # Get a frame from the video source
        ret, frame = self.videoController.getFrame()

        if ret:
            self.photo = PIL.ImageTk.\
                PhotoImage(image = PIL.Image.fromarray(frame))

        return self.photo