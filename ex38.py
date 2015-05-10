ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there aren't ten things in that list; let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", 
"Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d item's now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # prints the second thing
print stuff[-1]  # prints the last thing
print stuff.pop() # pop removes last item and returns that item
print ' '.join(stuff) # prints contents of stuff with spaces
print '#'.join(stuff[3:5]) # prints stuff[3] and stuff[4] with #'s between
