# Exercise 10: What Was That?

tabby_cat = '\tI\'m tabbed in.'
persian_cat = 'I\'m split\non a line.'
backslash_cat = 'I\'m \\ a \\ cat.'

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

""" 'Fun' Code """
# Useful for a loading prompt?
"""
while True:
        for i in ['/','-','|','\\','|']:
                print "%s\r" % i,
"""

""" Study Drills
1. Memorize all the escape sequences by putting them on flash cards.
2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of the triple-double-quote?
3. Combine escape sequences and format strings to create a more complex format.
4. Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
"""
