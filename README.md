# Face Detection System using Mediapipe

This project is a Python-based face detection system that utilizes the Mediapipe library and OpenCV. The system provides the ability to detect faces in images or video streams, drawing bounding boxes around the detected faces and providing their positions and scores.

## Dependencies

The following dependencies are required to run the script:

- OpenCV
- Mediapipe

You can install these dependencies using pip:

```shell
pip install opencv-python mediapipe
```

## Usage

To use the `FaceDetector` class in your own code, you can import it as follows:

```python
from face_detector import FaceDetector
```

Then, create an instance of the `FaceDetector` class with your desired configuration:

```python
detector = FaceDetector(minDetectConf=0.5)
```

You can adjust the `minDetectConf` parameter based on your desired confidence threshold for face detection.

After creating the `FaceDetector` object, you can call its methods to detect faces in images or video frames.

For example, to detect faces in a single image:

```python
import cv2

image = cv2.imread("image.jpg")
detected_image = detector.detectFace(image)
face_positions = detector.getPosition(image)
# Process the detected image and face positions as needed
```

Refer to the script for more details and examples on how to use the `FaceDetector` class.

## Acknowledgements

The face detection system in this project is powered by the Mediapipe library, which provides the face detection model used for detecting faces in images and video streams.
