#  figure out how turning a python script
# into a full on bash command works with
# switches and such, using argv?

from os import chdir
from os import system
import glob

folder = input("Enter folder of playlist from root")
files = glob.glob(f"{folder}/*")
for file in files:
    print(file)
    system("afplay file")
