import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path

# Text formatting for better presentation
formatting = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}

def welcome_print():
    print("")
    print(formatting["BOLD"] + "Live wallpaper Engine for Linux")
    print(formatting["FAIL"] + "by Gmm09x")
    print(formatting["ENDC"] + "usage: main.py [-h] [-t {gif,video,cache}] [-p PATH] [-w WAIT_TIME] [-o {xfce,i3wm,kde}] [-b]")
    print("Options:")
    print("  -h, --help            show this help message and exit")
    print("  -t {gif,video,cache}, --type {gif,video,cache}")
    print("                        Type of wallpaper (gif, video, cache)")
    print("  -p PATH, --path PATH  Path to the file or directory containing the wallpaper")
    print("  -w WAIT_TIME, --wait-time WAIT_TIME")
    print("                        Wait time between frames for image sequence wallpapers (default is 0.05s)")
    print("  -o {xfce,i3wm,kde}, --os {xfce,i3wm,kde}")
    print("                        Target operating system (XFCE, i3wm, KDE)")
    print("  -b, --background      Run wallpaper operations in the background")
    print(formatting["WARNING"] + "IMPORTANT NOTE: path must be global, Example: /home/you/Videos/video.mp4 NOT: ./video.mp4. Make sure you have imagemagik installed")
    print(formatting["ENDC"])

def clear_cache():
    print("Clearing cache...")
    shutil.rmtree('./src/cache', ignore_errors=True)
    os.mkdir("./src/cache")

def run_wallpaper_from_cache(wait_time):
    os.system(f"python3 {Path(__file__).parent}/src/modules/wallpaper.py {Path(__file__).parent}/src/cache {wait_time}")

def check_root():
    if os.geteuid() != 0:
        print(formatting["FAIL"] + "This script must be run with root privileges (sudo).")
        sys.exit(1)

def main():
    if len(sys.argv) == 1 or sys.argv[1] in ["-h", "--help"]:
        welcome_print()
        return

    check_root()

    parser = argparse.ArgumentParser(description="Script for managing wallpapers.")
    parser.add_argument("-t", "--type", choices=["gif", "video", "cache"], default="gif", help="Type of wallpaper (gif, video, cache)")
    parser.add_argument("-p", "--path", help="Path to the file or directory containing the wallpaper")
    parser.add_argument("-w", "--wait-time", type=float, default=0.05, help="Wait time between frames for image sequence wallpapers (default is 0.05s)")
    parser.add_argument("-o", "--os", choices=["xfce", "i3wm", "kde"], default="xfce", help="Target operating system (XFCE, i3wm, KDE)")
    parser.add_argument("-b", "--background", action="store_true", help="Run wallpaper operations in the background")
    args = parser.parse_args()

    wallpaper_type = args.type
    path = args.path
    wait_time = args.wait_time
    target_os = args.os
    background = args.background

    if wallpaper_type == "cache":
        print("Using last cached animation")
        if background:
            run_wallpaper_from_cache(wait_time)
        else:
            print("Running in foreground. Use -b or --background option to run in background.")
            run_wallpaper_from_cache(wait_time)
        return

    if not path:
        print(formatting["FAIL"] + "No path specified")
        return

    if not Path(path).exists():
        print(formatting["FAIL"] + "Path does not exist:", path)
        return

    print("Killing other wallpaper instances...")
    subprocess.Popen(["nohup", f"{Path(__file__).parent}/src/modules/kill.sh"])

    if wallpaper_type == "sequence":
        print("Animating image sequence in", path)
        if background:
            subprocess.Popen(["python3", f"{Path(__file__).parent}/src/modules/wallpaper.py", path, str(wait_time)])
        else:
            print("Running in foreground. Use -b or --background option to run in background.")
            os.system(f"python {Path(__file__).parent}/src/modules/wallpaper.py {path} {wait_time}")
    elif wallpaper_type == "gif":
        clear_cache()
        print("Converting GIF to image sequence, please wait...")
        if background:
            subprocess.Popen(["convert", path, "-coalesce", "./src/cache/frame.png"])
            run_wallpaper_from_cache(wait_time)
        else:
            print("Running in foreground. Use -b or --background option to run in background.")
            os.system(f"convert {path} -coalesce ./src/cache/frame.png")
            run_wallpaper_from_cache(wait_time)
    elif wallpaper_type == "video":
        clear_cache()
        print("Converting video file to image sequence, please wait...")
        if background:
            subprocess.Popen(["ffmpeg", "-i", path, "-vf", "fps=30", "-vf", "scale=1280:720", "./src/cache/frame-%d.png"])
            run_wallpaper_from_cache(wait_time)
        else:
            print("Running in foreground. Use -b or --background option to run in background.")
            os.system(f"ffmpeg -i {path} -vf fps=30 -vf scale=1280:720 ./src/cache/frame-%d.png")
            run_wallpaper_from_cache(wait_time)

# Execute the main function
if __name__ == "__main__":
    main()

print("\nExiting")
