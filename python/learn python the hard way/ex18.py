# Exercise 18: Names, Variables, Code, Functions

# this is one like your scripts with argv
def print_two(*args):
        arg1, arg2 = args
        print 'arg1: %r, arg2: %r' % (arg1, arg2)

# *args is useless in that case
def print_two_2(arg1, arg2):
        print 'arg1: %r, arg2: %r' % (arg1, arg2)

# just one argument
def print_one(arg1):
        print 'arg1: %r' % arg1

# none
def print_none():
        print 'I got nothin\'.'

print_two('Boehman', 'Frog')
print_two_2('Boehman', 'Toad')
print_one('This?')
print_none()
