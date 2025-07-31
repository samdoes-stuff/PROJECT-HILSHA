

#include <espnow.h>
#include <WiFi.h>

uint8_t pi0MAC[] = {0x24, 0x6F, 0x28, 0xYY, 0xYY, 0xYY};  // Pi Zero ESP MAC
uint8_t fcMAC[] = {0x24, 0x6F, 0x28, 0xZZ, 0xZZ, 0xZZ};   // FC ESP MAC

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  esp_now_init();

  esp_now_set_self_role(ESP_NOW_ROLE_COMBO);
  esp_now_add_peer(pi0MAC, ESP_NOW_ROLE_COMBO, 1, NULL, 0);
  esp_now_add_peer(fcMAC, ESP_NOW_ROLE_COMBO, 1, NULL, 0);
  esp_now_register_recv_cb(onReceive);
}

void loop() {
  if (Serial.available()) {
    uint8_t buffer[250];
    int len = Serial.readBytes(buffer, sizeof(buffer));
    if (len > 0) {
      esp_now_send(pi0MAC, buffer, len);  
    }
  }
}

void onReceive(uint8_t *mac, uint8_t *incomingData, uint8_t len) {
  Serial.write(incomingData, len); 
}
