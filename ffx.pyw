"""A python script to convert Final Fantasy X HD saves across platforms.

DISCLAIMER: Use this script at your own risk!

For compatibility, see: https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter#compatibility

For known issues, see: https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter#known-issues

For instructions on extracting a save file to use as an input, see: https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter#extract-a-decrypted-version-of-your-save-file

Resources used:
  - https://gbatemp.net/threads/convert-ff10-pc-ps3-ps4-psv-save-to-ns.535866/
  - https://steamcommunity.com/sharedfiles/filedetails/?id=685884099
  - https://steamcommunity.com/sharedfiles/filedetails/?id=683458202
  - https://steamcommunity.com/sharedfiles/filedetails/?id=695869704
"""

import binascii
import os
import sys
from Modules.checksum import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# The Switch save file allegedly uses some kind of 8-byte timestamp at the
# beginning of the save file. I couldn't find much concrete info about it,
# but according to the forum posts using this value appears to work. Perhaps
# a better alternative would be to also accept an existing FFX save file
# extracted from a target nintendo switch in order to reuse the exact 8
# bytes generated from the header file for a legit save.
SWITCH_PREFIX_BYTES = bytearray.fromhex('08 00 00 00 01 00 01 02')

SWITCH_SUFFIX_BYTES = bytearray.fromhex('00 00 00 00 00 00 00 00')

PS3_FILENAME = 'SAVES'
SWITCH_FILENAME = 'ffx_XXX'
STEAM_FILENAME = 'ffx_XXX'


def createRow(root, label, options):
  """Creates a new row.

  Params:
      root: The root Tkinter object to add the row to.
      label: The text label to display on the left-side of the row.
      Options: A list of strings for each option for the OptionMenu on the right-hand side.
  """
  row = Frame(root)
  row.pack(side = TOP, fill = X, padx = 10 , pady = 10)
  createLabelInRow(row, label)
  selection = createOptionMenuInRow(row, *options)
  return selection


def createLabelInRow(row, text):
  """Creates a new left-aligned label in a row.

  params:
      row: The tkinter root object for the row.
      text: The string of text to use as the label.
  """
  label = Label(row, width=12, text=text+": ", anchor='w')
  label.pack(side = LEFT)


def createOptionMenuInRow(row, *options):
  """Creates a new right-aligned `OptionMenu` in a row.

  params:
      row: The tkinter root object for the row.
      options: A list of string options to include in the OptionMenu.
               The first is assumed to be the default.
  """
  if len(options) <= 0:
    return
  value = StringVar(row)
  value.set(options[0])  # Default value
  option_menu = OptionMenu(row, value, *options)
  option_menu.pack(side = RIGHT, expand = YES, fill = X)
  return value


def isEncrypted(file_contents):
  """Returns a boolean indicating whether the file is encrypted or not.

  Checks the last 8 bytes to ensure they are all 0x00. Anything else is
  assumed to be encrypted (which may have false positives, but should be
  rare).

  NOTE: This is a very crude approximation, but should work well enough
  for the FFX save files.
  """
  for i in range(1, 9):
    i = i * -1;
    if chr(file_contents[i]) != '\x00':
      return True
  return False


def write_bytes_to_file(file_bytes, path, filename):
  """Writes a `bytearray` to the file at `path/filename`"""
  absolute_path = os.path.join(path, filename)
  print(absolute_path)
  with open(absolute_path, mode='wb') as file:
    file.write(file_bytes)


def convert_bytes_from_switch(file_bytes):
  # Trim the first 8 bytes.
  file_bytes = file_bytes[8:]
  # Append the Switch suffix.
  file_bytes = file_bytes + SWITCH_SUFFIX_BYTES
  return file_bytes


