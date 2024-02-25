import tkinter

from rps_cv.app.templates.layouts.genericlayout import GenericLayout

from rps_cv.core.utils.shape import Shape
from rps_cv.app.config.appconfig import AppConfig

class PlayerLayout(GenericLayout):
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
                                     height = self.height,
                                     bg = "gray")
        self.canvas.pack()

        self.Label = tkinter.Label(self, text="Détection en cours...")
        self.Label.pack()


    def setController(self, playerController):
        self.controller = playerController


    def update(self, photo, shape):
        if shape == Shape.ROCK:
            self.Label.config(text="Pierre")
        elif shape == Shape.PAPER:
            self.Label.config(text="Feuille")
        elif shape == Shape.SCISSORS:
            self.Label.config(text="Ciseaux")

        self.canvas.create_image(0,0,image=photo,anchor=tkinter.NW)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.after(self.delay, self.controller.update)
