#include <Time.h>
//-------------------
#define Ph1 9
#define Ph2 8
#define Ph4 7
#define Ph8 6

#define Pm1 10
#define Pm2 11
#define Pm4 12
#define Pm8 13
#define Pm16 A0
#define Pm32 A1

#define PM 5

#define interruptor 3
//-------------------
int h1=0;
int h2=0;
int h4=0;
int h8=0;

int m1=0;
int m2=0;
int m4=0;
int m8=0;
int m16=0;
int m32=0;
//-------------------
boolean suspend=false;
//-------------------
time_t t=0;
//-------------------
void setup(){
  pinMode(Ph1,OUTPUT);
  pinMode(Ph2,OUTPUT);
  pinMode(Ph4,OUTPUT);
  pinMode(Ph8,OUTPUT);

  pinMode(Pm1,OUTPUT);
  pinMode(Pm2,OUTPUT);
  pinMode(Pm4,OUTPUT);
  pinMode(Pm8,OUTPUT);
  pinMode(Pm16,OUTPUT);
  pinMode(Pm32,OUTPUT);

  pinMode(PM,OUTPUT);

  pinMode(interruptor,INPUT);

  Serial.begin(9600);
}

void loop(){
  t = now();
  if(Serial.available()){
    sync();
  }

  int hora = hour(t);
  if (hora>12){
    hora-=12;
  }
  int minuto = minute(t);


  Serial.print("Hora: ");
  Serial.print(hora);
  Serial.print(" Minutos: ");
  Serial.print(minuto);
  Serial.print(" Segundos: ");
  Serial.print(second(t));
  Serial.print(" PM: ");
  Serial.print(isPM());
  Serial.print(" PINMODE: ");
  Serial.println(digitalRead(interruptor));

  h1=bitRead(hora,0);
  h2=bitRead(hora,1);
  h4=bitRead(hora,2);
  h8=bitRead(hora,3);

  m1=bitRead(minuto,0);
  m2=bitRead(minuto,1);
  m4=bitRead(minuto,2);
  m8=bitRead(minuto,3);
  m16=bitRead(minuto,4);
  m32=bitRead(minuto,5);

//  if (digitalRead(interruptor)==LOW){    
    digitalWrite(Ph1,h1);
    digitalWrite(Ph2,h2);
    digitalWrite(Ph4,h4);
    digitalWrite(Ph8,h8);

    digitalWrite(Pm1,m1);
    digitalWrite(Pm2,m2);
    digitalWrite(Pm4,m4);
    digitalWrite(Pm8,m8);
    digitalWrite(Pm16,m16);
    digitalWrite(Pm32,m32);

    digitalWrite(PM,isPM());/*
  }
  else if (digitalRead(interruptor)==HIGH){
    digitalWrite(Ph1,LOW);
    digitalWrite(Ph2,LOW);
    digitalWrite(Ph4,LOW);
    digitalWrite(Ph8,LOW);

    digitalWrite(Pm1,LOW);
    digitalWrite(Pm2,LOW);
    digitalWrite(Pm4,LOW);
    digitalWrite(Pm8,LOW);
    digitalWrite(Pm16,LOW);
    digitalWrite(Pm32,LOW);

    digitalWrite(PM,LOW);
  }
  */
}

void sync() {
  String serial="";
  while(Serial.available()){
    char data=Serial.read();
    serial+=data;
  }
    setTime(serial.toInt());
}





