# Exercise 5: More Variables And Printing
name = 'Isaac D. Boehman'
age = 19 # 6/15/93
height = 69.0 # inches
height_cm = height * 2.54
weight = 160.0 # lbs
weight_kg = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print 'He\'s %r inches tall.' % height
print 'That\'s %d centimeters.' % height_cm
print 'He\'s %d lbs heavy.' % weight
print 'That\'s %d kilograms' % weight_kg
print 'Actually that\'s not too heavy.'
print 'He\'s got %s eyes and %r hair.' % (eyes, hair)
print 'His teeth are usually %s depending on the coffee.' % teeth

print 'If I add %d, %d, and %d I get %d.' % (age, height, weight, age + height + weight)

""" Study Drills
1. Change all the variables so there isn't the my_ in front. Make sure you change the name everywhere, not just where you used = to set them.
2. Try more format characters. %r is a very useful one. It's like saying "print this no matter what".
3. Search online for all of the Python format characters.
%d = decimal, %s = string, %r = raw (calls repr()), %f = floats
4. Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just type in the measurements. Work out the math in Python.
"""
