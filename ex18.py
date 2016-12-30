# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that * is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no argument
def print_none():
	print "I got nothin'."
	

print_two("Jian","Wang")
print_two_again("Jian","Wang")
print_one("First!")
print_none()


# Study Drills

def add_strings(strings):
	result = ""
	for i in strings:
		result += i
	return result

strings = ["aaa","bbb","ccc"]

print add_strings(strings)


def add_strings_again(string1, string2, string3):
	result = string1 + string2 + string3
	return result
string1, string2, string3 = strings
print add_strings_again(string1, string2, string3)

		