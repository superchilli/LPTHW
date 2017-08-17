# """
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# """
#
# # Getting user input
# name = input("What's your name? ")
# age = int(input("What's your age? "))
#
# # Manipulating strings
# year = (2017 - age) + 100
#
# print("Hi, %s! You will turn 100 years old in %d." % (name, year))

# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# num = int(input("input a number: "))
#
# if num % 2 == 0:
#     print("Even")
#
# else:
#     print("Odd")

# '''
# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
# '''
#
# a = [3, 2, 4, 3, 7, 3, 8, 0, 34, 55, 89, 202, 5, 1, 6, 33]
#
# new_a = []
#
# def less_than_5(a):
#     for i in a:
#             if i <= 5:
#                 new_a.append(i)
#     print(new_a)
#
# less_than_5(a)

# '''
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
# '''
#
# num = int(input("Choose a number to input: "))
#
# def divisor(num):
#     for x in range(2, num):
#         if num % x == 0:
#             print(x)
#
# divisor(num)

# '''
# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# '''
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# def list_overlap(a, b):
#     c=[]
#     for i in a:
#         if i in b and i not in c:
#             c.append(i)
#     return c
#
# print(list_overlap(a, b))

# '''
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
# '''
#
# word = input("input a string: ")
#
# def stringlists(word):
#     if word[:] == word[::-1]:
#         print("Your string is a palindrome.")
#     else:
#         print("Your string is not a palindrome")
#
# stringlists(word)

# '''
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and
# makes a new list that has only the even elements of this list in it.
# '''
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [x for x in a if x % 2 == 0]
#
# print(b)

# import random
#
# '''
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
# '''
#
# while True:
#     player = input("pick one to answer: rock, paper or sciccors: ")
#
#     choose = ['rock', 'paper', 'sciccors']
#
#     computer = choose[random.randint(0, 2)]
#
#     if player == computer:
#         print("try again!")
#
#     elif player == "rock" and computer == "sciccors":
#         print("You win!")
#         break
#     elif player == "paper" and computer == "sciccors":
#         print("You loose.. TAT")
#         break
#     elif player == "sciccors" and computer == "rock":
#         print("You loose.. TAT")
#         break
#     elif player == "sciccors" and computer == "paper":
#         print("You win!")
#         break
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#         break
#     elif player == "rock" and computer == "paper":
#         print("You loose.. TAT")
#         break
#     else:
#         print("Please choose the right answer!")
#         break

# '''
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# '''
# import random
#
# computer = random.randint(1,9)
# guess = 0
# t = 0
# while guess != computer and guess != "exit":
#     guess = input("guess a number: ")
#
#     if guess == "exit":
#         break
#
#     guess = int(guess)
#     t += 1
#
#     if guess > computer:
#         print("Too high! Try again.")
#
#     elif guess < computer:
#         print("Too low! Try again.")
#
#     elif guess == computer:
#         print("You win! You have guessd", t, "times!")

# '''
# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
#
# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.
# (Hint: Remember list comprehensions from Exercise 7).
#
# The original formulation of this exercise said to write the solution using one line of Python,
# but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog,
# so you can either choose to use the original directive and read about the set command in Python 3.3,
# or try to implement this on your own and use at least one list comprehension in the solution.
#
# Extra:
#
# Randomly generate two lists to test this
# '''
# import random
#
# a = random.sample(range(100), 10)
# b = random.sample(range(20, 200), 15)
#
# c = [i for i in set(a) if i in b]
# d = [i for i in c if c.count(i) == 1]
# print(d)

# '''
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.
# '''
# def get_integer(text= "Give me a number: "):
#     return int(input(text))
#
# num = get_integer()
# l = [x for x in range(2, num) if num % x == 0]
#
# def prime(num):
#     if num > 1:
#         if len(l) == 0:
#             print(num, "is a prime.")
#
#         else:
#             print(num, "is not a prime.")
#     else:
#         print(num, "is not a prime.")
#
# prime(num)

# '''
# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.
# '''
#
# import random
# l = random.sample(range(30), 12)
#
# def alist(l):
#     new_l = [l[0], l[-1]]
#     print(new_l)
#
# alist(l)

