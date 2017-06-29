from sys import argv
from os.path import exists

srcipt, from_file, to_file = argv

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
