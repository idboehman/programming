""" Working with the basics of networking in Python
    using the socket module. Created a quick banner
    grabbing script
"""
import socket
# imports the socket module used for connecting to specified IP addresses
def getbanner(ip, port):
    """Grabs the banner of the given IP and port"""
    try:
        socket.setdefaulttimeout(10) # set's the default timeout to 2 seconds
        sock = socket.socket() # creates a new socket called sock
        sock.connect((ip, port)) #connects to IP specified on port 22
        banner = sock.recv(1024)
        return banner
    except Exception, e:
        print 'Caught an exception: '
        print '[-] Error = '+str(e)
        return
def check_ssh(banner):
    """Detects if SSH is vulnerable"""
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
                    print 'OpenSSH versions below 5.8 are vulnerable to a',
                    print 'potential leak of private key data described in',
                    print 'the OpenSSH 5.8 release notes'
            else:
                    print '[*] OpenSSH appears up to date and secure'
    else:
            print '[-] Script currently doesn\'t support non-OpenSSH servers'
 
 
def main():
    """Runs the script"""
    ip = raw_input("What host would you like to check for SSH vulns on? ")
    port = int(raw_input("Which port would you like to check? "))
    banner = getbanner(ip, port)
    if banner:
        print '[+] Banner of ' + ip + ':' + str(port) + ' = \n' + banner
        check_ssh(banner)

if __name__ == '__main__':
    main()
     
