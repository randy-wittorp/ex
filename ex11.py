print "How old are you?",
age = raw_input()  #raw_input() is not in Python 3; 
                   #it is preferable to input() in python 2
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
  age, height, weight)
