from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys
import binascii


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


def convert_save_file(game_option, save_type_option, target_console_option):
  if save_type_option.get() == target_console_option.get():
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


if __name__ == '__main__':
  if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

  tk = Tk()
  tk.title("FFX Save Converter")
  tk.resizable(False, False)

  game = createRow(tk, label="Game", options=["Final Fantasy X"])

  save_type = createRow(tk, label="Save File Type", options=["PC (Steam)", "Nintendo Switch"])

  target_console = createRow(tk, label="Target Console", options=["Nintendo Switch", "PC (Steam)"])

  open_button = Button(tk, text='Convert save file', command=lambda:convert_save_file(game, save_type, target_console))
  open_button.pack(expand=True, pady = 10)

  mainloop()