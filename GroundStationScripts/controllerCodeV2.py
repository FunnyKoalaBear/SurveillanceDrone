#libraries for wireless communication
import socket
import time
import json

#controller input libraries 
import pygame
import time

#setting up connection 
HOST = '192.168.1.168' #modify with rasberry pi ip 
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#setting up controller 
pygame.init()
pygame.joystick.init()

# --- MAPPING CONFIG (You may need to tweak these for your specific controller) ---
# Xbox/PS4 Standard: 0=LeftX, 1=LeftY, 2=RightX, 3=RightY
AXIS_ROLL = 2  # Right Stick X
AXIS_PITCH = 3 # Right Stick Y
AXIS_YAW = 0   # Left Stick X
AXIS_THROTTLE = 1 # Left Stick Y

#checking for controller connection
if pygame.joystick.get_count() == 0:
    print("No controller detected!")
    exit()


joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected to: {joystick.get_name()}")

print("WARNING: PROPS SHOULD BE OFF.")
print("Move sticks to send commands. Press Ctrl+C to stop.\n")


try: 
    while True:
        pygame.event.pump()

        #Getting joystick raw values by id for roll, pitch, yaw, throttle
        #Values recieve by pygame range -1.0 -> 1.0

        #Pixhawk needs values -1000 to 1000 so we process raw values (left joystick)
        val_roll = int(joystick.get_axis(AXIS_ROLL) * 1000)

        #right joy stick, axis 3 & 4. 
        val_pitch = int(joystick.get_axis(AXIS_PITCH) * 1000 * -1) #up becomes positive, down becomes negative  
        val_yaw = int(joystick.get_axis(AXIS_YAW) * 1000)

        #Throttle is -1 at max, 1 at min. We need to process it
        #0 is min 1000 is max
        val_throttle = joystick.get_axis(AXIS_THROTTLE)
        val_throttle = int((val_throttle*-1 + 1) * 500)

        #creating a json data packet
        dataPacket = {
            "r": val_roll,
            "t": val_throttle,
            "p": val_pitch,
            "y": val_yaw
        }

        #sending the data 
        msg = json.dumps(dataPacket)
        s.sendall(msg.encode('utf-8'))


        # # Buttons on right
        # for i in range(joystick.get_numbuttons()):
            
        #     state = joystick.get_button(i)

        #     if state != prev_buttons[i]:
        #         print(f"Button {i}: {'Pressed' if state else 'Released'}")
        #         prev_buttons[i] = state

        #         output = f"button{i}:{state}\n"
        #         s.sendall(output.encode())

        # # D-Pad (Buttons on left)
        # for i in range(joystick.get_numhats()):

        #     hat = joystick.get_hat(i)

        #     if hat != prev_hats[i]:
        #         print(f"Hat {i}: {hat}")
        #         prev_hats[i] = hat

        #         output = f"hat{i}:{hat[0]},{hat[1]}\n"
        #         s.sendall(output.encode())
                
        time.sleep(0.02)

except KeyboardInterrupt:
    print("Closing connection.")
    s.close()

