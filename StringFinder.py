
import os

from functools import partial

filename = 'F:\Installers\VBox.exe'  # this is just my test thing. it's just the virtual box installer
# filename = input('enter file path: ')
byteList = []
if os.path.exists() and os.path.isfile():
    with open(filename, 'rb') as file:
        for byte in iter(partial(file.read, 1), b''):
            byteList.append(byte)
            # todo: actually do something here.
            # The plan is to have it compare it to a list of words and technical strings (so file paths, names, compile paths, etc)
else:
    print("invalid file path. try again.")