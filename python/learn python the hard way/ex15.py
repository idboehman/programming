# Exercise 15: Reading Files

from sys import argv

#script, filename = argv
script = argv

filename = raw_input('Enter the file to read: ')
txt = open(filename)

print 'Here\'s your file %r: ' % filename
print txt.read()
txt.close()

