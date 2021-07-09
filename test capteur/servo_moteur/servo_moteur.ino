#include <Servo.h>
Servo myServo;

int motorPin = 9;
void setup() {
  // put your setup code here, to run once:

  myServo.attach(motorPin);
  delay(1000);
  myServo.write(0);
  delay(1000);
  
  myServo.write(90);//realaising parachute
  
  delay(1000);
  myServo.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:

}
