

#include <espnow.h>
#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  esp_now_init();
  esp_now_set_self_role(ESP_NOW_ROLE_COMBO);
  esp_now_register_recv_cb(onReceive);
}

void loop() {
  if (Serial.available()) {
    uint8_t buf[250];
    int len = Serial.readBytes(buf, sizeof(buf));
    if (len > 0) {
      
    }
  }
}

void onReceive(uint8_t *mac, uint8_t *data, uint8_t len) {
  Serial.write(data, len);  
}
