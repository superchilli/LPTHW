# Jumble Words
# @Sihua 2017/07
import random

print """
Here is a random dic, and we will random pick one word from the dic.
We will reorder the word, and give that word to you.
Your mission is to guess what's the orginal word and give the answer.
Notice that you only got three chance!
"""

dic = ['guess', 'university', 'package', 'selection', 'hospital']

word = random.choice(dic)   # word = dic[randomInt(0, len(dic))]

def messyWord(word):
    # 1. split
    split_word = list(word) # ['g', 'u', 'e', 's', 's']
    length = len(split_word)
    new = []

    # when use 'for' in favor of 'while'??
    for i in range(0, length):
        randomIndex = random.randint(0, len(split_word) - 1)
        new.append(split_word[randomIndex])
        split_word.remove(split_word[randomIndex])

    new_word = ''.join(new)
    print new_word

print "Here is your word: "

messyWord(word)

chance = 1

while chance <= 3:
    guess = raw_input('Your answer is:')
    if  guess == word:
        print "Congrats! You win!"
        break
    else:
        if chance == 3:
            print "You lose!"
        else:
            print "Try again!"
        chance += 1
