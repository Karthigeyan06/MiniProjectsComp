#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

int pwmA = 3;
int pwmB = 5;
int in1 = 9;
int in2 = 10;
int in3 = 11;
int in4 = 12;

// PID constants
float Kp = 40;
float Ki = 0.5;
float Kd = 10;

float angle, error, previous_error;
float P = 0, I = 0, D = 0;
float PIDvalue = 0;

const int maxSpeed = 200;

int motorSpeed;

int16_t ax, ay, az;
int16_t gx, gy, gz;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
  
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(pwmA, OUTPUT);
  pinMode(pwmB, OUTPUT);

  analogWrite(pwmA, 0);
  analogWrite(pwmB, 0);
}

void loop() {
  angle = readAngle();
  error = 0 - angle;

  P = error;
  I = I + error;
  D = error - previous_error;

  PIDvalue = (Kp * P) + (Ki * I) + (Kd * D);
  PIDvalue = constrain(PIDvalue, -maxSpeed, maxSpeed);

  motorSpeed = PIDvalue;

  if (motorSpeed > 0) {
    forward();
  } else if (motorSpeed < 0) {
    backward();
  } else {
    stop();
  }

  analogWrite(pwmA, abs(motorSpeed));
  analogWrite(pwmB, abs(motorSpeed));

  previous_error = error;

  Serial.print("Angle: "); Serial.println(angle);
  Serial.print("Motor Speed: "); Serial.println(motorSpeed);
  Serial.println("----------");

  delay(1000);
}

float readAngle() {
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  float accAngle = atan2(ay, az) * 180 / PI;
  float gyroRate = gx / 131.0;

  static float angle = 0;
  float dt = 0.02;
  angle = 0.98 * (angle + gyroRate * dt) + 0.02 * accAngle;
  
  return angle;
}

void forward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}

void backward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void stop() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}
