#importing pyhton socket
import socket

#this is the standard ip address to use for a loopback interface
HOST = "127.0.0.1"
#this is non-privileged the port the server is listening on
PORT = 65432

print("server starting - listening for connections at IP", HOST, "and port", PORT)
# created a socket with type SOCK_stream (uses TCP) and sets IPv4 for the internet address
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #associates this socket with our predefined host and port
    s.listen() #socket is listening for connections
    conn, addr = s.accept() #new socket conn when a connection is created
    with conn:
        print(f"Connected established with {addr}")
        while True: #reads data until there is no more
            data = conn.recv(1024)
            
            if not data: #stops the loop when no more data
                break
            
            print("Data recieved: " + data.decode("utf-8"))
            
            #decode the input data at the ## separating different parts of the data
            data = data.split(bytes("##", "utf-8"))
            
            #data is for computing an operation
            if data[0] == bytes("OP", "utf-8"):                
                try: #convert some of the input data into numbers if possible
                    x = float(data[2])
                    y = float(data[3])
                except:
                    print("The number(s) you entered are not valid")
                    conn.sendall(bytes("ERROR", "utf-8"))
                    break
                
                #set initial output
                output = 0
                
                #locate value of part of the input data and compute
                if data[1] == bytes("+", "utf-8"):
                    output = x + y
                elif data[1] == bytes("-", "utf-8"):
                    output = x - y
                elif data[1] == bytes("/", "utf-8"):
                    output = x / y
                elif data[1] == bytes("*", "utf-8"): 
                    output = x * y
                elif data[1] == bytes("%", "utf-8"):
                    output = x % y
                else:
                    print("Not a valid operation")
                    conn.sendall(bytes("ERROR", "utf-8"))
                    break
                    
                #return solution back to client
                print("Solution of " + str(output) + " has been found")
                print(f"Sending solution back")
                conn.sendall(bytes(str(output), "utf-8"))
                
            #data is for finding a word in a sentence
            elif data[0] == bytes("FI", "utf-8"):
                #split the sentence at the end of the input data into an array of words
                sentence = data[1].decode("utf-8").split(" ")
                
                try: #convert the requested nth word to a number if possible
                    n = int(data[2]) - 1
                except:
                    print("n is not a valid integer")
                    conn.sendall(bytes("ERROR", "utf-8"))
                    break
                
                #check to make sure n is not out of bounds
                if n >= len(sentence) or n < 0:
                   print("n is not valid")
                   conn.sendall(bytes("ERROR", "utf-8"))
                   break
            
                #send back the word
                print("Requested word is " + sentence[n])
                print(f"Sending solution back")
                conn.sendall(bytes(sentence[n], "utf-8"))
                
            else:
                print("That is not a valid preformance.")
                conn.sendall(bytes("ERROR", "utf-8"))
                break 
    
            

print("Server is done!")
