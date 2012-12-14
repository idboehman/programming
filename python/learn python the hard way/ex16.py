# Exercise 16: Reading And Writing Files

from sys import argv

script, filename = argv

print 'We\'re going to erase %r.' % filename
print 'If you don\'t want that, hit CTRL-C (^C).'
print 'If you do want that, hit RETURN.'

raw_input('?')

print 'Opening the file...'
# opens the file 'filename' with write permissions
target = open(filename, 'w')

print 'Truncating the file. Goodbye!'
# erasing the file of content
#target.truncate()

print 'Now I\'m going to ask you for three lines.'

line1 = raw_input('line 1: ')
line2 = raw_input('line 2: ')
line3 = raw_input('line 3: ')

print 'I\'m going to write these to the file ( %r ) we opened.' % filename

"""
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
"""
target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

print 'And finally, we close %r.' % filename
target.close()
