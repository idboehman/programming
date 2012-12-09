"""
# Basics
# An quick rundown of basics of python
# Variables
# var_name = var assignment
# variables automatically typed
# ex:
port = 21
# port will be of type int
print "should return <type 'int'>"
print type(port)
banner = "Apache 2.x"
print "banner is of type 'str'"
print type(banner)
openHuh = True
print "should return <type 'bool'>"
print type(openHuh)
portList=[21,22,23,80,443]
print "an array (list) of ports, type 'list'"
print type(portList)
"""
"""
# String manipulation 
# strings have methods upper(), lower(), replace(old,new), find(), etc
# upper() = makes entire string upcase
# lower() = does same as above except lowercase
# replace(old,new) replaces the old substring w/ new substring
# find(substr) returns the offset of the first occurance of given substring
# examples
print 'banner.upper() should return "APACHE 2.X" '
print banner.upper()
print 'banner.lower() should return "apache 2.x" '
print banner.lower()
print "banner.replace('ach','ugr') should return 'Apugre 2.x' "
print banner.replace('ach','ugr')
print "banner.find('2.') should return 7"
print banner.find('2.')
"""

"""
# Lists & their manipulation
print "using portList definited earlier"
print 'should output [21,22,23,80,443]'
print portList
print 'removing elements'
print 'portList.remove(23) should remove element 23 (telnet port)'
portList.remove(23)
print '[21,22,80,443] should be the list returned'
print portList
portList.remove(443)
print '[21,22,80] should be the list returned from portList.remove(443)'
print portList
print 'adding port 8080 to the portList via portList.append(8080)'
portList.append(8080)
# [21,22,80,8080]
print 'adding port 3306 to the portlist via portList.append(3306)'
portList.append(3306)
print 'current portlist should be [21,22,80,8080,3306]'
print portList
print 'sorting the list via portList.sort()' 
portList.sort()
print '[21,22,80,3306,8080] is the sorted list'
print portList
print 'finding index of ports 22 and 8080 and storing as variables'
posSSH = portList.index(22)
posHTTPalt = portList.index(8080)
print '[+] There are '+str(posSSH)+' ports to scan before SSH and '+str(posHTTPalt)+' ports before the HTTP alternative (8080)'
print 'length of a list using len(list)'
portListLen = len(portList)
print '[+] Scanning '+str(portListLen)+' ports total'
"""

""" Dictionaries """
# similar to a Map, elements of the list have a key and value
# created by:
# dictname = {'key':value, 'key2':value2, ..., 'keyx':valuex}
print 'Creating a dictonary of common services & associated ports'
services = {'ftp':21, 'ssh':22, 'telnet':23, 'www':80, 'mysql':3306, 'www-alt':8080}
print 'Printing the keys of the services dictionary via services.keys()'
print services.keys()
print 'Printing all the items of the services dictionary via services.items()'
print services.items()
print 'Checking if dictionary has a key'
print 'Ex: services.has_key("ftp") should return True, services.has_key("smtp") => False'
print 'services.has_key("ftp"): '+str(services.has_key("ftp"))
print 'services.has_key("smtp"): '+str(services.has_key("smtp"))
print 'If a key is in the dictionary, can call its value by the element\'s key'
print 'Ex: services["ftp"] should reutrn 21, services["mysql"] should return 3306'
print 'services["ftp"]: '+str(services["ftp"])
print 'services["mysql"]: '+str(services["mysql"])
