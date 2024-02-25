from tkinter import *

from rps_cv.app.templates.layouts.computerlayout import ComputerLayout
from rps_cv.app.templates.layouts.playerlayout import PlayerLayout

from rps_cv.app.controller.computercontroller import ComputerController
from rps_cv.app.controller.playercontroller import PlayerController

from rps_cv.app.config.appconfig import AppConfig
from rps_cv.core.utils.turnresult import TurnResult

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

        self.default_counter = AppConfig["round_duration"]
        self.counter = self.default_counter

    def __draw(self):
        self.canvasRow = Frame(self, height=self.video_height)

        self.computerLayout = ComputerLayout(self.canvasRow,
                                             self.video_width,
                                             self.video_height)
        self.computerLayout.pack(side = LEFT)

        self.counterText = Label(self.canvasRow,
                                 text="Victoires",
                                 width=12)
        self.counterText.pack(side = LEFT)

        self.playerLayout = PlayerLayout(self.canvasRow,
                                         self.video_width,
                                         self.video_height)
        self.playerLayout.pack(side = RIGHT)

        self.canvasRow.pack()

        self.btn_nextround = Button(self,
                                   text="Tour suivant",
                                   width=50,
                                   command=self.nextRound)
        self.btn_nextround.pack(anchor = CENTER, expand=True)


    def setController(self, computerController):
        self.controller = computerController


    def newGame(self):
        self.controller.newGame()


    def nextRound(self):
        self.controller.nextRound()


    def displayRoundLayout(self, delay):
        self.computerController.newRound()
        self.playerController.unsetRoundReview()
        self.updateCounter(self.default_counter)
        self.btn_nextround.pack_forget()

        self.after(delay, self.controller.getRoundWinner)


    def displayRoundReviewLayout(self):
        self.computerController.revealChoice()
        self.playerController.setRoundReview()
        self.showLabelResult()
        self.btn_nextround.pack(anchor = CENTER, expand=True)


    def displayGameReviewLayout(self):
        pass


    def updateCounter(self, counter = None):
        if counter: self.counter = counter
        self.counterText.config(text=str(self.counter))
        self.counter -= 1
        if self.counter > 0:
            self.after(1000, self.updateCounter)


    def showLabelResult(self):
        result = self.controller.roundResult
        if result == TurnResult.WIN:
            self.counterText.config(text="Victoire")
        elif result == TurnResult.LOSE:
            self.counterText.config(text="Défaite")
        elif result == TurnResult.DRAW:
            self.counterText.config(text="Égalité")