# '''
# Write a program that asks the user how many Fibonnaci numbers to generate and
# then generates them. Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
# '''
#
#
# num = int(input("How many Fibonnaci numbers you want to generate? "))
#
# def fib(n):
#     i = 1
#     if n == 0:
#         fibo = []
#     elif n == 1:
#         fibo = [1]
#     elif n == 2:
#         fibo = [1, 1]
#     elif n > 2:
#         fibo = [1, 1]
#         while i < (n - 1):
#             fibo.append(fibo[i]+fibo[i-1])
#             i += 1
#
#     return fibo
#
# print(fib(num))

# '''
# Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.
# '''
# # set
# a = [1, 1, 2, 2, 3, 4, 5, 4, 6, 7, 8, 10, 32, 2, 63, 34, 33, 44, 55, 55, 24]
# def minus_dup(x):
#     b = set(x)
#     b = list(b)
#     return b
#
# print(minus_dup(a))
#
# # loop
# a = [1, 1, 2, 2, 3, 4, 5, 4, 6, 7, 8, 10, 32, 2, 63, 34, 33, 44, 55, 55, 24]
#
# def minus_dup_loop(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b
#
# print(minus_dup_loop(a))

# '''
# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#
# My name is Michele
#
# Then I would see the string:
#
# Michele is name My
# shown back to me.
# '''
#
# def reverse_str():
#     s = input("input a long string with space: ")
#     l = s.split()
#     l = l[::-1]
#     result = " ".join(l)
#     return result
#
# print(reverse_str())

# '''
# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
# uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# '''
# import random
#
# key1 = 'abcdefghijklmnopqrstuvwxyz'
# key2 = '0123456789'
# key3 = '!@#$%^&*()<>?_'
# key4 = 'QWERTYUIIOPASDFGHJKLZXCVBNM'
#
# def generate_pw():
#     pw = random.sample(key1, 3) + random.sample(key2, 3) + random.sample(key3, 1) + random.sample(key4, 3)
#     result = "".join(pw)
#     return result
#
# print(generate_pw())

# '''
# Use the BeautifulSoup and requests Python packages to print out a
# list of all the article titles on the New York Times homepage.
# '''
#
# import requests
# from bs4 import BeautifulSoup
#
# url = 'http://www.nytimes.com'
# r = requests.get(url)
# soup = BeautifulSoup(r.text)
# title = []
#
# for story_heading in soup.find_all(class_= "story-heading"):
#     title.append(story_heading.text)
#
# print title

# '''
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.
# '''
#
# import random
# def compare(computer, user):
#     cowbull = [0, 0]
#     for i in range(4):
#         if computer[i] == user[i]:
#             cowbull[0] += 1
#
#         elif user[i] in computer:
#             cowbull[1] += 1
#     return cowbull
#
#
# def cow_and_bull():
#     computer = str(random.randint(1000,9999))
#     count = 0
#     while True:
#         user = input("Please input a 4-digit number: ")
#         count += 1
#         if user == "exit":
#             break
#         cowandbull = compare(computer, user)
#         print("You have guessed", count, "times. with", cowandbull[0], "cows and", cowandbull[1], "bulls.")
#
#         if cowandbull[0] == 4:
#             print("You win! after guessed ", count, "times. with", cowandbull[0], "cows and", owandbull[1], "bulls.")
#             break
#
#         else:
#             print("Guess again!")
#
# if __name__ == "__main__":
#     cow_and_bull()

# '''
# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
# '''
# def fn(l, n):
#     if n in l:
#         return True
#     else:
#         return False
#
# def fn(l, n):
#     s = 1
#     e = len(l) - 1
#
#     while True:
#         m = (e - s) / 2
#         if m < s or m > e or m < 0:
#             return False
#         m_l = l[m]
#         if m_l == n:
#             return True
#         elif m_l < n:
#             s = m
#         else:
#             e = m
#
# if __name__ == "__main__":
#     l = [2, 3, 4, 5, 6, 7, 8, 9]
#     fn(l, 3)

# '''
#
# Take the code from the How To Decode A Website exercise
# (if you didn’t do it or just want to play with some different code, use the code from the solution),
# and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.
# '''
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.nytimes.com"
# r = requests.get(url)
# soup = BeautifulSoup(r.text)
#
# filename = input("File to save to: ")
#
# with open(filename, 'w') as f:
#     for story_heading in soup.find_all(class_="story-heading"):
#         if story_heading.a:
#             f.write(story_heading.a.text.replace("\n", " ").strip())
#         else:
#             f.write(story_heading.contents[0].strip())