def convert_save_file(game_option, save_type_option, target_console_option):
  source = save_type_option.get()
  target = target_console_option.get()
  if target in source:
    messagebox.showerror(title='Selection Error',
                         message='Save file type and target console cannot be the same.')
    return

  filename = filedialog.askopenfilename(title='Open a file', initialdir='/')
  if not filename:
    return

  with open(filename, mode='rb') as file:
    file_content = file.read()
    if isEncrypted(file_content):
      answer = messagebox.askyesno(title='Encryption Error',
                                   message='The file appears to be encrypted. Attempting the conversion may result in a corrupted save.\n\nDo you want to continue anyway?\n\nVisit https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter for more details.')
      if not answer:
        return

    path = os.path.dirname(os.path.abspath(filename))
    file_bytes = bytearray(file_content)

    # If the file is a Switch save, convert it to the more standard
    # format first (the format shared by PC, PS3, PS4, PS Vita).
    if 'Nintendo Switch' in source:
      file_bytes = convert_bytes_from_switch(file_bytes)

    if 'Nintendo Switch' in target:
      # Append the 8 byte prefix
      file_bytes = SWITCH_PREFIX_BYTES + file_bytes

      # Remove the trailing 8 bytes to keep the file size the same. (These are all 0x00 anyway.)
      file_bytes = file_bytes[:-8]

      target_filename = SWITCH_FILENAME
      title='Nintendo Switch Save'
      message=("Your save is now ready!\n\nPost-work:\n\n1. Rename it from 'ffx_XXX' by "
               "replacing the 'XXX' with a number from 000-999 that doesn't collide with "
               "an existing save slot. For example: 'ffx_001' would correspond to the "
               "second save slot.\n\n2. Use Checkpoint to restore the save.\n\n3. Load "
               "the save file on your switch (it may look weird, but this is "
               "normal).\n\n4. Use an in-game save point to save the current game. This "
               "will fix any weirdness.\n\nFor more details, view the guide on "
               "https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter")
    elif 'PS3' in target:
      target_filename = PS3_FILENAME
      title='PS3 (decrypted) Save'
      message=("Your save is now ready!\n\nPost-work:\n\n1. Use a tool such as 'Bruteforce Sava Data' "
               "to encrypt the SAVES file.\n\n2. Use a USB flashdrive to copy the encrypted PS3 folder "
               "back to the device.\n\n3. Load the save file on your PS3 (it may look weird, but "
               "this is normal).\n\n4. Use an in-game save point to save the current game. This "
               "will fix any weirdness.\n\nFor more details, view the guide on "
               "https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter")
    elif 'Steam' in target:
      target_filename = PC_FILENAME
      title='Steam Save'
      message=("Your save is now ready!\n\nPost-work:\n\n1. Rename it from 'ffx_XXX' by "
               "replacing the 'XXX' with a number from 000-999 that doesn't collide with "
               "an existing save slot. For example: 'ffx_001' would correspond to the "
               "second save slot.\n\n2. Copy the renamed save file to the appropriate "
               "saved data location for your Steam device "
               "(https://www.pcgamingwiki.com/wiki/Final_Fantasy_X/X-2_HD_Remaster#Save_game_data_location)."
               "\n\n3. Load the save file on your PC (it may look weird, but this is "
               "normal).\n\n4. Use an in-game save point to save the current game. This "
               "will fix any weirdness.\n\nFor more details, view the guide on "
               "https://github.com/mrhappyasthma/Final-Fantasy-X-HD-Cross-platform-Save-Converter")

    update_checksum(file_bytes, Game.FFX)
    write_bytes_to_file(file_bytes, path, target_filename)
    messagebox.showinfo(title=title, message=message)


if __name__ == '__main__':
  if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

  tk = Tk()
  tk.title("FFX Save Converter")
  tk.resizable(False, False)
  tk.geometry("305x200")

  game = createRow(tk, label="Game", options=["Final Fantasy X"])

  save_type = createRow(tk, label="Save File Type",
                        options=["Steam (PC, Linux, Mac)", "(decrypted) PS3", "(decrypted) PS4",  "(decrypted) PS Vita", "Nintendo Switch"])

  target_console = createRow(tk, label="Target Console",
                             options=["Nintendo Switch", "PS3 (decrypted)", "Steam (PC, Linux, Mac)"])

  open_button = Button(tk, text='Convert save file', command=lambda:convert_save_file(game, save_type, target_console))
  open_button.pack(expand=True, pady = 5)

  answer = messagebox.askyesno(title='Disclaimer',
                               message=('WARNING: Use this tool at your own risk. I take no responsibility for lost '
                                        'save files, corrupted saves, bricked consoles, etc.\n\nDo you still want to '
                                        'continue to the tool?'))

  if not answer:
    quit();

  mainloop()
