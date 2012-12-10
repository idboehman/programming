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

print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6 # 7
# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - .25 + 6
# 6 - 5 + 0 - .25 + 6
# 1 + 0 - .25 + 6
# 1 - .25 + 6
# .75 + 6
# 6.75
# updated to use Floating points for division for more accurate answer

print 'Is it true that 3 + 2 < 5 - 7?'

print 3 + 2 < 5 - 7 # 5 < 2, False

print 'What is 3 + 2?', 3 + 2 # 5
print 'What is 5 - 7?', 5 - 7 # 2 

print 'Oh, that\'s why it\'s False.'

print 'How about some more.'

print 'Is it greater?', 5 > -2 # True
print 'Is it greater or equal?', 5 >= -2 # True
print 'Is it less or equal?', 5 <= -2 # False

""" Study Drills
1. Above each line, use the # to write a comment to yourself explaining what the line does.
2. Remember in Exercise 0 when you started python? Start python this way again and using the above characters and what you know, use python as a calculator.
3. Find something you need to calculate and write a new .py file that does it.
4. Notice the math seems "wrong"? There are no fractions, only whole numbers. Find out why by researching what a "floating point" number is.
5. Rewrite ex3.py to use floating point numbers so it's more accurate (hint: 20.0 is floating point).
"""
