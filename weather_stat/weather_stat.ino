#define BLYNK_TEMPLATE_ID "TMPL3xGxZ0V7q"
#define BLYNK_TEMPLATE_NAME "Weather Monitor"
#define BLYNK_AUTH_TOKEN "7QsYLAuqdGOor0g-uPIDYxIffDZjZJiz"

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP085.h>
#include <DHT.h>
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// Define DHT11 pin and type
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP085 bmp;

// Your WiFi credentials
char ssid[] = "Karthig";
char pass[] = "gkn__f14";

// Threshold values for alerts
float temperatureThreshold = 50.0; // Example: 30°C
float humidityThreshold = 70.0; // Example: 70%

void setup() {
  // Initialize serial communication
  Serial.begin(115200);

  // Initialize the DHT11 sensor
  dht.begin();

  // Initialize the BMP180 sensor
  if (!bmp.begin()) {
    Serial.println("Could not find a valid BMP085 sensor, check wiring!");
    while (1) {}
  }

  // Initialize Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop() {
  Blynk.run();
  sendSensorData();
  delay(2000); // Update every 2 seconds
}

void sendSensorData() {
  // Read temperature and humidity from DHT11
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Read pressure from BMP180
  float p = bmp.readPressure() / 100.0F; // Convert Pa to hPa

  // Print values to serial monitor
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C\t");
  Serial.print("Pressure: ");
  Serial.print(p);
  Serial.println(" hPa");

  // Send values to Blynk
  Blynk.virtualWrite(V1, t); // Temperature
  Blynk.virtualWrite(V2, h); // Humidity
  Blynk.virtualWrite(V3, p); // Pressure

  // Check conditions for alerts
  if (t > temperatureThreshold) {
    Blynk.logEvent("temp","Temperature above 50 degree celsius");

}
}