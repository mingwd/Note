#************************************************************ EX 14
print '''
from sys import argv
script, user_name = argv
inputSource = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(inputSource)

print "Where do you live %s?" % user_name
lives = raw_input(inputSource)

print "What kind of computer do you have?"
computer = raw_input(inputSource)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
'''

#************************************************************ EX 15

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
print txt.read()
print "Typle the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#************************************************************ EX 16


from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

#************************************************************ EX 17



