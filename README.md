## What is LinuxWallCraftEngine?
"LinuxWallCraftEngine" is a straightforward script designed for Linux users who want to spruce up their desktop background. 
Think of it as giving your computer screen a fresh coat of paint! With "LinuxWallCraftEngine," you have the power to easily set animated GIFs, cool videos, or beautiful image slideshows as your wallpaper. 
It's a fun and creative way to personalize your desktop and make it uniquely yours!

## Installation

To install and set up the Live LinuxWallCraftEngine for Linux, follow these steps:

1. Clone the repository:

 ```bash
git clone https://github.com/Gmm09x/LinuxWallCraftEngine.git
cd LinuxWallCraftEngine
sudo bash setup.sh
sudo python3 main.py -h   
```	

## Usage
```bash
python3 main.py [-h] [-t {gif,video,cache}] [-p PATH] [-w WAIT_TIME] [-o {xfce,i3wm,kde}]
```

## Set Video Wallpaper
```bash
python3 main.py -t video -p /path/to/your/video.mp4
```

## Set Image Sequence Wallpaper
```bash
python3 main.py -t cache -p /path/to/your/image/sequence/directory
```

## Set Wallpaper for Specific Desktop Environment
```bash
python3 main.py -t gif -p /path/to/your/animated.gif -o xfce
```

## Important Notes
* Paths must be absolute, for example: /home/username/Pictures/wallpaper.gif, not ./wallpaper.gif.
* Make sure you have the necessary dependencies installed (Python 3, FFmpeg, ImageMagick).
* Performance may vary depending on the desktop environment and system configuration.


### Feel free to customize or expand this section further to provide more detailed instructions or examples as needed.
