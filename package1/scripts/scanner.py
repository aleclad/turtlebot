#import msvcrt
import PIL
import curses
import time
from PIL import Image
import subprocess
from skimage.viewer import ImageViewer
from skimage.io import imread
from PyQt5 import QtCore, QtGui, QtWidgets


while True:  #Dont exit program always wait for input
  # char = char = msvcrt.getch()
  print("\n\n\nPlease scan a barcode...\n\n\n")
  a = []
  for x in range(7):
    char = char = raw_input() #was msvcrt.getch()
    x = a.append(char) 

  if a == [b'1', b'2', b'3', b'4', b'5', b'6', b'7']:        #wait for the number '1' in barcode number
    p = subprocess.Popen('python imviewer.py')
    time.sleep(10)
    p.kill()
    a.clear() 
   
  else:
    print("####################\n\n\nBarcode Scan ID not registered\nPlease Scan ON Semiconductor Parts only :)\n\n\n####################")
    a.clear()
   # while getch.kbhit():       #was msvcrt.kbhit() - return boolean value if any key is being pressed
     # getch.getch()            #was msvcrt.getch()







# print ("Please scan your barcode.")
# int = msvcrt.getch()
# print (int)