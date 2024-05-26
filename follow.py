import image
import car

class Follower:
    def __init__(self):
        self.detector = image.Detector()
        self.motors = car.Car()

    def follow(self, name: str, threshold = 0.0):
        """
        Follows an object with the given name.

        Args:
            name (str): The name of the object to follow.
            threshold (float): The minimum confidence score for an object to be considered.
        """
        pos = self.detector.locate(name, threshold)

        if pos is None:
            self.motors.stop()
            return
        
        x, y = pos
        print(f"Located: {x}, {y}")

        x = x - 0.5

        BASE_SPEED = 0.5
        ROTATE_SPEED = 0.3

        # Turn towards the object, while mostly moving forward
        self.motors.move(BASE_SPEED + x * ROTATE_SPEED, BASE_SPEED - x * ROTATE_SPEED)

    def __del__(self):
        del self.detector

follower = Follower()
while True:
    follower.follow("person")