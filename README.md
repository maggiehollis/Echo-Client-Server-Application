# Echo Client Server Application
Maggie Hollis
September 2023

This application has two functions using a simple Echo Client Server application. You can either compute a mathematical operation or find a word (based on index starting at n=1) in a sentence. 

## Acknowledgements

My client-server application is based code adapted from https://realpython.com/python-sockets/. 

### Initial Run

Open two terminal windows. On one navigate to the directory where you have saved the files. 

On one window (this will be your server window) type in: python echo-server.py [OR] python3 echo-server.py (depending on how you run python on your device)

You should see a message that the server has started and is waiting for a connection

On the other window (this will be your client window) type in: python echo-client.py [OR] python3 echo-client.py 

Once you run this you should see a message that a connection to the server has been created and will be prompted to choose between computing a mathematical operation or finding the nth word in a sentence.


### Mathematical Operation

To preform a mathematical operation type in "OPERATION".

You will then be asked to enter the type of operation (+,-,etc.) you would like to compute. Enter the character (ie. "+" or "%").

Finally enter two numbers that will appear A ~ B in the equation (where ~ is the character you entered above). Type number A, press enter, type number B, and then press enter.

On the client and server side you can see how the two interact based on the outputted messages. The last thing you will see is the answer to the equation on the client side.

If passed + 1 2, the output is: 1+2 = 3

### Finding a Word

To find the nth word in a sentence type "FIND"

You will then be asked to enter a sentence. Please type the sentence (disregarding any punctuation) and then press enter.

You will then be prompted to enter a value n, representing the nth word in the sentence. Note that the first word is at n=1. Then press enter.

On both the client and server side you can see how the two interact. The last thing you will see is the word you were looking for outputted on the client side.

If passed "I love cats" and 3, the output is: The #3 word is cat

## Writing Your Own Client or Server

### Initial Set Up

The server uses an IP address of 127.0.0.1 and a port number of 65432. The client is set to connect to these. Both sides use a python socket set up with socket.AF_INET and socket.SOCK_STREAM to use IPv4 and TCP. 

On the server side the socket then binds the port and host numbers and listens for any connections.

On the client side the socket connects to the port and host numbers above. 

Once the connection is established a new socket is created on the server side that represents the connection. The server recieves data in bytes of type utf-8 and sends them back with the same type.

### Client-Server Communication

The server expects one of two inputs. It either expects OP##A##B##C where A is an operation type (+,-,/,*,%), and B and C are numbers (either integer or decimal). It also can take FI##A##B where A is a sentence and B is an integer. Both of these types of input need to be converted in bytes using utf-8.

### Server-Client Communication

After sending the initial message the client expects just the solution/result back. If it sent an OP message it expects a float value. If it sent a FI message it expects a string value.



