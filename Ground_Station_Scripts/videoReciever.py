import subprocess

# ip = "172.20.10.4" #hotspot 
ip = "192.168.1.167" #lab wifi

command = f"ffplay tcp://{ip}:2200 -vf \"setpts=N/30\" -fflags nobuffer -flags low_delay -framedrop"

p1 = subprocess.run(command, shell=True, check=True)
