#include <Servo.h>

int time = 10000;//time befor opening parachute case

int jackPin = 2;
int ledPin = 3;
int motorPin = 9;
int buzzerPin = 6;

Servo myServo;

void setup()
{
  //init
  pinMode (jackPin, INPUT);
  pinMode (ledPin, OUTPUT);
  pinMode (buzzerPin, OUTPUT);
  
  myServo.attach(motorPin);
  myServo.write(0);
  
  
  while (digitalRead(jackPin)==1)//until removing jack
  {
    //waiting
  }
  digitalWrite(ledPin, HIGH);//turning n the led
  
  delay(time);//waiting until end of flight
  myServo.write(90);//realaising parachute
  analogWrite(buzzerPin, 90);
}
void loop()
{
  
  
}
