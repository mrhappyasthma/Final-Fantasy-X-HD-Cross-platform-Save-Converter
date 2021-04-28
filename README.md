# FFX-HD---Save-Converter
A helper tool to convert FFX saves from PS3/PS4/PSVita/Switch/PC

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

