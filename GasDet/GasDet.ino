#define BLYNK_TEMPLATE_ID "ID"
#define BLYNK_TEMPLATE_NAME "NAME"
#define BLYNK_AUTH_TOKEN "TOKEN"

#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

 
char auth[] = BLYNK_AUTH_TOKEN;

char ssid[] = "NetworkName"; 
char pass[] = "Password";
int smokeA0 = A0;
int data = 0;
int sensorThres = 100;


BlynkTimer timer;

void sendSensor(){
 
 int data = analogRead(smokeA0);
 Blynk.virtualWrite(V0, data);
  Serial.print("Pin A0: ");
  Serial.println(data);


  if(data > 300){
    
    Blynk.logEvent("gas_alert","Gas Leakage Detected");
  }
}

void setup(){
  pinMode(smokeA0, INPUT);
   Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  
  timer.setInterval(2500L, sendSensor);
}

void loop(){
  Blynk.run();
  timer.run();
}