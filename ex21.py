def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print"DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with functions!!!!!"

age = add(25, 5)
height = subtract(70, 2)
weight = multiply(80, 2)
iq = divide(100, 2)

print "Age: %d\nHeight: %d\nWeight: %d\nIQ: %d\n" % (age, height, weight, iq)

print "Here is a puzzle."

print "That becomes :", add(age, subtract(height, multiply(weight, divide(iq, 2)))),
print "Can you do it by hand?"
