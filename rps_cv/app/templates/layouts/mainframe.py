from tkinter import *

from rps_cv.app.templates.layouts.computerlayout import ComputerLayout
from rps_cv.app.templates.layouts.playerlayout import PlayerLayout

from rps_cv.app.controller.computercontroller import ComputerController
from rps_cv.app.controller.playercontroller import PlayerController


class MainFrame(Frame):
    def __init__(self, container, videoService, playerService, computerService):
        super().__init__(container)

        self.videoService = videoService
        self.playerService = playerService
        self.computerService = computerService

        self.video_width = videoService.width
        self.video_height = videoService.height

        self.__draw()

        self.controller = None
        self.playerController = PlayerController(self.playerLayout,
                                                self.playerService,
                                                self.videoService)
        self.computerController = ComputerController(self.computerLayout,
                                                     self.computerService)


    def __draw(self):
        self.counterText = Label(self, text="1")
        self.counterText.pack()

        self.canvasRow = Frame(self)

        self.computerLayout = ComputerLayout(self.canvasRow,
                                             self.video_width,
                                             self.video_height)
        self.computerLayout.pack(side = LEFT)

        self.playerLayout = PlayerLayout(self.canvasRow,
                                         self.video_height,
                                         self.video_width)
        self.playerLayout.pack(side = RIGHT)

        self.canvasRow.pack()

        self.btn_snapshot = Button(self,
                                   text="Snapshot",
                                   width=50,
                                   command=self.nextRound)
        self.btn_snapshot.pack(anchor = CENTER, expand=True)


    def setController(self, computerController):
        self.controller = computerController


    def newGame(self):
        self.controller.newGame()


    def nextRound(self):
        self.controller.nextRound()


    def displayRoundLayout(self, delay):
        # TODO
        #pass
        print("Display round layout")
        self.after(delay, self.controller.getRoundWinner)


    def displayRoundReviewLayout(self):
        # TODO
        print("Display round Review layout")
        pass


    def displayGameReviewLayout(self):
        # TODO
        print("Display game Review layout")
        pass