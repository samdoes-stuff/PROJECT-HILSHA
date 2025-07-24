# journal.md

## Note before reading

I honestly didn't know how to write a journal or what it exactly means, so I struggled to register daily logs. This is my raw, honest, daily record for GitHub, capturing the exact things I did and my frustrations.

## Day 1 – Dopamine Rush & Existential Crisis (28 JUNE 2025)

Saw the IRO post.  
Got hyped.  
Realized I have no project.  
Got depressed.  

Main theme: **Space Robots.**  
Brain: "We can totally build a Lunar Cave Explorer Robot."  
Reality: "Can we though?"  

Proceeded to conduct "research" (read: aggressively Googling at 3 AM).  
Found nothing that says "you can’t do it," which made me **even more excited**.  
**Conclusion:** If no one did it yet, that’s a *feature*. ~ 2 hours

## Day 2 – Flight Controller Rabbit Hole (29 JUNE 2025)

Dual gyro-redundancy flight controllers?  
**Hell crazy expensive + not even mini.**

Me: "Ok, let’s clone one."  
Dived into ArduPilot’s site like a smurf looking for berries.  
Found an open-source controller with:

✅ ArduPilot compatibility  
✅ Dual gyro  
✅ Open schematics  
✅ 3D files  
✅ “Beyond” files (whatever those are)  

**Best part:** Found third-party retailers from “Bangdoodh” (Banggood, but my dopamine-addled brain read it wrong) selling them for **$75 instead of $200+.**

**Bad news:** It’s discontinued, but hey, still supported for normal Pixhawk versions.

Sadly, Pixhawk normal versions are big chonks, not fitting my tiny lunar bot dreams.  
Also, they don’t give me a *dedicated Wi-Fi data link* for easy log transfers.  
That’s why I decided: **I’m cloning it.**

---

*Note: I still don’t know how to write a journal properly, so here it is in my chaos style. Enjoy the ride as I try to build a lunar cave explorer while riding dopamine waves.*

https://ardupilot.org/copter/docs/common-pixracer-overview.html

~ 3 hours


## Day 3 – The “Which Schematic Is It” Saga (30 JUNE 2025)

I found out the schematic linked in the repo wasn’t even for the **PixRacer** I’m trying to clone.  
Apparently, there are **a billion PixRacer versions:**

- Pixhawk version  
- Holybro version  
- [Insert another vendor here] version

Result: *Confusion and mild mental dismantlement*.

I **smurfed** (stalked) the owner’s GitHub repo like a raccoon in a trash can until I *finally* found the exact schematics and design files.

Bad news: All of it was in **Altium Designer** (aka *LTM designer in my brain*), which is hella expensive and doesn’t give student packages for high school students.  
Result: Got **rekt again**.

To keep sanity, I decided to **redraw the schematics in EasyEDA** for my understanding and rebuild it from scratch.  
Oh, and some schematics were *missing parts in the middle*.

---

*Note: I still don’t know how to write a journal, but this chaos is now immortalized for future me (or future contributors) to understand why I’m building a lunar cave explorer bot while battling overpriced CAD tools.* ~ 6 hours

https://firmware.ardupilot.org/Rover/

https://drive.google.com/file/d/13R---X2ncpKuxhJewDeZoGOMFhPUqMNB/view?usp=drive_link


## Day 4 – PCB Existential Crisis (1 July 2025)

**Working on schematics again. Working on schematics again.**

Finally, **finished the schematics** (🎉 tiny victory).  
Now came the **worst nightmare: component sourcing**.

- “Which capacitor should I use, 0603 or 0402?”  
- “What should I include in my PCB design?”  
- “What should my PCB layout look like?”  
- “How do I make it look exactly the same as the reference?”

When I redrew the schematic in EasyEDA, I *forgot* I would actually have to **lay out a PCB too.**

The open-source hardware repo had a PCB in Altium Designer (or *LTM designer* in my caffeine brain), but I couldn’t find a clean PCB export, only schematics.

What did I do?  
Went back to the GitHub repo, found an **`.ltm` file** (still don’t know what that means).

Uploaded it to an LTM viewer. Boom:  
**Turns out you can download the PCB separately from there.**

So I did exactly that. ~ 4 hours

https://365.altium.com/files/DE5E7958-BE7D-470E-812E-0988A14BB30F


## Day 5 – BOM Madness & SMD Headache ( 9 July 2025)

Took a **1-week break** (exams cooked my brain 🧠🔥).  
Came back, saw my PCB files, and stepped into **Day 5: Component Sourcing Hell.**

Making the BOM should’ve been chill. Sourcing **MCU and gyros? Easy.**  
But then came **the mini demons: capacitors and resistors.**

I didn’t realize they have *footprints* (apparently called SMD components) that you have to match *exactly*.  
Found out my **normal soldering iron won’t even work**, and I need a **hot air gun** just to put these rice-sized components on.

At that point, I left the “how to solder” thought for Future Me and focused on **collecting parts**.

