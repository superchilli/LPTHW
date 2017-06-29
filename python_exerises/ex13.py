from sys import argv

script, first, second, third = argv

print argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:",third

likes = raw_input("Do you like me?")

print "So you said %r about liking me." % likes
