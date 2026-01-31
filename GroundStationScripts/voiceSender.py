import sounddevice as sd
import numpy as np
import socket, struct, time

#recording setup 
duration = 20 #sec
fs = 44100  #sample rate
sd.default.samplerate = fs
sd.default.channels = 1 #mono 
#sd.default.device = (68, 69) #connects to computer speaker  #output, input
gain = 20

#python3 -m sounddevice #to check supported output/input devices 

#initializing InputStream
def callback(indata, status, frames, time):
    # if status:
    #     print(status)
        
    recording.append(indata.copy())
    #callback function appends raw audio from input stream to recording array

stream = sd.InputStream(samplerate=fs, callback=callback)


#socket setup 
HOST = "0.0.0.0"
PORT = 1234

#TCP transmission 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() #(clientsocket, address) = serversocket.accept()
    print("Connected and waiting for audio.")

    with conn:
        print(f"Connected by {addr}") #logging new connection 

        while True:
            recording = []
            enter = input("Press enter to start recording: ")

            if len(enter) == 0:
    
                #recording
                stream.start()
                print("Recording started. ")
                secondEnter = input("Press enter to stop recording: ")

                while len(secondEnter) != 0: #record till second enter key input 
                    secondEnter = input("Press enter to stop recording: ")

                #stop recording             
                time.sleep(0.5) #getting the last bit of voice recoring after pause  
                stream.stop()
                print("Recording stopped. ")
                

                #preparing audio for sending
                fullAudio = np.concatenate(recording, axis=0) #makes many lists in recoring into continuous numpy array 
                louderRecording = np.clip(fullAudio * gain, -1.0, 1.0)  #increasing audio volume

                data_bytes = louderRecording.astype(np.float32).tobytes() #converting numpy array to bytes at float32 format 
                header = struct.pack('<I', len(data_bytes)) #creates header for audio payload size, little endian, unsigned 32-bit integer, databyte count is being bytified
                
                #sending data 
                conn.sendall(header + data_bytes)
                print("Recording sent!")





#upgrade 1 
# Make program with classes so functions can be called before audio is sent 
#https://docs.python.org/3/howto/sockets.html
#for now i will leave this at a working prototype

#upgrade 2 
#voice modulation features 