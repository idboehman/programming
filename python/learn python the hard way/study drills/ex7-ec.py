# Exercise 7: More Printing
# Oh joy...

# prints the string that follows
print 'Mary had a little lamb.'
# prints the following string, inserts the string 'snow' for %s
print 'Its fleece was white as %s.' % 'snow'
# prints the string that follows
print 'And everywhere that Mary went.'
# prints the character '.' and repeats it 10 times
print '.' * 10 # what'd that do? Repeats the character '.' 10 times

# assigns strings to the variables end1 - end12
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
# Prints the concatination of strings 1 - 12 on one line
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# having not run the program w/o comma yet, I believe it just prints the 
# strings on the same line. removing it would create a new line between
# the print statements
# Having now run the program w/ comma removed, I now know that without it,
# it prints the next print statement on a new line. With it, it inserts
# a space and continues to print the same print statement on the same line

""" Study Drills
1. Go back through and write a comment on what each line does.
2. Read each one backwards or outloud to find your errors
3. From now on, when you make mistakes write down on a piece of paper what kind of mistake you made.
4. When you go to the next exercise, look at the last mistakes you made and try not to make them in this new one.
5. Remember that everyone makes mistakes. Programmers are like magicians who like everyone to think they are perfect and never wrong, but it's all an act. They make mistakes all the time.
"""
