import time
from pymavlink import mavutil

# /dev/serial0 is the alias for the GPIO UART pins we enabled earlier
connection_string = '/dev/serial0'
baud_rate = 921600

print(f"Trying to connect on {connection_string} at {baud_rate}...")

try:
    # Create the connection
    master = mavutil.mavlink_connection(connection_string, baud=baud_rate)

    # Wait for the first heartbeat
    # This is a blocking command. It will pause here until it hears from Pixhawk.
    print("Waiting for heartbeat...")
    master.wait_heartbeat()

    # If we get here, IT WORKED!
    print("Success! Heartbeat received.")
    print(f"System ID: {master.target_system}, Component ID: {master.target_component}")

    # Print a few attitude messages to prove data flow
    for i in range(5):
        msg = master.recv_match(type='ATTITUDE', blocking=True)
        if msg:
            print(f"Message {i+1}: Roll={msg.roll:.2f} Pitch={msg.pitch:.2f}")

except Exception as e:
    print(f"Error: {e}")