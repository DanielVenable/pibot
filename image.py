import tensorflow as tf
import tensorflow_hub as hub
import cv2

class Detector:
    def __init__(self):
        url = "https://www.kaggle.com/models/google/mobilenet-v2/TensorFlow1/openimages-v4-ssd-mobilenet-v2/1"

        self.model = hub.load(url).signatures['default']

        # Open camera
        self.cap = cv2.VideoCapture(0)

    def detect(self) -> dict:
        """
        Detects objects in an image captured from the camera.

        Returns: The prediction made by the model.
        """

        # Get image from camera
        success, image = self.cap.read()

        if not success:
            raise Exception("Could not get image from camera")

        # Preprocess image
        image = cv2.resize(image, (128, 128))
        image = (image / 255.0).astype('float32')
        image = tf.convert_to_tensor(image.reshape(1, 128, 128, 3))

        # Make prediction
        prediction = self.model(image)

        return prediction

    def find_objects(self, name: str, threshold = 0.0) -> list[tf.Tensor]:
        """
        Finds the bounding boxes of objects with the given name in the image.

        Args:
            name (str): The name of the object to search for.
            threshold (float): The minimum confidence score for an object to be considered.

        Returns: A list of bounding boxes (detection boxes) for the objects found,
            sorted by confidence score in descending order.
        """
        prediction = self.detect()
        names = prediction['detection_class_entities']
        scores = prediction['detection_scores']
        boxes = prediction['detection_boxes']

        return [
            boxes[i] for i in range(len(names))
            if names[i].numpy().decode().lower() == name.lower() and scores[i] > threshold]
    
    def locate(self, name: str, threshold = 0.0) -> tuple[int, int]:
        """
        Locates the center of the first object with the given name.

        Args:
            name (str): The name of the object to search for.
            threshold (float): The minimum confidence score for an object to be considered.

        Returns: The x and y coordinates of the center of the object, or `None` if no object found.
        """
        boxes = self.find_objects(name, threshold)

        if not boxes:
            return None

        box = boxes[0]
        x = (box[1] + box[3]) / 2
        y = (box[0] + box[2]) / 2

        return x, y

    def __del__(self):
        self.cap.release()