import time
from pymavlink import mavutil

#connection details 
connection_string = '/dev/serial0'
baud_rate = 921600


try: 
    #making connection
    myConnection = mavutil.mavlink_connection(connection_string, baud=baud_rate)
    
    print("Waiting for heartbeat...")
    myConnection.wait_heartbeat()

    #heartbeat output 
    print("Heartbeat recieved!")
    print(f"System ID: {myConnection.target_system}, Component ID: {myConnection}")


        

        
except Exception as e:
    print(f"Error: {e}")
