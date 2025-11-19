import subprocess

command = f"rpicam-vid -t 0 --width 1200 --height 720 --framerate 30 --inline --listen -o tcp://0.0.0.0:2200"

p1 = subprocess.run(command, shell=True, check=True)