# '''
# Given a .txt file that has a list of a bunch of names,
# count how many of each name there are in the file, and print out the results to the screen.
# I have a .txt file for you, if you want to use it!
# '''
#
# counter_dict = {}
#
# with open("file.txt", 'r') as f:
#     line = f.readline()
#     while line:
#         line = line.strip()
#         if line in counter_dict:
#             counter_dict[line] += 1
#         else:
#             counter_dict[line] = 1
# print(counter_dict)

# '''
# Given two .txt files that have lists of numbers in them,
# find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000,
# and the other .txt file has a list of happy numbers up to 1000.
# '''
# # solution 1
# x = []
# with open('one.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         x.append(int(line))
#         line = f.readline()
#
# y = []
# with open('two.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         y.append(int(line))
#         line = f.readline()
#
# z = []
#
# for i in x:
#     if i in y:
#         z.append(i)
#
# print(z)
#
# # solution 2
# def file_to_list(filename):
#     filelist = []
#     with open(filename) as f:
#         line = f.readline()
#         while line:
#             filelist.append(int(line))
#             line = f.readline()
#     return filelist
#
# x = file_to_list("one.txt")
# y = file_to_list("two.txt")
#
# z = [i for i in x if i in y]
# print z

# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
# r = requests.get(url)
# soup = BeautifulSoup(r.text)
#
# for elem in soup.select("div.parbase.cn_text > div.body > p"):
#     print(elem.text)

# '''
# Ask the user what size game board they want to draw,
# and draw it for them to the screen using Python’s print statement.
# '''
#
#
# def print_horiz_line():
#     print("---" * board_size)
#
# def print_vert_line():
#     print("|  " * board_size + 1)
#
# if __name__ == "__main__":
#
#     board_size = int(input("Tell me the size of board you want: "))
#
#     for index in range(board_size):
#         print_horiz_line()
#         print_vert_line()
#     print_horiz_line()

# '''
# This time, we’re going to do exactly the opposite.
# You, the user, will have in your head a number between 0 and 100. The program will guess a number,
# and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1,
# and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy.
# An alternate strategy might be to guess 50 (right in the middle of the range),
# and then increase / decrease by 1 as needed. After you’ve written the program,
# try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)
# '''
#
# def check_grid(grid):
#     # rows
#     for x in range(3):
#         if len(set(grid[x][0], grid[x][1], grid[x][2])) == 1 and grid[x][0] != 0:
#             return grid[x][0]
#
#     # columns
#     for x in range(3):
#         if len(set(grid[0][x], grid[1][x], grid[2][x])) == 1 and grid[0][x] != 0:
#             return grid[0][x]
#
#     # diagnose
#     diag1 = set(grid[0][0], grid[1][1], grid[2][2])
#     diag2 = set(grid[0][2], grid[1][1], grid[2][0])
#     if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
#         return grid[1][1]
#
#     return 0

'''
1. ask user input
2. turn the input into int. to split and strip them
3. make the change to the list.

1. def a function to draw the game
2. def a function to know game's winner
3. play the game.
'''

# 1. ask uer to input a number:

player1 = input("type in row first and then column, (for example: 1, 2): ")
player2 = input("type in row first and then column, (for example: 1, 2): ")

# 2. turn the input into int.

list_player1 = player1.split(",")
list_player2 = player2.split(",")

final_player1 = []
final_player2 = []

for i in list_player1:
    final_player1.append(int(i.strip()) - 1)

for i in list_player2:
    final_player2.append(int(i.strip()) - 1)

grid = [[0, 0, 0,],
        [0, 0, 0,],
        [0, 0, 0,]]

'''
Implement a function that takes as input three variables,
and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python
normally takes care of for us. All you need is some variables and if statements!
'''

num = input("give me three numbers, using ' ' to ditingush them: ")
num = num.split(' ')
new_num = []
for i in num:
    new_num.append(int(i.strip()))

if new_num[0] > new_num[1] and new_num[0] > new_num[2]:
    print(new_num[0], "is the largest number!")
elif new_num[1] > new_num[0] and new_num[1] > new_num[2]:
    print(new_num[1], "is the largest number!")
else:
    print(new_num[2], "is the largest number!")
