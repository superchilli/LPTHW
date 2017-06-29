def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# call function cheese_and_crackers, use the variables + int

def count_star(star):
    print "Today we can see %d stars." % star

count_star(20)

count_star(30 + 20)

you_see = int(raw_input("How much stars do you watch today?"))

count_star(you_see)
