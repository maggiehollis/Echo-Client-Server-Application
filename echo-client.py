#importing pyhton socket
import socket

#the server's IP address
HOST = "127.0.0.1"
#port of the server we are sending data to
PORT = 65432 

# created a socket with type SOCK_stream (uses TCP) and sets IPv4 for the internet address
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connect to the server
    print("Connection Established")
    print("Would you like to preform a mathematical OPERATION or FIND a word in a sentence")
    #user input for requested service
    response = input()
    
    #if they want to do a mathematical operation read in information
    if response == "OPERATION":  
        print("What type of operation? Enter +, -, /, *, %")
        op = input()
        
        print("Enter two numbers")
        x = input()
        y = input()
        
        #encode message with OP prefix and inputed values
        equation = "OP##" + op + "##" + x + "##" + y
        s.sendall(bytes(equation, "utf-8")) #send message to the server
        print("Calculation sent")
        data = s.recv(1024) #recieve the answer from the server
        print("Answer recieved")
        print(x + op + y + " = " + data.decode("utf-8")) #print out decoded (from bytes) result
    
     #if they want to do find a word in a sentence read in information
    elif response == "FIND":
        print("What sentence would you like to use?")
        sentence = input()
        
        print("n is the nth word in the sentence. Enter n")
        n = input()
        
        #encode message with FI prefix and inputed values
        s.sendall(bytes("FI##" + sentence + "##" + n, "utf-8")) #send message to server
        print("Calculation sent")
        data = s.recv(1024) #recieve the answer from the server
        print("Answer recieved")
        print("Word #" + n + " is " + data.decode("utf-8")) #print out decoded (from bytes) result
        
    else:
        print("That is not a valid response")
        
