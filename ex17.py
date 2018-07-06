from sys import argv
from os.path import exists
script = argv[0]
form_file = argv[1]
to_file = argv[2]


print ("Copying from %s to %s" % (form_file,to_file))

in_file = open(form_file)
in_data = in_file.read()

print ("The input file is %d bytes long" % len(in_data))

print("Does the output file exist? %r" % exists(to_file))

print ("Ready, hit ENTER to continue,CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(in_data)

print (" Alright, all done")

out_file.close()
in_file.close()