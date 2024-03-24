import os
import sys
import time
import subprocess
import shutil

# Function to set the wallpaper using feh
def setWallpaper(path):
    print("Setting wallpaper to " + path)
    if os.path.exists(path):
        # Use feh to set the wallpaper and fill the screen
        subprocess.Popen(["feh", "--bg-fill", path])
    else:
        print("ERROR: File not found")

# Command-line arguments: path to image sequence and wait time
path = sys.argv[1]  # Path to the directory containing image sequence
wait_time = float(sys.argv[2])  # Time interval between changing wallpapers

# Retrieve list of image files in the specified directory
sequence_files = next(os.walk(path), (None, None, []))[2]

# Display information about the image sequence
print("[+] Listing frames in " + path)
print("[+] Running image sequence from: " + path)
print("[+] Frames:\n" + str(sequence_files) + "\nTotal: " + str(len(sequence_files)))
print("[+] Animating")

# Loop to set each image as wallpaper with specified time interval
while True:
    time.sleep(wait_time)
    for i in range(len(sequence_files)):
        setWallpaper(path + "/frame-" + str(i) + ".png")
        time.sleep(wait_time)
