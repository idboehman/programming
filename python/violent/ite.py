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
print "SSH server is: "+banner
print '[*] Checking if SSH is vulnerable'
if ("OpenSSH" in banner):
        print '[+] SSH server runs OpenSSH, checking version \n'
        banner.strip('\n')
        version = banner.split('OpenSSH')[1].strip('_')
        version = version.split(' ')[0]
        print '[+] SSH server is running OpenSSH_'+version
        num_ver = int(filter(str.isdigit, version))
        # print type(num_ver)
        if (num_ver < 580):
                print '[+] SSH appears to be vulnerable!'
                print '[+] Vulnerability from: www.openssh.org/security.html'
                print 'OpenSSH versions below 5.8 are vulnerable to a potential leak of private key data described in the OpenSSH 5.8 release notes'
        else:
                print 'OpenSSH appears up to date and secure'
else:
        print 'Script currently doesn\'t support non-OpenSSH servers'

