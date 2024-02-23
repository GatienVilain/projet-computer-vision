from tkinter import *

from rps_cv.app.templates.mainframe import MainFrame

from rps_cv.app.controller.videocapture import VideoCapture

from rps_cv.app.config.appconfig import AppConfig


class App(Tk):
    def __init__(self,
                 window_title = AppConfig["window_title"],
                 video_source = AppConfig["video_source"]):
        super().__init__()

        self.title(window_title)

        # open video source (by default this will try to open the computer webcam)
        self.video_source = video_source
        self.vid = VideoCapture(self.video_source)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = AppConfig["delay"]

        # Draw the window
        self.__draw()


    def __draw(self):
        self.mainFrame = MainFrame(self, self.vid)
        self.mainFrame.pack()


    def run(self):
        self.update()
        self.mainloop()


    def update(self):
        self.mainFrame.update()
        self.after(self.delay, self.update)