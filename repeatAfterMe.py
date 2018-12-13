import time
import sys
import os
from time import sleep

print "\n\nRepeat After Me"

repeatAfterMe = raw_input("\n\tType something...")




def autoType():
   words = "\n\t\t %s \t\t " % repeatAfterMe
   for char in words:
       sleep(0.1)
       sys.stdout.write(char)
       sys.stdout.flush()

autoType()

print "\n\nRepeat After Me"