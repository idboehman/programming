# Exercise 40: Modules, Classes, And Objects

class Song(object):
        """A class to represent a song"""
        def __init__(self, lyrics):
                self.lyrics = lyrics

        def sing(self):
                for line in self.lyrics:
                        print line


happy_bday = Song(['Happy birthday to you',
                   'I don\'t want to get sued',
                   'So I\'ll stop right there'])

bulls_on_parade = Song(['They rally around the family',
                        'With pockets full of shells'])

happy_bday.sing()
print '-' * 10
bulls_on_parade.sing()
print '-' * 10
stellar_lyrics = ['Meet me in outer space',
                  'We could spend the night',
                  'Watch the earth come up']
stellar = Song(stellar_lyrics)
stellar.sing()
