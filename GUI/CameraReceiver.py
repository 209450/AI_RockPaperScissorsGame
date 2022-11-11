import cv2


class CameraReceiver:
    def __init__(self):
        self.camera = None

    def connect_to_url_camera(self, url):
        self.camera = cv2.VideoCapture(url)

    def retrieve_video_frame(self):
        ret, frame = self.camera.read()
        return frame

    def __del__(self):
        if self.camera is not None:
            self.camera.release()
