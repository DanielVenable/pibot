import serial

class Car:
    def __init__(self):
        self.serial_connection = serial.Serial('/dev/ttyUSB0', 9600)

    def move(self, left, right):
        """
        Moves the robot.

        Args:
            left (int): The speed of the left motor.
            right (int): The speed of the right motor.
        """
        self.serial_connection.write(f"L{int(left * 255)}R{int(right * 255)}".encode())

    def stop(self):
        self.serial_connection.write(b"S")