""" Working with the basics of networking in Python
    using the socket module. Created a quick banner
    grabbing script
"""
import socket
# imports the socket module used for connecting to specified IP addresses
socket.setdefaulttimeout(2) # set's the default timeout to 2 seconds
sock = socket.socket() # creates a new socket called sock
sock.connect(("10.235.1.6",22)) #connects to IP specified on port 22
# in this case, my Debian server
banner = sock.recv(1024)
# grabs the banner from the connection, the first 1024 bytes
# of the connection
print banner

