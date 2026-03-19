
#libraries for wireless communication
import socket
import time

#controller input libraries 
import pygame
import time

#setting up connection 
HOST = '127.0.0.1'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#setting up controller 
pygame.init()
pygame.joystick.init()



if pygame.joystick.get_count() == 0:
    print("No controller detected!")
    exit()



joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected to: {joystick.get_name()}")
print("\nMove a stick, press a button, or use D-pad.\n(Press Ctrl+C to quit)\n")



# store previous values to detect changes
prev_axes = [0] * joystick.get_numaxes()
prev_buttons = [0] * joystick.get_numbuttons()
prev_hats = [(0, 0)] * joystick.get_numhats()



while True:
    pygame.event.pump()

    # Axes
    for i in range(joystick.get_numaxes()):

        axis = joystick.get_axis(i)

        if abs(axis - prev_axes[i]) > 0.1:
            print(f"Axis {i}: {axis:.2f}")
            prev_axes[i] = axis
            
            output = f"axis{i}:{axis:.2f}\n"
            s.sendall(output.encode())

    # Buttons on right
    for i in range(joystick.get_numbuttons()):
        
        state = joystick.get_button(i)

        if state != prev_buttons[i]:
            print(f"Button {i}: {'Pressed' if state else 'Released'}")
            prev_buttons[i] = state

            output = f"button{i}:{state}\n"
            s.sendall(output.encode())

    # D-Pad (Buttons on left)
    for i in range(joystick.get_numhats()):

        hat = joystick.get_hat(i)

        if hat != prev_hats[i]:
            print(f"Hat {i}: {hat}")
            prev_hats[i] = hat

            output = f"hat{i}:{hat[0]},{hat[1]}\n"
            s.sendall(output.encode())
            
    time.sleep(0.02)


#UPGRADE THIS CODE BY SENDING DATA IN JSON FORMAT LATER 
