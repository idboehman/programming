# Exercise 3: Numbers And Math
"""
+ plus = addition
- minus = subtraction
/ slash = division
* asterisk = multiplication
% percent = modulo
< less-than = boolean, less-than
> greater-than = boolean, greater-than
<= less-than-equal = boolean, less than or equals to
>= greater-than-equal = boolean, greater than or equals to
"""

print 'I will now count my chickens:'

print 'Hens', 25 + 30 / 6 # 25 + (30 / 6) = 25 + 5 = 30
print 'Roosters', 100 - 25 * 3 % 4 # 100 - (25 * 3 % 4) = 100 - ((25 * 3) % 4) = 100 - (75 % 4) = 100 - (3) = 97

print 'Now I will count the eggs:'

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 # 7
# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - .25 + 6
# 6 - 5 + 0 - .25 + 6
# 1 + 0 - .25 + 6
# 1 - .25 + 6
# .75 + 6
# 6.75
# up to 7 b/c no floats

print 'Is it true that 3 + 2 < 5 - 7?'

print 3 + 2 < 5 - 7 # 5 < 2, False

print 'What is 3 + 2?', 3 + 2 # 5
print 'What is 5 - 7?', 5 - 7 # 2 

print 'Oh, that\'s why it\'s False.'

print 'How about some more.'

print 'Is it greater?', 5 > -2 # True
print 'Is it greater or equal?', 5 >= -2 # True
print 'Is it less or equal?', 5 <= -2 # False


