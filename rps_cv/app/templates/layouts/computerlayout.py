import tkinter
import PIL.Image, PIL.ImageTk

from rps_cv.app.templates.layouts.genericlayout import GenericLayout

from rps_cv.core.utils.shape import Shape
from rps_cv.app.config.appconfig import AppConfig


class ComputerLayout(GenericLayout):
    def __init__(self, container, width, height):
        super().__init__(container)

        self.width = width
        self.height = height

        self.__draw()

        self.controller = None

    def __draw(self):
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self,
                                     width = self.width,
                                     height = self.height,
                                     bg = "gray")
        self.canvas.pack()

        self.Label = tkinter.Label(self, text="Patiente...")
        self.Label.pack()


    def setController(self, computerController):
        self.controller = computerController


    def update(self, labelText, shape):
        self.Label.config(text=labelText)

        self.img = PIL.ImageTk.PhotoImage(
            image = PIL.Image.open(AppConfig["shape_images"][shape])
        )

        self.canvas.create_image(self.width // 2, self.height // 2, image = self.img, anchor = "center")


    def hideChoice(self):
        self.update("Réfléchis...", "hidden")


    def showChoice(self, shape):
        if shape == Shape.ROCK:
            self.update("Pierre", "rock")
        elif shape == Shape.PAPER:
            self.update("Feuille", "paper")
        elif shape == Shape.SCISSORS:
            self.update("Ciseaux", "scissors")




