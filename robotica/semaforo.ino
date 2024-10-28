int rojo=13;
int amarillo=12;
int verde=11;
  
  
void setup()
{
pinMode(rojo,OUTPUT);
pinMode(amarillo,OUTPUT);
pinMode(verde,OUTPUT);
}

void loop()
{
  digitalWrite(verde,HIGH);
  delay(2000);
  digitalWrite(verde,LOW);
    
  digitalWrite(amarillo,HIGH);
  delay(1000);
  digitalWrite(amarillo,LOW);
    
  digitalWrite(rojo,HIGH);
  delay(4000);
  digitalWrite(rojo,LOW);
}