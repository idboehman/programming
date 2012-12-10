import sys
import os
# Given a word, lists all the words that could appear next in a word ladder using given
# list of 3807 four-letter words
# Ex: wordLadder('puma') ->
# duma, pima, puja, pula, pump, puna, pupa
def wordLadder(word):

def main():
        if len(sys.argv) == 2
        wlist = sys.argv[1]
        # Check if the file exists 
        if not os.path.isfile(wlist):
                print '[-] '+wlist+' does not exist.'
                exit(0)
        # Check's if we have read permissions on the file
        if not os.access(wlist, os.R_OK):
                print '[-] Do not have read permissions for '+wlist
                exit(0)
        word = raw_input('What word would you like to check word ladder for?')
        print '[+] Checking for word ladders of '+word+' using the wordlist: '+wlist
        wordLadder(word)

