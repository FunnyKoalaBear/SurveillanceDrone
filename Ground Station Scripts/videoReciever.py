import subprocess

command = f"ffplay tcp://192.168.137.146:2200 -vf \"setpts=N/30\" -fflags nobuffer -flags low_delay -framedrop"

p1 = subprocess.run(command, shell=True, check=True)
