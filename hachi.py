import socket
import time
import random

# Create a socket
s = socket.socket()
s.bind(("localhost", 8020))
s.listen(5)

print("Waiting for a connection...")
c, adr = s.accept()
print("Connection to " + str(adr) + " established")

# Total number of frames to send
a = int(input("Enter total number of frames: "))

x = 0
print("Sending -->", x)
c.send(str(x).encode())

while a > 1:
    timer = 5
    t = random.randint(1, 7)

    msg = c.recv(1).decode()

    if timer > t:
        time.sleep(3)
        print("ACK -->", msg)
        x = int(msg)
        print("Sending -->", str(x))
        c.send(str(x).encode())
    else:
        time.sleep(3)
        print("Timeout")
        print("Sending again -->", x)
        c.send(str(x).encode())

    a -= 1

print("All frames sent successfully.")
c.close()
s.close()

#################################################

import socket

# Create a socket
s = socket.socket()
s.connect(("localhost", 8020))

while True:
    msg = s.recv(1).decode()
    print("Received -->", msg)

    x = int(msg)

    if x == 0:
        x = x + 1
    else:
        x = x - 1

    s.send(str(x).encode())
##########################################
# OUTPUT:
# Waiting for a connection...
# Connection to ('127.0.0.1', 49532) established
# Enter total number of frames: 3
# Sending --> 0
# ACK --> 1
# Sending --> 1
# ACK --> 0
# Sending --> 0
# All frames sent successfully.


# Received --> 0
# Received --> 1
# Received --> 0
