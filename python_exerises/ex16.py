from sys import argv

script, filename = argv

print "We're going to erase %r ." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") #wait for the command

print "Opening the file..."
target = open(filename,'w') #open file for reading

print "Truncating the file. Goodbye!"
target.truncate() #truncate the file.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") #get the line 1
line2 = raw_input("line 2: ") #get the line 2
line3 = raw_input("line 3: ") #get the line 3

print "Now I'm going to write these to the file."

str = line1 + '\n' + line2 + '\n' + line3 + '\n'

target.write(str)

print "And finally, we close it."
target.close() #close file
