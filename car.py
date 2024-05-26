import gpiozero as gpio

class Car:
    def __init__(self):
        self.motor_left = gpio.Motor(6, 13)
        self.motor_right = gpio.Motor(16, 20)
        self.speed_left = gpio.PWMOutputDevice(5)
        self.speed_right = gpio.PWMOutputDevice(21)

        # TODO: Specify pins for motors and speed control.

    def move(self, left, right):
        """
        Moves the robot.

        Args:
            left (int): The speed of the left motor.
            right (int): The speed of the right motor.
        """

        self.speed_left.value = left
        self.speed_right.value = right

        if left > 0:
            self.motor_left.forward()
        else:
            self.motor_left.backward()

        if right > 0:
            self.motor_right.forward()
        else:
            self.motor_right.backward()

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()