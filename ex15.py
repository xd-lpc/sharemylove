from sys import argv
script = argv[0]
filename = argv[1]

txt = open(filename)

print ("Here is you file %s" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input("> ")
txt_again = open (file_again)

print (txt_again.read())