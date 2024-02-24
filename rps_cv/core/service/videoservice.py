import cv2
import time

from rps_cv.core.config.coreconfig import CoreConfig

from rps_cv.core.entity.videoentity import VideoEntity

class VideoService:
    def __init__(self,
                 video_source = CoreConfig["camera_source"]):
        self.video = VideoEntity(video_source)

    @property
    def width(self):
        return self.video.width

    @property
    def height(self):
        return self.video.height


    def getFrame(self):
        return self.video.getFrame()


    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.getFrame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg",
                        cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
