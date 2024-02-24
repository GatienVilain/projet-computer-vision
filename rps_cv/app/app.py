from tkinter import *

from rps_cv.app.templates.mainframe import MainFrame

from rps_cv.app.config.appconfig import AppConfig


class App(Tk):
    def __init__(self,
                 window_title = AppConfig["window_title"],
                 video_source = AppConfig["video_source"]):
        super().__init__()

        self.title(window_title)

        self.video_source = video_source

        # Draw the window
        self.__draw()


    def __draw(self):
        self.mainFrame = MainFrame(self, self.video_source)
        self.mainFrame.pack()


    def run(self):
        self.mainloop()