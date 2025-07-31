
#include <espnow.h>
#include <WiFi.h>

uint8_t peerAddress[] = {0x24, 0x6F, 0x28, 0xAB, 0xCD, 0xEF}; 

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  Serial.println("ESP-NOW UART bridge starting...");

  if (esp_now_init() != 0) {
    Serial.println("ESP-NOW init failed");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_COMBO);
  esp_now_add_peer(peerAddress, ESP_NOW_ROLE_COMBO, 1, NULL, 0);
  esp_now_register_recv_cb(onDataRecv);
  esp_now_register_send_cb(onDataSent);
}

void loop() {
  if (Serial.available()) {
    uint8_t buffer[250];
    int len = Serial.readBytes(buffer, sizeof(buffer));
    if (len > 0) {
      esp_now_send(peerAddress, buffer, len);
    }
  }
}

void onDataRecv(uint8_t *mac, uint8_t *data, uint8_t len) {
  Serial.write(data, len);
}

void onDataSent(uint8_t *mac, uint8_t status) {
  
}
