from sys import argv
script = argv[0]
filename = argv[1]

print ("we are going to erase %r" % filename)
print ("if you don't want that, hit CTRL-C (^C).")
print ("if you really want this, hit ENTER")

input("?")

print ("Opening file ....")
target = open(filename,'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines")

line1 = input("line1 : ")
line2 = input("line2 : ")
line3 = input("line3 : ")

print ("I'm going to write these to the file ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print (" And finally, we close it")

target.close()