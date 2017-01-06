from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Openning the file..."
target = open(filename, 'w') # w: write

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

prompt = "line %d: " # to define a string variable for prompting
fmt = "\n" # formatter "\n"

line1 = raw_input(prompt % 1)
line2 = raw_input(prompt % 2)
line3 = raw_input(prompt % 3)


print "I'm going to write these to the file."
# the first way
target.write("the first way" + fmt)
for i in [line1, line2, line3]:
	target.write(i + fmt)	
	
# the second way
target.write("the second way" + fmt)
target.write(line1 + fmt + line2 + fmt + line3 + fmt)

# the third way
target.write("the third way" + fmt)
i = 0
line = [line1, line2, line3]
while i < 3:
	target.write(line[i] + fmt)	
	i += 1
	
print "And finally, we close it."
target.close()
