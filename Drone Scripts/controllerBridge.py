import time
import os

#libraries for wireless communication
import socket
import json 

#setting up connection 
HOST = '0.0.0.0'
PORT = 1234

# Set SDL to use the dummy driver (crucial for running on Headless Pi/SSH)
os.environ["SDL_VIDEODRIVER"] = "dummy"
from pymavlink import mavutil

# --- CONFIGURATION ---
CONNECTION_STRING = '/dev/serial0'
BAUD_RATE = 921600


def connect_drone():
    print(f"Connecting to Pixhawk on {CONNECTION_STRING}...")
    master = mavutil.mavlink_connection(CONNECTION_STRING, baud=BAUD_RATE)
    master.wait_heartbeat()
    print(f"Connected! System ID: {master.target_system}")
    return master


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #Network handshake
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}...")

    conn, addr = s.accept()
    print(f"Connected by {addr}")


    def main():
        master = connect_drone()

        print("\n--- STARTING CONTROL LOOP ---")
        
        #recieving data 
        with conn:
            while True:
                data = conn.recv(1024).decode() #Recieves 1024 bits and decodes from binary 
                
                if not data: #stopping connection if program ends  
                    break
                
                print("Recieved: ", data)


                # Send at 20Hz (Standard for manual control)
                rate = 20 
                period = 1.0 / rate

                start_time = time.time()

                # 1. Get Input
                try: 
                    commands = json.loads(data)
                    x = commands['p'] # Pitch
                    y = commands['r'] # Roll
                    z = commands['t'] # Throttle
                    r = commands['y'] # Yaw
                    print(x, y, z, r)
                
                except json.JSONDecodeError:
                    pass

                # 2. Send MANUAL_CONTROL Message
                # https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
                try: 
                    master.mav.manual_control_send(
                        master.target_system,
                        x, y, z, r,
                        0 # Buttons mask (unused for now)
                    )
                except UnboundLocalError:
                    pass

                # 3. Debug Print (Optional - prints every 20 loops to reduce spam)
                # status_msg = f"Sent: P:{x} R:{y} T:{z} Y:{r}"
                # sys.stdout.write(f"\r{status_msg}")
                # sys.stdout.flush()

                # 4. Check for incoming data (Battery/Status)
                msg = master.recv_match(blocking=False)
                if msg:
                    if msg.get_type() == 'SYS_STATUS':
                        voltage = msg.voltage_battery / 1000.0
                        if voltage > 5.0: # Filter out garbage readings
                            print(f" [Telemetry] Battery: {voltage:.1f}V")

                # 5. Maintain Loop Rate
                time_diff = time.time() - start_time
                if time_diff < period:
                    time.sleep(period - time_diff)


    if __name__ == "__main__":
        main()