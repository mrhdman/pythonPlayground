import time
import sys
import os
from time import sleep

def autoType():
   words = "Check this out."
   for char in words:
       sleep(1)
       sys.stdout.write(char)
       sys.stdout.flush()

autoType()