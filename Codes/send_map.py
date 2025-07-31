
import serial
import time
import zlib

FILE = "map_compressed.ply.gz"
PORT = "/dev/ttyUSB0"
CHUNK_SIZE = 240

ser = serial.Serial(PORT, 115200, timeout=1)
time.sleep(2)

print(f"Sending {FILE} over ESP-NOW via ESP8266...")

with open(FILE, "rb") as f:
    file_data = f.read()

num_chunks = (len(file_data) + CHUNK_SIZE - 1) // CHUNK_SIZE

for i in range(num_chunks):
    chunk = file_data[i*CHUNK_SIZE:(i+1)*CHUNK_SIZE]
    index_bytes = i.to_bytes(2, 'big')
    checksum = zlib.crc32(chunk) & 0xFFFFFFFF
    checksum_bytes = checksum.to_bytes(4, 'big')

    packet = b'\xA5' + index_bytes + checksum_bytes + chunk
    ser.write(packet)
    time.sleep(0.01)

print("✅ Done sending!")
