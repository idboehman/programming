# Exercise 33: While Loops

i = 0
numbers = []

def numAppend(begin, end):
        """Appends the numbers from i to the given end"""
        while begin < end:
                print 'At the top i is %d' % begin
                numbers.append(begin)
                
                begin += 1
                print 'Numbers now: ', numbers
                print 'At the bottom i is %d' % begin

numAppend(i, 6)
print 'The numbers: '
for num in numbers:
        print num
