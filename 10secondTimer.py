import time
import os
from time import sleep



os.system("clear")
print "\n\t\t\t\t10 second timer."

start = raw_input("\n\nPress enter to start.\n\n")

if start == "":
    i = 10
    numbers = []

    while i > 0:
        print "\t%d" % i
        time.sleep(1.0)
        numbers.append(i)
        i = i - 1

        if i == 0:
            print "\n\t\t\t\t  Time is up."
