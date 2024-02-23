import tkinter

import PIL.Image, PIL.ImageTk

from rps_cv.app.templates.canvaslayout import CanvasLayout

class PlayerLayout(CanvasLayout):
    def __init__(self, container, vid):
        super().__init__(container)

        self.vid = vid

        self.__draw()

    def __draw(self):
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self,
                                     width = self.vid.width,
                                     height = self.vid.height)
        self.canvas.pack()

        self.Label = tkinter.Label(self, text="Ciseaux")
        self.Label.pack()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.\
                PhotoImage(image = PIL.Image.fromarray(frame))
        self.canvas.create_image(0, 0, image = self.photo,
                                       anchor = tkinter.NW)