import os
import sys
import time

print("\n Make sure you've already install aria2 packet.")
print(" If you've installed python, just type pip install aria2p to install aria2 packet.")

magnet_link = input (" \n Paste your Magnet Link here, and hit Enter: ")

eksekusi = "aria2c -u10K " + '"' + magnet_link + '"'

print("\n")

print("STARTING.....")

time.sleep(3)

os.system(eksekusi)

time.sleep(3000)
