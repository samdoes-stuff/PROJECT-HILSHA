

import serial
import zlib

PORT = "/dev/ttyUSB0"
OUTPUT = "received_map.ply.gz"

ser = serial.Serial(PORT, 115200, timeout=2)
received_chunks = {}

print("📡 Receiving data...")

while True:
    if ser.in_waiting >= 7:
        header = ser.read(1)
        if header != b'\xA5':
            continue

        index = int.from_bytes(ser.read(2), 'big')
        checksum = int.from_bytes(ser.read(4), 'big')
        chunk = ser.read(240)

        if zlib.crc32(chunk) & 0xFFFFFFFF == checksum:
            received_chunks[index] = chunk
            print(f"✅ Received chunk #{index}")
        else:
            print(f"❌ Corrupted chunk #{index}, skipping")

    if len(received_chunks) > 0 and max(received_chunks.keys()) - min(received_chunks.keys()) + 1 == len(received_chunks):
        break

with open(OUTPUT, "wb") as f:
    for i in sorted(received_chunks.keys()):
        f.write(received_chunks[i])

print(f"📁 Saved full map to {OUTPUT}")
