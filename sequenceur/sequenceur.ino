#include <Servo.h>

//led du haut (rouge) : directement connécté sur l'interupteur, représente l'alimentation 9V
//led du milieu (jaune) : s'allume quand le cable jack a été araché, l'arduino commence à compter
//led du bas (vert) : c'est la sortie du cable jack : allumé=jack branché ; éteint=jack débranché

int time = 18000;//time befor opening parachute case

int jackPin = 2;
int ledPin = 3;
int motorPin = 9;
int buzzerPin = 6;
int pos = 0; 
long timer_secu = 0; 
long last_time_pluged=0;
long millis_now=0;

Servo myServo;

void setup()
{
  //init
  pinMode (jackPin, INPUT);
  pinMode (ledPin, OUTPUT);
  pinMode (buzzerPin, OUTPUT);
  
  myServo.attach(motorPin);

  for (pos = 180; pos >= 170; pos -= 1) { //cette fonction remet le bras en position de départ
    myServo.write(pos);             
    delay(15);                       
  }
  
  while (timer_secu<1000)//until removing jack
  {
    millis_now=millis();
    if(digitalRead(jackPin)==1){
      last_time_pluged=millis_now;
    }
    
    timer_secu=millis_now-last_time_pluged;
  }
  digitalWrite(ledPin, HIGH);//turning n the led
  
  delay(time);//waiting until end of flight
  

 for (pos = 180; pos >= 95; pos -= 1) { //realaising parachute
    myServo.write(pos);            
    delay(50);                      
  }
  analogWrite(buzzerPin, 90);
}
void loop()
{
  
  
}
