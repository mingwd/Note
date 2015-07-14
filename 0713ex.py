myName = 'Zed'
my_age = 35 # not a lie
my_height = 74.7 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % myName
print "Let's talk about",  myName
print "my height is", round(my_height, 1)

#************************************************************ EX 6

string1 = "this is the first part"
string2 = "of the second part"
print string1 + string2
print string1, string2

#************************************************************ EX 7

print "Mary had a little lamb."
print "Its fleece was white as %s." % "snow"
print "And everywhere that Marry went."
print "." * 10 # print out 10 "*" ?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

#************************************************************ EX 8

formatter = "%r %r %r %r"

print formatter % ("one", "two", "\nthree", 'four')
print 'this is a string'

#************************************************************ EX 9

print "print double quote \
	this way"
print """ or print
	double
	quote
	this 
	way"""

days = "Mon Tue Wed Thu Fri Sat Sun"
print "Here are the days: ", days
print "Here are the days: " + days

#************************************************************ EX 10 & 11

#while True:
    #for i in ["/","-","|","\\","|"]:
	        #print "%s\r" % i,

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#************************************************************ EX 12

age = raw_input("How old are you? ")

#************************************************************ EX 13
# python module !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#************************************************************ EX 14

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions. "
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_nput(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)


