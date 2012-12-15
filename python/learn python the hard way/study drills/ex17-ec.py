# Exercise 17: More Files
# fewest lines possible
import sys 
open(sys.argv[2], 'w').write(open(sys.argv[1]).read())
print 'Copied %s to %s' % (sys.argv[1], sys.argv[2])

