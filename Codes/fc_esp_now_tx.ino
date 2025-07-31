
#include <espnow.h>
#include <WiFi.h>

uint8_t pi5MAC[] = {0x24, 0x6F, 0x28, 0xXX, 0xXX, 0xXX};  // Pi 5 ESP MAC here

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  if (esp_now_init() != 0) {
    Serial.println("ESP-NOW init failed");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_COMBO);
  esp_now_add_peer(pi5MAC, ESP_NOW_ROLE_COMBO, 1, NULL, 0);
}

void loop() {
  if (Serial.available()) {
    uint8_t data[250];
    int len = Serial.readBytes(data, sizeof(data));
    if (len > 0) {
      esp_now_send(pi5MAC, data, len);
    }
  }
}
