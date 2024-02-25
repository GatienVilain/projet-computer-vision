from tkinter import *

from rps_cv.app.templates.layouts.mainframe import MainFrame

from rps_cv.core.service.videoservice import VideoService
from rps_cv.core.service.playerservice import PlayerService
from rps_cv.core.service.computerservice import ComputerService

from rps_cv.app.controller.gamecontroller import GameController

from rps_cv.app.config.appconfig import AppConfig


class App(Tk):
    def __init__(self,
                 window_title = AppConfig["window_title"],
                 video_source = AppConfig["video_source"]):
        super().__init__()

        self.title(window_title)

        self.video_source = video_source
        self.videoService = VideoService(self.video_source)
        self.playerService = PlayerService(self.videoService)
        self.computerService = ComputerService()

        # Draw the window
        self.__draw()

        self.gameController = GameController(self.mainFrame,
                                            self.playerService,
                                            self.computerService)


    def __draw(self):
        self.mainFrame = MainFrame(self,
                                   self.videoService,
                                   self.playerService,
                                   self.computerService)
        self.mainFrame.pack()


    def run(self):
        self.mainloop()