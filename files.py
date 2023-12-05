import files

# Open a file
fo = open("hi.pdf", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")
fo = open("foo.txt", "r")
text = fo.read()
print (text)

# Close opened file
fo.close()
