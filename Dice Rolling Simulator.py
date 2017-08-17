import random
start_word = "Now, let's start rolling!"
print start_word

def roll_dice():
    number = random.randint(1, 6)
    print number

answer = True
while (answer):
    roll_dice()
    answer = raw_input('Do you want to start roll again? ') in ['yes', 'Yes']
