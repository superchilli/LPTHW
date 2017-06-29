from sys import argv # impport argv

script, input_file = argv # transfer to argv

def print_all(f): #define a function called print_all,
    print f.read() # print the file's content

def rewind(f): # define a function called rewind.
    f.seek(0) # seek

def print_a_line(line_count, f): # define a function that
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
