from sys import argv #import argv

script, filename = argv #get the arguments

txt = open(filename)

#open file for reading

print "Here's your file %r:" % filename #print filename we input
print txt.read() #print the file content

print "Type the filename again:" #print some word here
file_again = raw_input("> ") #get the filename

txt_again = open(file_again) #open file again for reading

print txt_again.read() #print the file content agian

txt.close()
txt_again.close()
