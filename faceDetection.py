import cv2
import mediapipe as mp
import time


class FaceDetector:

    def __init__(self, minDetectConf=0.5):
        
        self.minDetectConf = minDetectConf
        
        self.mpFace = mp.solutions.face_detection
        self.face = self.mpFace.FaceDetection(self.minDetectConf)
        self.mpDraw = mp.solutions.drawing_utils


    def detectFace(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.face.process(imgRGB)
        
        if self.results.detections and draw:
            for idx, detection in enumerate(self.results.detections):
                self.mpDraw.draw_detection(img, detection)

        return img

    def getPosition(self, img):
        
        detectionList = []
        
        if self.results.detections:
            for idx, detection in enumerate(self.results.detections):
                h, w, c = img.shape
                bboxC = detection.location_data.relative_bounding_box
                bbox = idx, int(bboxC.xmin * w), int(bboxC.ymin * h), int(bboxC.width * w), int(bboxC.height * h)
                score = int(detection.score[0] * 100)
                cv2.putText(img, str(score), (bbox[1], bbox[2]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
                detectionList.append([score, bbox])
        return detectionList
                
