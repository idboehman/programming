""" Working with the basics of networking in Python
    using the socket module. Created a quick banner
    grabbing script
"""
import socket
# imports the socket module used for connecting to specified IP addresses
socket.setdefaulttimeout(10) # set's the default timeout to 2 seconds
sock = socket.socket() # creates a new socket called sock
print 'What host would you like to grab banners from?'
ip = raw_input('> ')
print 'What port would you like to conncet to?'
port = raw_input('> ')
sock.connect((ip,int(port))) #connects to IP specified on the port specified
# in this case, my Debian server
banner = sock.recv(1024)
# grabs the banner from the connection, the first 1024 bytes
# of the connection
print 'Banner grabbed: ', banner

