import time
import os
import sys

# Set SDL to use the dummy driver (crucial for running on Headless Pi/SSH)
os.environ["SDL_VIDEODRIVER"] = "dummy"

from pymavlink import mavutil

# Try to import pygame for controller reading
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    print("Error: 'pygame' not found. Run 'pip3 install pygame'")
    PYGAME_AVAILABLE = False

# --- CONFIGURATION ---
CONNECTION_STRING = '/dev/serial0'
BAUD_RATE = 921600

# --- MAPPING CONFIG (You may need to tweak these for your specific controller) ---
# Xbox/PS4 Standard: 0=LeftX, 1=LeftY, 2=RightX, 3=RightY
AXIS_ROLL = 2  # Right Stick X
AXIS_PITCH = 3 # Right Stick Y
AXIS_YAW = 0   # Left Stick X
AXIS_THROTTLE = 1 # Left Stick Y

def connect_drone():
    print(f"Connecting to Pixhawk on {CONNECTION_STRING}...")
    master = mavutil.mavlink_connection(CONNECTION_STRING, baud=BAUD_RATE)
    master.wait_heartbeat()
    print(f"Connected! System ID: {master.target_system}")
    return master

def init_controller():
    if not PYGAME_AVAILABLE:
        return None
    
    pygame.init()
    pygame.joystick.init()
    
    if pygame.joystick.get_count() == 0:
        print("No controller found! Plug in a USB controller.")
        return None
    
    joy = pygame.joystick.Joystick(0)
    joy.init()
    print(f"Controller detected: {joy.get_name()}")
    return joy

def get_pwm_values(joystick):
    """
    Reads controller and returns mapped values for Pixhawk.
    Pixhawk expects:
    x (Pitch): -1000 (fwd) to 1000 (back)
    y (Roll):  -1000 (left) to 1000 (right)
    z (Throt): 0 (low) to 1000 (high)  <-- Note the 0-1000 range!
    r (Yaw):   -1000 (left) to 1000 (right)
    """
    if joystick is None:
        # Failsafe: Send Neutral if no controller
        return 0, 0, 0, 0

    pygame.event.pump() # Process internal events
    
    # 1. Read raw float values (-1.0 to 1.0)
    # Note: In Pygame, Y-axis -1 is often UP, 1 is DOWN (inverted flight style)
    raw_roll = joystick.get_axis(AXIS_ROLL)
    raw_pitch = joystick.get_axis(AXIS_PITCH) 
    raw_yaw = joystick.get_axis(AXIS_YAW)
    raw_throttle = joystick.get_axis(AXIS_THROTTLE)

    # 2. Map to Pixhawk Range (-1000 to 1000)
    # We invert pitch because pushing stick Forward (Up) usually gives -1.0 in pygame
    # but Pixhawk expects Forward to be positive or negative depending on frame.
    # Standard NED: Forward is Positive X. 
    
    # Let's stick to standard RC mapping:
    y_roll = int(raw_roll * 1000) 
    x_pitch = int(raw_pitch * -1000) # Invert so pushing stick up = move forward
    r_yaw = int(raw_yaw * 1000)

    # 3. Map Throttle (Special Case)
    # Pygame gives -1 (Up/Full) to 1 (Down/Zero) or centered 0.
    # We want 0 to 1000.
    # This formula maps a standard centered stick to 0-1000:
    # (value + 1) * 500 -> -1 becomes 0, 1 becomes 1000.
    # CHECK YOUR CONTROLLER: If your throttle is spring-loaded to center, this gives 50% throttle at rest!
    # For safety, we will simply map the raw stick to 0-1000 range assuming -1 is bottom.
    z_throttle = int((raw_throttle * -1 + 1) * 500)
    
    # Clamp values just in case
    z_throttle = max(0, min(1000, z_throttle))

    return x_pitch, y_roll, z_throttle, r_yaw

def main():
    master = connect_drone()
    joystick = init_controller()

    print("\n--- STARTING CONTROL LOOP ---")
    print("WARNING: PROPS SHOULD BE OFF.")
    print("Move sticks to send commands. Press Ctrl+C to stop.\n")

    # Send at 20Hz (Standard for manual control)
    rate = 20 
    period = 1.0 / rate

    try:
        while True:
            start_time = time.time()

            # 1. Get Input
            x, y, z, r = get_pwm_values(joystick)

            # 2. Send MANUAL_CONTROL Message
            # https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
            master.mav.manual_control_send(
                master.target_system,
                x, y, z, r,
                0 # Buttons mask (unused for now)
            )

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

    except KeyboardInterrupt:
        print("\nStopping...")

if __name__ == "__main__":
    main()