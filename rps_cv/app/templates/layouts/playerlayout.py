import tkinter

from rps_cv.app.templates.layouts.canvaslayout import CanvasLayout

from rps_cv.app.config.appconfig import AppConfig

class PlayerLayout(CanvasLayout):
    def __init__(self, container, width, height):
        super().__init__(container)

        self.width = width
        self.height = height
        self.delay = AppConfig["video_frame_delay"]

        self.__draw()

        self.controller = None

    def __draw(self):
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self,
                                     width = self.width,
                                     height = self.height)
        self.canvas.pack()

        self.Label = tkinter.Label(self, text="Ciseaux")
        self.Label.pack()


    def setController(self, playerController):
        self.controller = playerController


    def update(self):
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.canvas.create_image(0, 0, image = self.controller.getNewPhoto(),
                                       anchor = tkinter.NW)
        self.after(self.delay, self.update)
