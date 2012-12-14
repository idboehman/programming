# Exercise 6: Strings And Text
# creates string x of 'There are 10 types of people.'
# places decimal 10 inside string x w/ %d
x = 'There are %d types of people.' % 10
# creates string binary containing 'binary'
binary = 'binary'
# creates string do_not containing 'don\'t'
do_not = 'don\'t'
# creates string y which places strings binary and do_not inside itself
# output y = 'Those who know binary and those who don't'
# inserts strings binary and do_not into y using %s twice
y = 'Those who know %s and those who %s.' % (binary, do_not)

# prints string x, 'There are 10 types of people.'
print x
# prints string y, 'Those who know binary and those who don't'
print y

# prints the string 'I said: There are 10 types of people.'
# places string x inside the printed string. Called by %r (raw/repr())
print 'I said: %r.' % x
# prints the string 'I also said: 'Those who know binary and those who don't'
# places string y inside printed string, called by %s
print 'I also said: "%s".' % y

# creates boolean variable hilarious and sets value to False
hilarious = False
# creates string joke_evaluation and adds in a raw value to be determined later
joke_evaluation = 'Isn\'t that joke so funny?! %r'

# prints the string joke evaluation w/ hilarious as the raw value inserted into the string
print joke_evaluation % hilarious

# Creates string w containing 'This is the left side of ...'
w = 'This is the left side of ...'
# Creates the string e containing 'a string with a right side.'
e = 'a string with a right side.'

# prints the concatination of strings w & e
print w + e

""" Study Drills
1. Go through this program and write a comment above each line explaining it.
2. Find all the places where a string is put inside a string. There are four places.
3. Are you sure there's only four places? How do you know? Maybe I like lying.
4. Explain why adding the two strings w and e with + makes a longer string.
Adding strings together ( + ) concatinates the two strings into one long string. 
i = 'foo'
j = 'bar'
print i + j # should return 'foobar'
"""
