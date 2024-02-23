import time

from rps_cv.app import App

if __name__ == "__main__":

    # Create a window and pass it to the Application object
    app = App("Pierre Papier Ciseaux",
              video_source = 0)
    app.run()