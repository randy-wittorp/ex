from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room()
    print """There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?"""
    bear_moved = False
    
    while True:
        next = raw_input("> ").lower()
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.  You can go through it."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead(