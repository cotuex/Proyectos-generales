#include <SoftwareSerial.h>
SoftwareSerial wifiPort(2,3); // RX, TX
void setup()
{
  Serial.begin(9600);
  wifiPort.begin(9600);
  wifiPort.println("AT+RST");
  delay(1000);
  wifiPort.println("AT");
}
void loop() // run over and over
{
  wifiPort.listen();
  if (wifiPort.available() ) {
    Serial.write(wifiPort.read());
  }
  if (Serial.available() ){
    wifiPort.write(Serial.read());
  }
}

