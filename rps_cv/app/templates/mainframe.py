from tkinter import *

from rps_cv.app.templates.layouts.computerlayout import ComputerLayout
from rps_cv.app.templates.layouts.playerlayout import PlayerLayout

class MainFrame(Frame):
    def __init__(self, container, vid):
        super().__init__(container)

        self.vid = vid

        self.__draw()


    def __draw(self):
        self.counterText = Label(self, text="1")
        self.counterText.pack()

        self.canvasRow = Frame(self)

        self.computerLayout = ComputerLayout(self.canvasRow,
                                             self.vid.width,
                                             self.vid.height)
        self.computerLayout.pack(side = LEFT)

        self.playerLayout = PlayerLayout(self.canvasRow, self.vid)
        self.playerLayout.pack(side = RIGHT)

        self.canvasRow.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = Button(self,
                                   text="Snapshot",
                                   width=50,
                                   command=self.vid.snapshot)
        self.btn_snapshot.pack(anchor = CENTER, expand=True)


    def update(self):
        self.playerLayout.update()