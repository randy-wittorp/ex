from random import *
import os

class Dungeon(object):
    """This class will define the size of the dungeon.
    Will also automatically populate the dungeon with
    a random assortment of rooms"""
    
    def __init__(self, x=3, y=3):
        """Takes optional arguments for length of x axis and length
        of y-axis"""
        self.x_axis = x
        self.y_axis = y
        self.dungeon_rooms = {}
        self.visited_rooms = []
        self.current_room = (randint(0, (x - 1)), randint(0, (y - 1)))
        
        for x_coord in range(0, self.x_axis):
            for y_coord in range(0, self.y_axis):
                self.dungeon_rooms[(x_coord, y_coord)] = self.random_room()
                y_coord += 1
            x_coord += 1
        print "You are now in the", self.dungeon_rooms[self.current_room].get_name()
        
    
    def random_room(self):
        """Returns random room with coords x, y"""
        the_room = Room()
        selection = randint(0, 5)
        if selection == 0:
            the_room = Poopery()
        elif selection == 1:
            the_room = Refractory()
        elif selection == 2:
            the_room = Storage_room()
        elif selection == 3:
            the_room = Distillery()
        elif selection == 4:
            the_room = Broom_closet()
        elif selection == 5:
            the_room = Telethon()
        elif selection == 6:
            pass
        elif selection == 7:
            pass
        return the_room
    
    def draw(self):
        """This function will draw the dungeon, with an 'X' where
        the player currently is, and '*'s where he's been"""
        print "Current room is", self.current_room
        for y_coord in range(0, self.y_axis):
            print "=" * (self.x_axis * 3 + 1)
            for x_coord in range(0, self.x_axis):
                if (x_coord, y_coord) == self.current_room:
                    print "|X",
                elif (x_coord, y_coord) in self.visited_rooms:
                    print "|*",
                else:
                    print "| ", 
            print "|"
        print "=" * (self.x_axis * 3 + 1)
    
    def describe(self):
        """This will call a function to query the Room class
        object for its description"""
        print dungeon_rooms[current_room].room_description()
        
    def move(self, where):
        """This takes a direction and moves the player"""
        os.system('clear')
        self.visited_rooms.append(self.current_room)
        x_coord, y_coord = self.current_room
        if str(where).lower() == 'n' and y_coord > 0:
            y_coord -= 1
        elif str(where).lower() == 's' and y_coord < (self.y_axis - 1):
            y_coord += 1
        elif str(where).lower() == 'w' and x_coord > 0:
            x_coord -= 1
        elif str(where).lower() == 'e' and x_coord < (self.x_axis - 1):
            x_coord += 1
        elif str(where).lower() == 'q':
            exit(0)
        else:
            print "That is not a valid move"
        self.current_room = (x_coord, y_coord)
        self.draw()
        print "You are now in the", self.dungeon_rooms[self.current_room].get_name()
        print self.dungeon_rooms[self.current_room].get_description()
        

class Room(object):
    
    
    def get_moves(self):
        pass
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
        
    
    def check_if_visited(self):
        pass
        
    def __str__(self):
        return "%s" % self.name
    
    def __repr__(self):
        return "%s" % self.name
        
class Poopery(Room):
    def __init__(self):
        self.description = """The smell of poop is overwhelming.
        \nWhich way shall we go?"""
        self.name = "Poopery"
    


class Refractory(Room):
    def __init__(self):
        self.description = """This seems like a nice place to reflect.
        \nWhich way shall we go?"""
        self.name = "Refractory"
    


class Telethon(Room):
    def __init__(self):
        self.description = """The ringing of telephones is unbearable.
        \nWhich way shall we go?"""
        self.name = "Telethon"
    
    

class Storage_room(Room):
    def __init__(self):
        self.description = """Aptly named.  There are things stored here.
        \nWhich way shall we go?"""
        self.name = "Storage Room"
    


class Distillery(Room):
    def __init__(self):
        self.description = """Finally, something to drink.  Unreal.
        \nWhich way shall we go?"""
        self.name = "Distillery"
    

class Broom_closet(Room):    
    def __init__(self):
        self.description = """Not my house.  I'm not cleaning up.
        \nWhich way shall we go?"""
        self.name = "Broom Closet"
    



test = Dungeon(5,5)
while True:
    test.move(raw_input("[N], [S], [E], or [W]\n> "))




        
