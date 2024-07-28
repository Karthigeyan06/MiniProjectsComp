#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define RST_PIN D3  // Define the reset pin for the RFID reader
#define SS_PIN D4   // Define the slave select (chip select) pin for the RFID reader

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance
LiquidCrystal_I2C lcd(0x27, 16, 2); // Set the LCD address to 0x27 for a 16 chars and 2 line display

// Wi-Fi credentials
const char* ssid = "Karthig";
const char* password = "gkn__f14";
const char* serverUrl = "http://192.168.213.105:5000/mark_attendance";

// Define known UID strings
String knownUIDs[] = {"5386D826", "4357F313", "6752975F"};
String rollNumbers[] = {"202202039", "202202038", "202202030"};

void setup() {
  Serial.begin(9600); // Initialize serial communications with the PC
  SPI.begin();        // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Scan your ID");

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  lcd.setCursor(0, 1);
  lcd.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("WiFi connected");
  delay(1000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Scan your ID");
}

void loop() {
  if (!mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  if (!mfrc522.PICC_ReadCardSerial()) {
    return;
  }

  String content = "";
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();

  lcd.clear();
  lcd.setCursor(0, 0);

  bool knownTag = false;
  for (int i = 0; i < 3; i++) {
    if (content == knownUIDs[i]) {
      String message = "Roll: " + rollNumbers[i];
      Serial.println("Attendance marked for: " + rollNumbers[i]);
      lcd.print(message);
      knownTag = true;

      // Send data to the server
      if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;
        WiFiClient client;

        http.begin(client, serverUrl);
        
        http.addHeader("Content-Type", "application/x-www-form-urlencoded");
        String postData = "roll_number=" + rollNumbers[i];
        int httpResponseCode = http.POST(postData);
        if (httpResponseCode > 0) {
          String response = http.getString();
          Serial.println(httpResponseCode);
          Serial.println(response);
        } else {
          Serial.print("Error on sending POST: ");
          Serial.println(httpResponseCode);
        }
        http.end();
      } else {
        Serial.println("Error in WiFi connection");
      }

      break;
    }
  }

  if (!knownTag) {
    lcd.print("Unknown tag");
  }

  delay(2000);  // Display message for 2 seconds

  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Scan your ID");
}
