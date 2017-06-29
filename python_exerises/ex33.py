numbers = []
numbers_1 = []
def count_i(i, f):
    while i < 10:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + f
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

count_i(2, 3)

print "The numbers: "

for num in numbers:
    print num

for m in range(0, 6):
    numbers_1.append(m)

print numbers_1