Went to **LCSC**, started sourcing by footprint, one by one:  
✅ Check footprint  
✅ Check resistance  
✅ Check temperature rating  
✅ Check if thick or thin film

It was **one of the most boring, soul-draining things ever.**

It **took the whole day** just to make the BOM, checking every single component while my sanity slowly evaporated.

Worst part? **My IMU sensors and gyro chips were out of stock on LCSC.**

Checked AliExpress:
- Only breakout boards, not the raw SMD chips.
- If there were raw SMD chips, there were like 16-20 in stock, and I *do not trust that*.

By the end, I was **totally cooked**, but at least:

✅ **BOM completed.**  
✅ Sanity not completed.

--- ~ 9 hours

*Future note: BOM sourcing is the part no YouTube video warns you about while building your lunar cave explorer bot.*

<img width="1085" height="549" alt="Screenshot 2025-07-23 185502" src="https://github.com/user-attachments/assets/4f77693b-eab9-45bc-9454-e9aa1a51742b" />
<img width="1550" height="770" alt="Screenshot 2025-07-23 185531" src="https://github.com/user-attachments/assets/d8650077-7e66-45ef-b6d8-e74a49006e28" />
<img width="711" height="354" alt="Screenshot 2025-07-23 185752" src="https://github.com/user-attachments/assets/dcfdb3c6-5cab-4c1c-ac5b-e361a64d5e44" />

## Day 6 – Minor Tweaks, Major Relief (10 JULY 2025)

Today was **revision day**.

Held a quick **review session for my flight controller design** (basically me staring at EasyEDA, mumbling “please work”).

Did some **minor changes**:
- Tweaked a few traces
- Adjusted footprints
- Fixed silkscreen labels

And guess what? **My flight controller was ready to deploy.**

**Yeah.**

After days of chaotic sourcing, footprint checking, and schematic drawing, seeing it *ready to go* was a *tiny dopamine hit* I needed.~ 2 hours


## Day 7 – Back from Motivation Blackhole (13 JULY 2025)

Took **2 more days off** because I lost motivation and *almost forgot about this project*.

(Blame goes to seeing **Hackclub doing GitHubHQ**, which made me want to drop everything and watch them instead. Couldn’t join, it ended, so... back to my lunar bot.)

---

Today, I started thinking about **physical deployment**:

🪐 **Mission:**  
- How will it get to the **lunar cave?**  
- How will it *work once there?*

---

### The Plan I Cooked:

✅ I’ll place **two battery bases near the cave’s edge**.  
✅ They will be **interconnected with a rope** under tension strong enough to hold a **winch system**.  
✅ The **winch system** will lower and position the **main robot** over the cave entrance.

The **main robot** will:
- Carry the **flight controller, Raspberry Pi, and sensors**.
- Hang weightlessly, stabilized by tension, using **servos for positioning**.
- Function like a **weightless, handless drone** on a wire.

--- ~ 3 hours

Problem: I don’t know how to make it work **autonomously**, because it’s neither a rover nor a drone, just a weird *cable drone* run by **servos and wires**.

[ Battery Base A ]              [ Battery Base B ]
        |                               |
        |                               |
        +----------- Rope -------------+
                       |
                 [ Winch System ]
                       |
              [ Main Robot Payload ]
               (Flight Controller,
                Raspberry Pi,
                Sensors, Cameras)
                       ↓
          Cave Entrance for Deployment

## Day 8 (24/07/2025)

Took a long break before starting again.

Came up with the following **detailed rope-deployed lunar cave explorer architecture**:

```
[ Rover ]
   |-- Heavy-load Servo (drops battery spike base)
   |-- Rope Tensioning Mechanism
   |-- Servo for rope bend/tension adjust
   |-- LoRa Antenna → Mars Orbiter
   |-- Receives compressed video from Pi over tether/wireless

[ Rope (Tether) ]
   |-- PoE cable from Battery Base to Rope Center
   |-- Physical rope for tension + winch

[ Battery Spike Base ]
   |-- Power for system via PoE
   |-- Spike anchors on lunar cave floor

[ Rope Center Module ]
   |-- Raspberry Pi (3D mapping, image processing, compression)
        |-- MAVLink with Flight Controller
        |-- Controls Winch Servo
        |-- Sends compressed video to Rover
   |-- Main Winch Servo
   |-- Power distribution (FC, 3D Depth Camera, Servos)

[ 3D Mapping Module (Suspended) ]
   |-- Flight Controller (IMU, stabilization)
        |-- Servo 1: Pan camera
        |-- Servo 2: Rope tension adjust (optional)
   |-- 3D Depth Camera (depth capture)
   |-- Power from Rope Center Module via winch cable

[ Communication Flow ]
3D camera → Flight Controller → Pi (mapping + compression) → Rover → LoRa → Mars Orbiter
```
Also sourced all components and fitted in budget. Made BOM list.
Tomorrow will be the last day of this project I hope.

~ 7 hours


