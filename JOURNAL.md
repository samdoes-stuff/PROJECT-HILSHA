

## Day 1 – Flight Controller (28 JULY 2025)

Dual gyro-redundancy flight controllers?  
Thought to buy one very expensive even the second hand Pixhawk 2.4.8 is too out of my reach

Then I had the Idea to clone one
Dived into ArduPilot’s site for mission planning compatible   
Found an open-source controller with:

✅ ArduPilot compatibility  
✅ Dual gyro  
✅ Open schematics  
✅ 3D files  


Though I found the same one from third-party retailers from Banggood but selling them for $75 instead of $200

**Bad news:** It’s discontinued, but hey, still supported for normal Pixhawk versions.

Sadly, Pixhawk normal versions are big chonks, not fitting my tiny lunar bot dreams.  
Also, they don’t give me a esp8266 wifi module support for easy log transfers.  
That’s why I decided to clone it


https://ardupilot.org/copter/docs/common-pixracer-overview.html

~ 3 hours


## Day 2 (29 JULY 2025)

I found out the schematic linked in the repo wasn’t even for the exact pixracer I’m trying to clone.  
Apparently, there are so many pixracer version

- Pixhawk version  
- Holybro version  
- [Insert another vendor here] version



I roamed around GitHub repo  until I found the exact schematics and design files.

Bad news: All of it was in Altium Designer, which is hella expensive and doesn’t give student packages for high school students.  


I decided to redraw the schematics in EasyEDA for my understanding and rebuild it from scratch.  
Oh, and some schematics were missing. 


 ~ 1 hours

https://firmware.ardupilot.org/Rover/

https://drive.google.com/file/d/13R---X2ncpKuxhJewDeZoGOMFhPUqMNB/view?usp=drive_link


## Day 4 –  (30 July 2025)

 The day started with a goal for making a BOM file 

Main concern
-  footprints
- How do I make it look exactly the same as the reference?

When I redrew the schematic in EasyEDA, Now I have to make a pcb

The open-source hardware repo had a PCB in some random files that I never saw later found out that was Altium files but Altium was paid software. It is not free even for high schooler . Though I couldn’t find a clean PCB export, found schematics.

Went back to repo I found out there was several upgrades but they do not mention the whole files only mentions the upgraded file

Turns out you can download the file separately through altium 365 which is free lucky for me

So I did exactly that. 

After making the pcb I designed a case for the flight controller 

~ 4 hours

https://365.altium.com/files/DE5E7958-BE7D-470E-812E-0988A14BB30F
<img width="1473" height="784" alt="Screenshot 2025-07-31 234317" src="https://github.com/user-attachments/assets/05de6197-fe0a-435c-9cd2-e83ee929407b" />
<img width="1586" height="850" alt="Screenshot 2025-07-31 234256" src="https://github.com/user-attachments/assets/1161bf86-d2a0-4e27-87ff-e7aa20f18b65" />



## Day 5 – ( 31 July 2025)


Making the BOM should’ve been chill but footprints killed me I have look through again and again had to use the lcsc filter properly.

I suddenly realized I do not have a hot air gun but I am dealing with smd components\. I have to buy one when I checked it is almost half of my flight controller price what turned out later.



Went to LCSC, started sourcing by footprint, one by one:  
✅ Check footprint  
✅ Check resistance  
✅ Check temperature rating  
✅ Check if thick or thin film

Boring

I wasted a just to make the BOM.

Worst part? The original IMU sensors and gyro chips were out of stock and discontinued on LCSC.

Checked AliExpress:
- Only breakout boards, not the raw SMD chips.
- If there were raw SMD chips, there were like 16-20 in stock, and I do not trust that.

Then I have to did a upgrade and see the compatibility luckily I found some chips that were new and pin out alternative meaning it will not have any problem with mission planner firmware.

By the end, I was successful and tired but at least:

✅ BOM completed.


--- ~ 9 hours

Future note: BOM sourcing is the part no YouTube video warns you about while building your project.

<img width="1085" height="549" alt="Screenshot 2025-07-23 185502" src="https://github.com/user-attachments/assets/4f77693b-eab9-45bc-9454-e9aa1a51742b" />
<img width="1550" height="770" alt="Screenshot 2025-07-23 185531" src="https://github.com/user-attachments/assets/d8650077-7e66-45ef-b6d8-e74a49006e28" />
<img width="711" height="354" alt="Screenshot 2025-07-23 185752" src="https://github.com/user-attachments/assets/dcfdb3c6-5cab-4c1c-ac5b-e361a64d5e44" />

## Day 6 –  (1 August 2025)

Today was revision day.

Did a quick review for my flight controller design (basically me staring at EasyEDA).
