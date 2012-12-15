# Exercise 21: Functions Can Return Something

def add(a, b):
        print 'ADDING %d + %d' % (a, b)
        return a + b

def subtract(a, b):
        print 'SUBTRACTING %d - %d' % (a, b)
        return a - b

def multiply(a, b):
        print 'MULTIPLYING %d * %d' % (a, b)
        return a * b

def divide(a, b):
        print 'DIVIDING %d / %d' % (a, b)
        return a / b

print 'Let\'s do some math with functions'

age = add(14, 5)
height = subtract(79, 10)
weight = multiply(80, 2)
iq = divide(200, 2)

print 'Age: %d \n Height: %d \n Weight: %d \n IQ: %d \n' % (age, height, weight, iq)

# Extra Credit puzzle
print 'Here is a puzzle.'

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
"""
becomes:   add(age, subtract(height, multiply(weight, divide(iq, 2))))
           add(age, subtract(height, multiply(weight, 50)))
           add(age, subtract(height, 8000))
           add(age, -7931)
           -7912
"""
print 'That becomes: ', what, 'Can you do it by hand?'
