# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksongille'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s is in %s" % (city, abbrev)

# now do both at once
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'does not exist')
print "The city for the state 'TX' is: %s" % city

print """
-----------------------------------------------------------
You may now enter additional states and their corresponding
abbreviations.  To exit, enter [Q]"""
while True:
    # print "Enter new state name:"
    new_state = raw_input("Enter new state name:")
    if new_state.lower() == 'q':
        break
    print "Enter abbreviation:"
    new_abbrev = raw_input("> ")
    if new_abbrev.lower() == 'q':
        break
    print "-" * 60
    print "You have entered %s, abbreviated as %s." % (new_state, new_abbrev)
    print "Correct? [Yn]"
    confirmation = raw_input("> ")
    if confirmation.lower() == 'n':
        continue
    else:
        states[new_state] = new_abbrev
    print "Would you like to see all the states so far[Yn]?"
    display_states = raw_input("> ")
    if display_states.lower() == 'n':
        continue
    else:
        print '-' * 10
        for state, abbrev in states.items():
            print "%s is abbreviated %s" % (state, abbrev)
    print "-" * 60



