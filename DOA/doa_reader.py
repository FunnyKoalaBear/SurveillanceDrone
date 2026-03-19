import serial
import time 

SERIAL_PORT = '/dev/ttyACM0'  
BAUD_RATE = 115200


def main():
    while True:
        try: 
            #try to make connection and keep printing connection contents
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
            print(f"Reading form {ser.name}")

            while True:
                #continuously read incoming data and parse it to show lines independently 
                data = ser.readline().decode('utf-8').strip()
                print(f"Recieved: {data}")

        except serial.SerialException as e:
            #port not found so wait and try reconnect 
            print(f"Serial Error: {e}")
            print("Trying to connect again.. ")
            time.sleep(2)

        except KeyboardInterrupt:
            #closing serial connection 
            print("\nClosing program...")
            break

if __name__ == "__main__":
    main()
