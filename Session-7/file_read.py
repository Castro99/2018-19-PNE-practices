# Exercise of reading file Session 7

name = "mynotes.txt"


mytext = open(name, 'r')

print("The file has been opened correctly : {}".format(mytext.name))

Text = mytext.read()

print("The text find in this file is: {}".format(Text))

mytext.close()