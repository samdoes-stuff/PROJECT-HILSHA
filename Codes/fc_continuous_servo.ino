

#include <ESP8266WiFi.h>

const int servoPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(servoPin, OUTPUT);
  stopServo();
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "DESCEND") {
      rotateServoCW();
    } else if (cmd == "ASCEND") {
      rotateServoCCW();
    }
  }
}

void rotateServoCW() {
  analogWrite(servoPin, 80);  // CW
}

void rotateServoCCW() {
  analogWrite(servoPin, 160); // CCW
}

void stopServo() {
  analogWrite(servoPin, 0);  
}
