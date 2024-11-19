#define BLYNK_TEMPLATE_ID "TMPL3TuV_6il4"
#define BLYNK_TEMPLATE_NAME "SmartIrrigation"
#define BLYNK_AUTH_TOKEN "0lUW7hIu_eBRtRj90QOT0n7s6tObncR_"

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "0lUW7hIu_eBRtRj90QOT0n7s6tObncR_"; // Blynk Auth Token
char ssid[] = "Ooo"; // WiFi Network Name
char pass[] = "aasish123"; // WiFi Password

int sensorPin = A0; // Soil Moisture Sensor Pin
int relayPin = D0; // Relay Pin
int threshold = 40; // Moisture threshold percentage


BLYNK_WRITE(V3) { 
  int buttonState = param.asInt();
  Serial.print("Button state: ");
  Serial.println(buttonState);
  if (buttonState == 1) {
    digitalWrite(relayPin, LOW); 
    Serial.println("Water pump turned ON");
  } else {
    digitalWrite(relayPin, HIGH);
    Serial.println("Water pump turned OFF");
  }
}

void setup() {
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);

  pinMode(sensorPin, INPUT);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH); 

  Serial.println("Setup complete. Connecting to Blynk...");
}

void loop() {
  Blynk.run();
  
  int moistureValue = analogRead(sensorPin); 
  int moisturePercentage = map(moistureValue, 1023, 0, 0, 100);
  Blynk.virtualWrite(V2, moisturePercentage);
  
  Serial.print("Raw Sensor Value: ");
  Serial.println(moistureValue);
  Serial.print("Moisture Level: ");
  Serial.print(moisturePercentage);
  Serial.println("%");

  if (moisturePercentage < threshold) {
    Blynk.logEvent("lowmoisture", "Low Moisture Detected!");
    Serial.println("Low moisture detected, alert sent.");
  }
  
  delay(1000);
}
