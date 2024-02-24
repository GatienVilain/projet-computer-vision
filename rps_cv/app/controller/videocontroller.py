
from rps_cv.core.service.videoservice import VideoService

class VideoController:
    def __init__(self, video_source):
        self.video_source = video_source
        self.videoService = VideoService(self.video_source)

        self.width = self.videoService.width
        self.height = self.videoService.height


    def getFrame(self):
        return self.videoService.getFrame()


    def snapshot(self):
        self.videoService.snapshot()
