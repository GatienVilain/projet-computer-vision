from tkinter import *

from rps_cv.app.templates.computerlayout import ComputerLayout
from rps_cv.app.templates.playerlayout import PlayerLayout

from rps_cv.app.controller.videocapture import VideoCapture


class App(Tk):
    def __init__(self, window_title="Rock Paper Scissors", video_source=0):
        super().__init__()

        self.title(window_title)

        # open video source (by default this will try to open the computer webcam)
        self.video_source = video_source
        self.vid = VideoCapture(self.video_source)

        # Draw the window
        self.__draw()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.mainloop()


    def __draw(self):
        self.mainFrame = Frame(self)
        self.mainFrame.pack()

        self.counterText = Label(self.mainFrame, text="1")
        self.counterText.pack()

        self.canvasRow = Frame(self.mainFrame)

        self.computerLayout = ComputerLayout(self.canvasRow,
                                             self.vid.width,
                                             self.vid.height)
        self.computerLayout.pack(side = LEFT)

        self.playerLayout = PlayerLayout(self.canvasRow, self.vid)
        self.playerLayout.pack(side = RIGHT)

        self.canvasRow.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = Button(self.mainFrame,
                                   text="Snapshot",
                                   width=50,
                                   command=self.vid.snapshot)
        self.btn_snapshot.pack(anchor = CENTER, expand=True)


    def update(self):
        self.playerLayout.update()
        self.after(self.delay, self.update)