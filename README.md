# PROJECT-HILSHA

# 🌕A Lunar Cave Explorer 🚀🕳️  
> *"Because even the Moon has dark secrets."*

## 🛠️ What's This?  
Welcome to **Lunar Cave Explorer** – a robot with a mission: explore extraterrestrial potholes without falling apart or crying in zero gravity.

It’s a **three-module**, **servo-powered**, **ESP-NOW-connected**, **3D-mapping**, **autonomous lunar spelunking monster**.  
Made on Earth. Built to map the Moon. Or your backyard sewer system. Either works.

---

## 💡 The Idea  
Caves on the Moon? Mysterious. Unexplored. Potential future real estate.  
But they’re also dark, deep, and scary. So naturally, I sent a robot instead.

The system has **three main characters** in this sci-fi drama:

- 🧃 **Battery Base**: Solar-powered, stays at the cave entrance like your introverted friend at parties.  
- 🛸 **The Rover**: A Raspberry Pi Zero 2 W tank that drops off modules, rolls out like a boss, and handles the logistics.  
- 📷 **3D Mapping Module**: A brainy payload with OAK-D Lite + lights + a servo winch that drops itself into the cave and scans it like a boss.

---

## ⚙️ How It Works  
1. Everything launches bundled up like IKEA furniture.  
2. Rover transports the **Battery Base** to one side of the cave, detaches it like a secret agent.  
3. Then it pulls a full 180° move and drops anchor at the other side.  
4. In between: the heavy-lifting **servo winch** (shoutout to Injora) suspends the **3D mapping module** like it's rappelling into a lunar rave.  
5. Mapping module descends slowly and dramatically.  
6. Inside: Raspberry Pi 5, flight controller, OAK-D Lite, and LED light show.  
7. It captures 3D footage + IMU data using SLAM because **science.**  
8. Once mapped: file is compressed and sent back wirelessly via ESP-NOW.  
9. Repeat. Map again. Go deeper. Flex on aliens.

---

## 📡 Communication Protocol  
- **ESP-01 modules** send love letters between modules over ESP-NOW.  
- **Flight controller (Pixracer)** talks to Raspberry Pi for both IMU data and servo control.  
- **Camera footage** + IMU => mashed into a 3D point cloud.  
- **Compression** happens onboard because bandwidth is sacred.  

---

## 🧠 Technologies Used  
- 🧠 Raspberry Pi 5 & Zero 2 W  
- 📡 ESP8266 (ESP-01)  
- 🧲 Pixracer flight controller  
- 📷 OAK-D Lite (for delicious stereo depth)  
- 🔦 High-intensity LED  
- 🔧 Injora servo winch (the muscle)  
- 🔌 Lots of wires (don’t judge)  
- 🤯 SLAM mapping (Simultaneous Localization And Mind-blowingness)

---

## 🚨 Known Issues  
- Gravity on Earth ruins the lunar aesthetic  
- Servo drama if you mess up degrees vs radians  
- People ask "Why?" instead of "How can I help?"

---

## 📦 Setup  
Just kidding. If you're asking this, you're probably not ready.  
But in case you are:

1. Flash your Raspberry Pis.  
2. Flash your ESP-01s.  
3. Wire your servos.  
4. Connect everything like your life depends on it.  
5. Press the button.  
6. Wait for magic.

---

## 🤖 Can it be used on Earth?  
Yes. But it’ll feel underappreciated.

---

## ✨ Final Thoughts  
I built this because I love robots, caves, and doing things NASA *should* be doing.  
This was hard, chaotic, and full of servo-related trauma. But worth it.

---

## ☕ Buy me a coffee  
Not really. But leave a 🌟 if you want to make my day.

---

## License  
MIT — because knowledge should be as free as this rover. 

<img width="952" height="511" alt="Screenshot 2025-07-25 142617" src="https://github.com/user-attachments/assets/747136d2-8fec-4163-a86b-75fc30849ff0" />

