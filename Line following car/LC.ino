#include <AFMotor.h>

// Initialize motors using L293D motor shield library
AF_DCMotor motor1(1); // Motor connected to M1
AF_DCMotor motor2(2); // Motor connected to M2
AF_DCMotor motor3(3); // Motor connected to M3
AF_DCMotor motor4(4); // Motor connected to M4

const int leftSensorPin = A4;
const int rightSensorPin = A5;

void setup() {
  Serial.begin(9600); // For debugging
  motor1.setSpeed(100); // Set initial motor speed (0-255)
  motor2.setSpeed(100);
  motor3.setSpeed(100);
  motor4.setSpeed(100);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void loop() {
  // Read IR sensor values
  int leftValue = analogRead(leftSensorPin);
  int rightValue = analogRead(rightSensorPin);

  // Threshold to detect line (adjust based on sensor readings)
  const int threshold = 500;
  bool leftSensor = leftValue < threshold;  // LOW when detecting black line
  bool rightSensor = rightValue < threshold; // LOW when detecting black line

  Serial.print("Left Sensor: ");
  Serial.print(leftSensor);
  Serial.print(" | Right Sensor: ");
  Serial.println(rightSensor);

  // Line-following logic
  if (!leftSensor && !rightSensor) {
    // Case 1: Both sensors detect the black line (move forward)
    moveForward();
  } else if (!leftSensor && rightSensor) {
    // Case 2: Left sensor detects the line, right sensor off the line (turn right)
    turnLeft();
  } else if (leftSensor && !rightSensor) {
    // Case 3: Right sensor detects the line, left sensor off the line (turn left)
    turnRight();
  } else {
    // Case 4: Both sensors off the line (stop)
    stopMotors();
  }
}

void moveForward() {
  motor1.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor2.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor3.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor4.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor1.setSpeed(100);
  motor2.setSpeed(100);
  motor3.setSpeed(100);
  motor4.setSpeed(100);
}

void turnRight() {
  // Slow down left motors to turn right
  motor1.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor2.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor3.run(RELEASE);  // Stop or slow down left motors
  motor4.run(RELEASE);  // Stop or slow down left motors
  motor1.setSpeed(100);
  motor2.setSpeed(100);
}

void turnLeft() {
  // Slow down right motors to turn left
  motor1.run(RELEASE);  // Stop or slow down right motors
  motor2.run(RELEASE);  // Stop or slow down right motors
  motor3.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor4.run(BACKWARD); // Swap FORWARD to BACKWARD
  motor3.setSpeed(100);
  motor4.setSpeed(100);
}

void stopMotors() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}
