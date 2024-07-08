#define BLYNK_TEMPLATE_ID "YourTemplateID"
#define BLYNK_DEVICE_NAME "YourDeviceName"
#define BLYNK_AUTH_TOKEN "YourAuthToken"

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "YourNetworkName";
char pass[] = "YourPassword";

#define LDR1_PIN A0
#define LDR2_PIN A1
#define LDR3_PIN A2
#define RELAY_PIN D1

int ldr1Threshold = 500;
int ldr2Threshold = 500;
int ldr3Threshold = 500;

bool relayState = false;

BlynkTimer timer;

void checkLDRs() {
  int ldr1Value = analogRead(LDR1_PIN);
  int ldr2Value = analogRead(LDR2_PIN);
  int ldr3Value = analogRead(LDR3_PIN);

  
  Blynk.virtualWrite(V1, ldr2Value);
  Blynk.virtualWrite(V2, ldr3Value);

  
  if (ldr1Value < ldr1Threshold) {
    relayState = true;
  } else {
    relayState = false;
  }

  if (relayState) {
    digitalWrite(RELAY_PIN, HIGH);
  } else {
    digitalWrite(RELAY_PIN, LOW);
  }

  
  if (ldr2Value < ldr2Threshold) {
    Blynk.logEvent();
  }

  if (ldr3Value < ldr3Threshold) {
    Blynk.logEvent();
  }
}

BLYNK_WRITE(V0) {
  int pinValue = param.asInt();
  relayState = pinValue;
  digitalWrite(RELAY_PIN, relayState);
}

void setup() {
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);

  timer.setInterval(1000L, checkLDRs);
}

void loop() {
  Blynk.run();
  timer.run();
}
