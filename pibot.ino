#include <Arduino.h>

#define LEFT_FORWARD 7
#define LEFT_BACKWARD 8
#define RIGHT_FORWARD 11
#define RIGHT_BACKWARD 9
#define LEFT_SPEED 6
#define RIGHT_SPEED 5

void setup() {
    Serial.begin(9600);
    pinMode(LEFT_FORWARD, OUTPUT);
    pinMode(LEFT_BACKWARD, OUTPUT);
    pinMode(RIGHT_FORWARD, OUTPUT);
    pinMode(RIGHT_BACKWARD, OUTPUT);
    pinMode(LEFT_SPEED, OUTPUT);
    pinMode(RIGHT_SPEED, OUTPUT);
}

void loop() {    
    if (Serial.available() > 0) {
        char data = Serial.read();
        if (data == 'L') {
            float leftSpeed = Serial.parseInt();
            if (leftSpeed >= 0) {
                digitalWrite(LEFT_FORWARD, HIGH);
                digitalWrite(LEFT_BACKWARD, LOW);
                analogWrite(LEFT_SPEED, leftSpeed);
            } else {
                digitalWrite(LEFT_FORWARD, LOW);
                digitalWrite(LEFT_BACKWARD, HIGH);
                analogWrite(LEFT_SPEED, -leftSpeed);
            }
        } else if (data == 'R') {
            float rightSpeed = Serial.parseInt();
            if (rightSpeed >= 0) {
                digitalWrite(RIGHT_FORWARD, HIGH);
                digitalWrite(RIGHT_BACKWARD, LOW);
                analogWrite(RIGHT_SPEED, rightSpeed);
            } else {
                digitalWrite(RIGHT_FORWARD, LOW);
                digitalWrite(RIGHT_BACKWARD, HIGH);
                analogWrite(RIGHT_SPEED, -rightSpeed);
            }
        } else if (data == 'S') {
            digitalWrite(LEFT_FORWARD, LOW);
            digitalWrite(LEFT_BACKWARD, LOW);
            digitalWrite(RIGHT_FORWARD, LOW);
            digitalWrite(RIGHT_BACKWARD, LOW);
        }
    }
}