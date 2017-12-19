//http://www.hackeduca.com.br/ssd1306_oled-como-ligar/
// from https://playground.arduino.cc/Main/I2cScanner?action=sourceblock&num=1
#include <Wire.h>

void setup()
{
  Wire.begin();
  Serial.begin(9600);
  while (!Serial); 
  Serial.println("\nI2C Scanner");
}

void loop()
{
  byte error, address;
  int nDevices;
  Serial.println("Scaneando...");
  nDevices = 0;
  for(address = 1; address < 127; address++ ) 
  {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
    if (error == 0)
    {
      Serial.print("Dispositivo I2C encontrado no endereço 0x");
      if (address<16) 
        Serial.print("0");
      Serial.print(address,HEX);
      Serial.println("  !");

      nDevices++;
    }
    else if (error==4) 
    {
      Serial.print("Erro desconhecido no endereço 0x");
      if (address<16) 
        Serial.print("0");
      Serial.println(address,HEX);
    }    
  }
  if (nDevices == 0)
    Serial.println("Não encontramos nenhum dispositivo I2C\n");
  else
    Serial.println("pronto\n");
  delay(5000); 
}
