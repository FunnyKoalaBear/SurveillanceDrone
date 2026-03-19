import socket

HOST = "0.0.0.0"  # listen on all interfaces
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    #Network handshake
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT}...")


    conn, addr = s.accept()
    print(f"Connected by {addr}")

    #recieving data 
    with conn:
        while True:
            data = conn.recv(1024).decode() #Recieves 1024 bits and decodes from binary 
            
            if not data: #stopping connection if program ends  
                break
            
            print("Recieved: ", data)




