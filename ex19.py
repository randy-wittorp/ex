def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!\nGet a blanket.\n"

print "We can just give the function numbers directly:"
print "cheese_and_crackers(20, 30)"
cheese_and_crackers(20, 30)
print '\n\n\n'

print "OR, we can use variables from our script:"
print """
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
"""
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


