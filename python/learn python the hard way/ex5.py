# Exercise 5: More Variables And Printing
my_name = 'Isaac D. Boehman'
my_age = 19 # 6/15/93
my_height = 69 # inches
my_weight = 160 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print 'He\'s %d inches tall.' % my_height
print 'He\'s %d lbs heavy.' % my_weight
print 'Actually that\'s not too heavy.'
print 'He\'s got %s eyes and %s hair.' % (my_eyes, my_hair)
print 'His teeth are usually %s depending on the coffee.' % my_teeth

print 'If I add %d, %d, and %d I get %d.' % (my_age, my_height, my_weight, my_age + my_height + my_weight)
