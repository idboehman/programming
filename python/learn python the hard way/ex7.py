# Exercise 7: More Printing
# Oh joy...

print 'Mary had a little lamb.'
print 'Its fleece was white as %s.' % 'snow'
print 'And everywhere that Mary went.'
print '.' * 10 # what'd that do? Repeats the character '.' 10 times

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# having not run the program w/o comma yet, I believe it just prints the 
# strings on the same line. removing it would create a new line between
# the print statements
# Having now run the program w/ comma removed, I now know that without it,
# it prints the next print statement on a new line. With it, it inserts
# a space and continues to print the same print statement on the same line


