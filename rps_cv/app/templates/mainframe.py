from tkinter import *

from rps_cv.app.templates.layouts.computerlayout import ComputerLayout
from rps_cv.app.templates.layouts.playerlayout import PlayerLayout

from rps_cv.app.controller.videocontroller import VideoController
from rps_cv.app.controller.playercontroller import PlayerController


class MainFrame(Frame):
    def __init__(self, container, video_source):
        super().__init__(container)

        self.video_source = video_source
        self.videoController = VideoController(self.video_source)

        self.__draw()

        self.playerController = PlayerController(self.playerLayout, self.videoController)


    def __draw(self):
        self.counterText = Label(self, text="1")
        self.counterText.pack()

        self.canvasRow = Frame(self)

        self.computerLayout = ComputerLayout(self.canvasRow,
                                             self.videoController.width,
                                             self.videoController.height)
        self.computerLayout.pack(side = LEFT)

        self.playerLayout = PlayerLayout(self.canvasRow,
                                         self.videoController.width,
                                         self.videoController.height)
        self.playerLayout.pack(side = RIGHT)

        self.canvasRow.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = Button(self,
                                   text="Snapshot",
                                   width=50,
                                   command=self.videoController.snapshot)
        self.btn_snapshot.pack(anchor = CENTER, expand=True)