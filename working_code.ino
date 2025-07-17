#include <cvzone.h>
#include <Servo.h>

Servo LServo;
Servo RServo;
Servo HServo;

const int LS_pin = 8;
const int RS_pin = 9;
const int HS_pin = 10;

SerialData serialData(3, 3); // 3 values, max 3 digits each
int valsRec[3];

void setup() {
  serialData.begin();  // uses Serial.begin(9600) internally
  LServo.attach(LS_pin);
  RServo.attach(RS_pin);
  HServo.attach(HS_pin);
}

void loop() {
  serialData.Get(valsRec); // Receive [val1, val2, val3]
  LServo.write(valsRec[0]);
  RServo.write(valsRec[1]);
  HServo.write(valsRec[2]);
}
