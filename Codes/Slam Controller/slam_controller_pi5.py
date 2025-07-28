import os
import time
import serial
import subprocess

# ==== CONFIGURATIONS ====
SERIAL_PORT = '/dev/ttyUSB0'  # ESP-01 connected to Pi 5
BAUD_RATE = 115200
SLAM_FOLDER = '/home/pi/slam_data'
PI_ZERO_IP = '192.168.4.2'  # Pi Zero 2 W IP
PI_ZERO_USER = 'pi'
PI_ZERO_TARGET_FOLDER = '/home/pi/received_data/'
SCORE_THRESHOLD = 75

# ==== HELPERS ====

def get_latest_slam_file():
    files = [f for f in os.listdir(SLAM_FOLDER) if f.endswith('.ply') or f.endswith('.xyz')]
    if not files:
        return None
    files.sort(key=lambda x: os.path.getmtime(os.path.join(SLAM_FOLDER, x)), reverse=True)
    return os.path.join(SLAM_FOLDER, files[0])

def calculate_quality_score(file_path):
    print(f"[INFO] Evaluating file: {file_path}")
    size = os.path.getsize(file_path)
    score = min(100, size // 10000)  # Example: 10KB = 1 point
    print(f"[INFO] Calculated quality score: {score}")
    return score

def send_command_to_pixracer(command):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            ser.write((command + "\n").encode())
            print(f"[INFO] Sent command to PixRacer: {command}")
    except Exception as e:
        print(f"[ERROR] Failed to send command: {e}")

def send_file_to_pi_zero(file_path):
    try:
        subprocess.run([
            "scp",
            file_path,
            f"{PI_ZERO_USER}@{PI_ZERO_IP}:{PI_ZERO_TARGET_FOLDER}"
        ], check=True)
        print(f"[INFO] Sent file to Pi Zero 2 W: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to send file to Pi Zero: {e}")

# ==== MAIN LOOP ====
print("[START] Pi 5 SLAM Controller Running")
while True:
    latest_file = get_latest_slam_file()
    if latest_file:
        score = calculate_quality_score(latest_file)
        if score >= SCORE_THRESHOLD:
            send_command_to_pixracer("STOP_ROTATION")
            time.sleep(1)
            send_command_to_pixracer("DROP_WINCH")
            send_file_to_pi_zero(latest_file)
        else:
            print("[INFO] Score too low, skipping...")
    else:
        print("[INFO] No SLAM file found yet...")

    time.sleep(10)
