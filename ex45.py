from sys import argv

script, filename = argv

print "=" * 40, '\n\n'
print "Let's make up a bunch of different types of rooms for a game."
print "At anytime, enter [Q] to quit.\n\n"

target = open(filename, 'w')
game_rooms = []

while True:
    room = {}
    
    # get the name of a room
    print "First, what type of room is it?  Let's give it a name."
    room['name'] = raw_input("> ").lower().capitalize()
    if room['name'].lower() == 'q':
        break
    print "Great! %s is a great room type.\n" % room['name']
    
    # get the description of a room
    print "Write a short description of a %s" % room['name']
    room['description'] = raw_input("> ")
    if room['description'].lower() == 'q':
        break
    print "\nWe're making great progress! So far we have this:"
    print "%s:" % room['name'], room['description']
    
    # get the greeting for the player as he enters
    print "\nWhat would you like the player to read as he enters the %s?" % room['name']
    room['greeting'] = raw_input("> ")
    if room['greeting'].lower() == 'q':
        break
    
    # add it to the list!!!!
    game_rooms.append(room)
    
    print "\n\n", "That room's done! Let's do another! \n", "=" * 40
    print "Remember, [Q]uit will get you out of here.\n\n"

# print game_rooms

for room in game_rooms:
    print """class %s(Room):
        \"\"\"%s\"\"\"
        
        def __init__(self)
            self.greeting = \"%s\"
        """ % (room['name'], room['description'], room['greeting'])


#need to write a Dungeon/Room class that has coord mgmt system
#Dungeon.__init__ should take two integers for a width and height. Rooms could be created at random, and the Room class could determine available directions to move
#Each Specific type of room should have a short puzzle to overcome, then give the available paths (N, S, E, W)
#Dungeon will store a two dimensional list of rooms
#will need to import random to generate random rooms




