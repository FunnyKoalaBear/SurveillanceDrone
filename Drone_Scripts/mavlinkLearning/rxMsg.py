import time
from pymavlink import mavutil

#connection details 
connection_string = '/dev/serial0'
baud_rate = 921600


try: 
    #making connection
    myConnection = mavutil.mavlink_connection(connection_string, baud=baud_rate, dialect="common")

    print("Waiting for heartbeat...")
    myConnection.wait_heartbeat()

    #heartbeat output 
    print("Heartbeat recieved!")
    print(f"System ID: {myConnection.target_system}, Component ID: {myConnection}")

    print("Starting message check every 2 seconds.")

    while True:
        #updating to latest data
        # msg = myConnection.recv_match(blocking=False)
        # print(msg.__dict__)
        
        myConnection.recv_match(blocking=False)

        # 2. Safely check the dictionary for the message you want
        if 'VFR_HUD' in myConnection.messages:
            # VFR_HUD uses 'alt' for the pressure-derived altitude
            alt_data = myConnection.messages['VFR_HUD'].alt
            print(f"Current Altitude: {alt_data}m")
        else:
            print("Waiting for altitude data...")

        try:    
            #accessing messages dictionary
            #altitude = myConnection.messages['GPS_RAW_INT'].alt
            timestamp = myConnection.time_since('GPS_RAW_INT')
            print(timestamp)
        
        except:
            print("No altitue message recieved.")

        time.sleep(2)
        
except Exception as e:
    print(f"Error: {e}")
