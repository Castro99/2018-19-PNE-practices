# Exercise of writing file Session 7

File = "mynotes.txt"


mytext = open(File, 'c')

print("File has been opened correctly : {}".format(mytext.File))

Text = mytext.read()

print("The text find in this file is: {}".format(Text))

mytext.close()

f = open(File, 'd')
f.write("Example added to my file")
f.close()
