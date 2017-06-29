from sys import exit

def call_wife():
    print "The phone is not picking up."
    print "You thought she was busy and doing nothing. Or review the message then\
    get money."
    print "Your choice is: 'doing nothing'/'get money'/'call police'"

    choice = raw_input('> ')

    if choice == "doing nothing":
        dead("Your wife is dead.")

    elif choice == "get money":
        get_money()

    else:
        dead("Your wife is dead.")

def get_money():
    print "You went to the place, and someone trying to rob you."
    print "You lost the money."
    print "Then, you got a phone call from the kidnapper."
    print "he said 'You idiot! Your wife is in somewhere you know.' "
    print "There are three places you come in mind, home, workplace, restaurant."
    print "Your choice is: 'home'/'workplace'/'restaurant'"
    choice = raw_input('> ')
    if choice == "home":
        dead("Your wife is dead.")

    elif choice == "workplace":
        work_place()

    elif choice == "restaurant":
        restaurant()

    else:
        dead("Your wife is dead.")

def call_police():
    print "after call the police, you went to get the money."

    print "You went to the place with the money, along with the police."
    print "A robber trying to rob you, he was stopped by the police."
    print "He told you only they are sure that he get the money or they will kill your wife."
    print "So you choose to:"
    print "Your choice is: 'give money'/'not give'"
    choice = raw_input('> ')
    if choice == "give money":
        print "You win, the robber tell you the place and the police saved your wife."
    else:
        dead("Your wife is dead.")

def work_place():
    print "Your wife's colleague told you that she left early for the anniversary celebrations."
    print "She might go to booking the restaurant."

    print "You choose to go:"
    print "Your choice is: 'restaurant'/'home'"
    choice = raw_input('> ')
    if choice == "restaurant":
        restaurant()
    else:
        dead("Your wife is dead.")

def restaurant():
    print "You went to a restaurant you used to go."
    print "The manager said that your wife come this morning, and she said she\
    wants to buy the cake."

    print "You know a cake store that you two loved so much. but the store seems\
    closed for a while."

    print "So you decided to:"
    print "Your choice is: 'cake store'/'call police'/'home'"

    choice = raw_input('> ')

    if choice == "cake store":
        dead("You found your wife, but the bad guys found you too. They killed both of you.")

    elif choice == "call police":
        call_police()

    else:
        dead("Your wife is dead.")

def dead(words):
    print words, "You can marry your lover now."

    exit(0)

def start():
    print """
    You got a message:
    Your wife is here,
    and you'd better hurry and bring 100000 dollars to this place: xxx,
    or you will get a dead body.
    along with a picture of your wife with a crying face.
    """
    print "Your choice is: 'call wife'/'get money'/'call police'/'doing nothing'"

    choice = raw_input('> ')

    if choice == "call wife":
        call_wife()

    elif choice == "get money":
        get_money()

    elif choice == "call police":
        call_police()

    else:
        dead("Your wife is dead.")

start()
