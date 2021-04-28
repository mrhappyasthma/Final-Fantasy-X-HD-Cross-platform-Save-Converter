# FFX-HD - Save-Converter

A helper tool to convert FFX saves from PS3/PS4/PSVita/Switch/PC.

The tool assumes you already have your existing FFX save file (decrypted, if needed) on your computer.

Simply run the tool, set the path to your source save file, and select the source/target platforms.

## Prework

### Playstation Consoles

Please read the following sub-section(s) if your source save is from your PS3, PS4, or PS Vita.

Playstation consoles encrypt their saves. If you already have a decrypted save, or know how to do this already, please skip ahead.

If not, see below for details on how to decrypt the saves.

#### Files transfered FROM PS3

0. Copy your save file from your PS3 to a USB drive. And then copy it onto you computer.

Then you need to get your User ID and Console ID. ([Video tutorial](https://www.youtube.com/watch?v=mMZxlTrpCaM), from some youtuber. My text instructions are also below.)

1. Install ps3tools on to your PC. Run the application. It will show a list of blue squares for each available tool. Click the one for `PARAM SFO Editor`.

2. Click the 'folder' icon and navigate to your PS3 `PARAM.SFO` file that you copied in step 0. (For me, the relative path was `PS3/SAVEDTA/BLUS31211SAVEDIR---------------/PARAM.SFO`).

3. On the left, under 'Account ID', there should be a drop-down menue that defaults to the `TITLE` option. Use the drop-down to select `PARAMS:UserID1`. Then write down (or copy/paste) the value. For me it was `00000002`, but it will vary for each person based on their PS3.

4. Then, using that same drop-down, select `PARAMS:PSID`. Then write down (or copy/paste) the value. For me it was `26DCD31037E0450A5B78467E1C1CB34F`, but this will vary for each PS3.

Now we are done with this application. You can close it (or even uninstall it if you don't plan to do this process again in the future. So long as you recorded those two values from your save file).

5. Next you need to download and install [Bruteforce Save Data](https://mega.nz/file/2hFEmYBR#k5Xi1c0xhBnVJ9SLN1QpnNmzrK15hjRRmpB5eT8uKFg).

6. Install `Msvbvm50.exe` and then install `Bruteforce_Save_Data_installer.exe`.

7. Launch `Bruteforce Save Data` application.

8. You can close out of any pop-ups about updating the software or anything else. Just get to the main page.

9. Right-click on the main window and go to `Settings > Global Settings`. This will open a configuration file window. Set the `User ID` and `Console ID` fields to the values we extracted in step 3 and step 4.

10. Click 'Close'. If it asks you to navigate to an `SFO` file, the navigate to the same one from step 2.

11. Set the `Path for SAVEDATA folders:` at the top of the main window to the SAVEDATA folder that you copied from your PS3. (You can use the `...` overflow option to use windows explorer to navigate to the folder, if you prefer that to typing out the path manually.

12. It should find your `FFX` save. Right click on the icon for the save and click `Decrypt all files`. If it asks you to confirm, click 'YES'.

13. To verify that it worked, the UI should turn Green in the bottom-left corner. Also navigate using Windows Explorer to your PS3 file path and see if it contains a file named `~files_decrypted_by_pfdtool.txt`.

14. Assuming all of this worked. You can now use the file named `SAVES` as the input to the program.

You're now done with this software. You can close it or even uninstall it, if you do not anticipate needing to do these steps again.

If you need to re-encrypt a save to put it back onto a PS3. The steps 5-14 can be done the same way, except this time you'll have the option for step 12 to `Encrypt all files`.

#### Files transfered FROM PS4

TODO: I don't have this game to verify. But my understanding is that similar decryption steps for the PS3 can be performed. Give that a try.

#### Files transfered FROM PS Vita

NOTE: This requires Custom Firmware (CFW) running on the Vita. Installing it on the Vita is outside the scope of this project. See [vita.hacks.guide](https://vita.hacks.guide/) for more info.

TODO

### Nintendo Switch Console

NOTE: If you are using a Nintendo Switch as your source or destination for your save file, you'll need to have a Switch running Custom Firmware (CFW).

Getting CFW on your Switch is outside the scope of this project. For more details, see [switch.homebrew.guide](https://switch.homebrew.guide/) for more info.

0a. Launch FFX and get far enough in the story to make a save file. (If you don't already have one.)

0b. Install [Checkpoint](https://github.com/FlagBrew/Checkpoint/releases) by downloading the latest `.nro` and putting it on your SD card in the `/switch` subdirectory.

1. Run `Checkpoint` and backup your FFX save.

2. Using FTP (such as [ftpd](https://github.com/mtheall/ftpd)) or by plugging your SD card into your computer, copy your save backup to your PC.

3. You will use the corresponding `ffx_ZZZ` file as the input for the software, where `ZZZ` is going to be the numbers from `001-999`. (The numbers correspond to the save slot location.)

If the Nintendo Switch is the target console, then you will take the output of the program and place it as the next `ffx_ZZZ` numerically. Or rename it to overwrite one of your existing saves.

## TODO (notes)

Convert FFX saves

PC to Switch
1. Copy save to alternate location
2. Open save in HxD
3. Paste 08 00 00 00 01 00 01 02 into first 8 bytes
4. Delete last 8 bytes (Should be all 00, to keep filesize the same)
5. Overwrite backup save in Checkpoint

Switch to PC
1. Copy save to alternate location
2. Open save in HxD
3. Delete first 8 bytes
4. Insert 00 into last 8 bytes
5. Save to PC folder
#62 Mar 23, 2020


PS3 / PS4 - decrypt saves first cybersaveeditor or savewizard

PSV - decrypt savemgr on jailbroken vita

1 download winhex
2 use winhex open two save
3 in psv save press ctrl+a and press ctrl+shift+c
4 in ns save , press alt+g , input "00000008" confirm the cursor moves to the middle position , press ctrl+b , press ctrl+s , ok


https://www.reddit.com/r/ps3homebrew/wiki/ps3_saves

https://www.youtube.com/watch?v=mMZxlTrpCaM


Copy bytes from 0x0h to 0x67ffh of a PS/PC save to the switch save starting at offset 0x8h.

Then remove the last 8 0’s from the file to ensure the file size is identical.


PS3 or PS4 or PSVita to PC

https://steamcommunity.com/sharedfiles/filedetails/?id=685884099
https://steamcommunity.com/sharedfiles/filedetails/?id=683458202

PC file format name:

ffx_XXX.dat where number from 000-999

PS3 format: SAVES (no extension)

If last 8 bytes are not all 00’s likely it’s encrypted by PS3/PS4 or Vita.

## Known issues

A.) The main character name will be reset to Tidus.

B.) After the save is ported to the new platform, the 'time played' and 'party members' that are previewed in the Load Game menu will be wrong.

This should fix itself if you save to another slot or save overtop of this save after loading it.

