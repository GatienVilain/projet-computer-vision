import tkinter

from rps_cv.app import App

if __name__ == "__main__":

    # Create a window and pass it to the Application object
    App("Pierre Papier Ciseaux",
        tkinter.Tk(),
        video_source = 0)