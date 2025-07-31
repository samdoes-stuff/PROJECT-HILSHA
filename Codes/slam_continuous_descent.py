

import time
import serial
from depthai_sdk import OakCamera
from some_slam_library import run_slam, estimate_map_quality, detect_bottom_surface

SERVO_DESCENT = b"DESCEND\n"
SERVO_ASCENT = b"ASCEND\n"
ESP_PORT = "/dev/ttyUSB0"
MAP_DISTANCE_THRESHOLD = 2.0
MAP_QUALITY_THRESHOLD = 97.0

def main():
    esp = serial.Serial(ESP_PORT, 115200, timeout=1)
    distance_mapped = 0.0
    full_map = []
    descending = True

    with OakCamera() as oak:
        camera = oak.create_stereo(depth=True)
        oak.start(blocking=False)

        while True:
            frame = camera.get_frame()
            slam_data = run_slam(frame)
            full_map.append(slam_data)
            distance_mapped += 0.1

            if descending and distance_mapped >= MAP_DISTANCE_THRESHOLD:
                quality = estimate_map_quality(full_map)
                if quality >= MAP_QUALITY_THRESHOLD:
                    esp.write(SERVO_DESCENT)
                    print("Descent triggered...")
                    distance_mapped = 0.0
                    time.sleep(3)  
                else:
                    print("Low quality, retrying scan...")
                    continue

            if detect_bottom_surface(frame):
                print("Bottom detected! Triggering ascent.")
                esp.write(SERVO_ASCENT)
                descending = False
                break

if __name__ == "__main__":
    main()
