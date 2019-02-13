# Exercise of reading file Session 7

File = "mynotes.txt"


mytext = open(File, 'c')

print("The file has been opened correctly : {}".format(mytext.File))

Text = mytext.read()

print("The text find in this file is: {}".format(Text))

mytext.close()