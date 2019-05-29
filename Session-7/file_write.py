# Exercise of writing file Session 7

name = "mynotes.txt"


mytext = open(name, 'r')

print("File has been opened correctly : {}".format(mytext.name))

Text = mytext.read()

print("The text find in this file is: {}".format(Text))

mytext.close()

f = open(name, 'a')
f.write("Example added to my file")
f.close()
