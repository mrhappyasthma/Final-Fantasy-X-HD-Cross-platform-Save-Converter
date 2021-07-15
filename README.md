# Final Fantasy X HD - Cross-platform Save Converter

<img src="https://i.ytimg.com/vi/myDYi0I-cgQ/maxresdefault.jpg" width="480" height="270">

## How To Use

A helper tool to convert FFX saves between PS3/PS4/PSVita/Steam/Nintendo Switch/Xbox One.

*The tool assumes you already have your existing FFX save file (decrypted, if needed) on your computer. For instructions, see [Extract a Decrypted Version of Your Save File](#extract-a-decrypted-version-of-your-save-file).*

Simply run the tool, select the `Save File Type` for the input save as well as the `Target Console`. Then simply press `Convert save file` and select your existing (decrypted) save.

Lastly, follow the on-screen instructions for the post-work. Or continue reading below.

![Screenshot of the tool.](https://i.imgur.com/9gtNHnV.png)

## Compatibility

Below is the compatibility chart going to/from the Nintendo Switch.

### FFX

#### Supported 

Aside from Xbox, I believe all of the others should be doable just based on my research. I could not find anyone attempting this with Xbox.

This is the list of implemented save conversions, so far.


| Supported | Nintendo Switch | Steam | PS3 | PS4 |  PS Vita | Xbox One |
|-----------|-----------------|-------|-----|-----|----------|----------|
| Xbox One | NO | NO | NO | NO | NO | - |
| PS Vita | NO | NO | NO | NO | - | NO |
| PS4 | NO | NO | NO | - | NO | NO |
| PS3 | YES | YES | - | NO | NO | NO |
| Steam | YES | - | YES | NO | NO | NO |
| Nintendo Switch | - | YES | YES | NO | NO | NO |

#### Verified

'Verified' means that I tried going to/from the console to confirm it worked.

| Supported | Nintendo Switch | Steam | PS3 | PS4 |  PS Vita | Xbox One |
|-----------|-----------------|-------|-----|-----|----------|----------|
| Xbox One | NO | NO | NO | NO | NO | - |
| PS Vita | NO | NO | NO | NO | - | NO |
| PS4 | NO | NO | NO | - | NO | NO |
| PS3 | NO | NO | - | NO | NO | NO |
| Steam | NO | - | NO | NO | NO | NO |
| Nintendo Switch | - | NO | NO | NO | NO | NO |

### FFX-2

This 'should' be implementable. But I don't have saves to test it. This is a stretch goal for me.

## Known issues

1. The main character name will be reset to Tidus.

2. After the save is ported to the new platform, the 'time played' and 'party members' that are previewed in the Load Game menu will be wrong.

   This should fix itself if you save to another slot or save overtop of this save after loading it.
   
   Here is an example of a save ported to Nintedo Switch from PS3.
   
   ![Example of a messed up save in slot 2](https://i.imgur.com/RAIDEEP.jpg)
   
   The save file should still launch fine. The next time you save, it should correct itself.
   
   Here is an example where I launched that save and saved it as slot 3:
   
   ![Example of re-saving the file in slot3](https://i.imgur.com/oB4jPmR.jpg)
   
   And here's an example where I launched the save and overwrite the same save to correct it:
   
   ![Example of overwriting the save file in slot2](https://i.imgur.com/z6TYrtP.jpg)

## Extract a decrypted version of your save file

Playstation consoles encrypt their save files, so there steps here are a bit more involved. PC and Nintendo Switch do not.

### Extract your save file from PS3

1. Copy your save file from your PS3 to a USB drive. And then copy it onto you computer.

Then you need to get your User ID and Console ID. ([Video tutorial](https://www.youtube.com/watch?v=mMZxlTrpCaM), from some youtuber. My text instructions are also below.)

2. Install ps3tools on to your PC. Run the application. It will show a list of blue squares for each available tool. Click the one for `PARAM SFO Editor`.

3. Click the 'folder' icon and navigate to your PS3 `PARAM.SFO` file that you copied in `step 1`. (For me, the relative path was `PS3/SAVEDTA/BLUS31211SAVEDIR---------------/PARAM.SFO`).

4. On the left, under 'Account ID', there should be a drop-down menue that defaults to the `TITLE` option. Use the drop-down to select `PARAMS:UserID1`. Then write down (or copy/paste) the value. For me it was `00000002`, but it will vary for each person based on their PS3.

5. Then, using that same drop-down, select `PARAMS:PSID`. Then write down (or copy/paste) the value. For me it was `26DCD31037E0450A5B78467E1C1CB34F`, but this will vary for each PS3.

Now we are done with this application. You can close it (or even uninstall it if you don't plan to do this process again in the future. So long as you recorded those two values from your save file).

6. Next you need to download and install [Bruteforce Save Data](https://mega.nz/file/2hFEmYBR#k5Xi1c0xhBnVJ9SLN1QpnNmzrK15hjRRmpB5eT8uKFg).

7. Install `Msvbvm50.exe` and then install `Bruteforce_Save_Data_installer.exe`.

8. Launch `Bruteforce Save Data` application.

9. You can close out of any pop-ups about updating the software or anything else. Just get to the main page.

10. Right-click on the main window and go to `Settings > Global Settings`. This will open a configuration file window. Set the `User ID` and `Console ID` fields to the values we extracted in step 3 and step 4.

11. Click 'Close'. If it asks you to navigate to an `SFO` file, the navigate to the same one from step 2.

12. Set the `Path for SAVEDATA folders:` at the top of the main window to the SAVEDATA folder that you copied from your PS3. (You can use the `...` overflow option to use windows explorer to navigate to the folder, if you prefer that to typing out the path manually.

13. It should find your `FFX` save. Right click on the icon for the save and click `Decrypt all files`. If it asks you to confirm, click 'YES'.

14. To verify that it worked, the UI should turn Green in the bottom-left corner. Also navigate using Windows Explorer to your PS3 file path and see if it contains a file named `~files_decrypted_by_pfdtool.txt`.

15. Assuming all of this worked. You can now use the file named `SAVES` as the input to the program.

You're now done with this software. You can close it or even uninstall it, if you do not anticipate needing to do these steps again.

### Extract your save file from PS4

TODO: I don't have this game to verify. But my understanding is that similar decryption steps for the PS3 can be performed. Give that a try.

### Extract your save file from PS Vita

NOTE: This requires Custom Firmware (CFW) running on the Vita. Installing it on the Vita is outside the scope of this project. See [vita.hacks.guide](https://vita.hacks.guide/) for more info.

1. Install the [vita-savemgr](https://github.com/d3m3vilurr/vita-savemgr/releases) using `Vita Shell`.

2. Use the save manager to backup a decrypted version of your save file.

3. Using FTP (from `Vita Shell`) or by plugging your console in to your computer using USB, copy the save file to your PC.

4. This save file can be used as the input to the program, since it's already decrypted.

### Extract your save file from Nintendo Switch

NOTE: If you are using a Nintendo Switch as your source or destination for your save file, you'll need to have a Switch running Custom Firmware (CFW).

Getting CFW on your Switch is outside the scope of this project. For more details, see [switch.homebrew.guide](https://switch.homebrew.guide/) for more info.

1. Launch FFX and get far enough in the story to make a save file. (If you don't already have one.)

2. Install [Checkpoint](https://github.com/FlagBrew/Checkpoint/releases) by downloading the latest `.nro` and putting it on your SD card in the `/switch` subdirectory.

3. Run `Checkpoint` and backup your FFX save.

4. Using FTP (such as [ftpd](https://github.com/mtheall/ftpd)) or by plugging your SD card into your computer, copy your save backup to your PC.

5. You will use the corresponding `ffx_ZZZ` file as the input for the software, where `ZZZ` is going to be the numbers from `001-999`. (The numbers correspond to the save slot location.)

6. Use these save file(s) as the inputs to the program.

### Extract your save file from a machine with Steam

1. Locate your FFX [save location](https://www.pcgamingwiki.com/wiki/Final_Fantasy_X/X-2_HD_Remaster#Save_game_data_location) for PC.

2. Take note of the file path to your `ffx_ZZZ` file, where `ZZZ` is the save location number from `001-999`.

3. Use these save file(s) as the inputs to the program.

### Extract your save file from Xbox One

TODO: No idea on this one. I don't have this game to see if it's encrypted or not. And what format the save is in.

## Copying the new save file to the target console

### Copy the modified file to Nintendo Switch

NOTE: If you are using a Nintendo Switch as your source or destination for your save file, you'll need to have a Switch running Custom Firmware (CFW).

Getting CFW on your Switch is outside the scope of this project. For more details, see [switch.homebrew.guide](https://switch.homebrew.guide/) for more info.

1. Launch FFX and get far enough in the story to make a save file. (If you don't already have one.)

2. Install [Checkpoint](https://github.com/FlagBrew/Checkpoint/releases) by downloading the latest `.nro` and putting it on your SD card in the `/switch` subdirectory.

3. If you haven't already created a Checkpoint backup, create one of the dummy save file from `step 1`.

4. Use FTP (such as [ftpd](https://github.com/mtheall/ftpd)) or by plugging your SD card into your computer, copy the save file to the `Checkpoint` subfolder for FFX. (For me, it was `/switch/Checkpoint/saves/0x0100BC300CB48000%20FINAL%20FANTASY%20X%20X-2%20HD%20Remaster/<folder_name_from_step_2>`).

5. Run `Checkpoint` and restore the save for FFX.

### Encrypt and copy the save file to PS3

TODO

### Encrypt and copy the save file to PS4

TODO: I don't have this game to verify. But my understanding is that similar decryption steps for the PS3 can be performed. Give that a try.

### Encrypt and copy your save file to PS Vita

TODO

6. Launch FFX and enjoy :)

### Copy the save file to a computer with Steam

1. Locate your FFX [save location](https://www.pcgamingwiki.com/wiki/Final_Fantasy_X/X-2_HD_Remaster#Save_game_data_location) for PC.

2. Rename the generated save file in the format `ffx_ZZZ` file, where `ZZZ` is the save location number from `001-999`.

3. Copy this file to the save file location from step 0.

4. Launch FFX and enjoy :)

### Extract your save file to Xbox One

TODO: No idea on this one. I don't have this game to see if it's encrypted or not. And what format the save is in.
