def print_two(*args):
    arg1,arg2 = args
    print ("arg1: %r,arg2: %r" % (arg1,arg2))

def print_two_again(arg1,arg2):
    print ("arg1: %r,arg2: %r" % (arg1,arg2))

def print_one(arg):
    print ("arg: %r" % arg)

def print_none():
    print ("nothing")

print_two("qq",'ww')

print_two_again('ee','rr')

print_one('a')

print_none( )