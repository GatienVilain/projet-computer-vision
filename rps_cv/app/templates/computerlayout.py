import tkinter

from rps_cv.app.templates.canvaslayout import CanvasLayout

class ComputerLayout(CanvasLayout):
    def __init__(self, container, width, height):
        super().__init__(container)

        self.width = width
        self.height = height

        self.__draw()

    def __draw(self):
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self,
                                     width = self.width,
                                     height = self.height)
        self.canvas.pack()

        self.Label = tkinter.Label(self, text="Papier")
        self.Label.pack()
