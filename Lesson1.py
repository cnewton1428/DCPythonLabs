# print " Lesson \t Topic \n 1 \t Strings and Conditionals \n 2 \t Lists and Loops \n 3 \t Dictionaries & Files"

# twitter = "@hearmecode"
# print twitter[1:5]

# phone = "(202) 456-7890"

# print phone [1:4]
# print phone [6:9]
# print phone [10:]

# name = "Car" #string
# age = 28 #number
# print "My name is: {0} and my age is: {1}" .format(name, age) #print out string and do something
# #.format(name, age) told what variables are put into the string in the spot/placeholders 0 and 1

# phone = "202-555-6789"
# print "Call {0} for great pizza" .format(phone[4:]) #slice at character 4 to the end

# tweet = """In just over one year, @hearmecode has reached over 800 members who are learning how to code together."""
# print """That tweet is {0} characters.
# You have {1} characters left""".format(len(tweet), 140-len(tweet)) #0 character is the 1st spot after .format(0, 1) so 0= len(tweet), 1=140-len(tweet)

# #function is len and variable with tweet


# phone = "202-555-9876"
# print "The area code is {0} \nThe Local is {1}" .format(phone[0:3], phone[4:])

# phone1 = "(202) 555-9876"
# print "Different format: {0}".format(phone1[0:])

# #Correct format
# phone = "202-555-9876"
# print "The area code is {0} \nThe Local is {1}" .format(phone[0:3], phone [4:]) 
# print "Different format: ({0}) {1}" .format(phone[0:3], phone[4:])

# twitter = "@hearmecode"
# print twitter.replace ('@', '#') #what it's looking to replace (@) in 1st character and with what in 2nd character (#) within brackets
# #so replace @ with # in hearmecode
# #hearmecode final answer

# #python performs arguments that came before .function 

# state = 'District of Columbia'
# print state
# print state.upper()
# print state.lower()

# article = """At Hear Me Code, students are teachers in training. The key to the classes' appeal, said Criqui, who is now an assistant teacher at Hear Me Code? "It's by women, for women," she said..."""

# print article.count(" he said")
# print article.count(" she said")

#CONDITIONALS

#indent to the end of the margin to run 
#Don't leave space before the words or variables and only tab once for if and then

students = 10
capacity = 50

if students < capacity:
	print "Keep recruiting"
else:
	print "End ticket signups"
#if this statement is true on line 4 print line 5; no matter what keep recruiting

#two equal signs to compare variables; does 5=5 or no so just True and false

#elif like a multiple choice question 

location = "DC"

if location == 'DC':
	print "District of Columbia"
elif location == 'MD':
	print "Maryland"
elif location == 'VA':
	print "Virginia"
else:
	print "Somewhere else"

students = 40
teaching_assistants = 5

if teaching_assistants == 0:
	print "None? Uh oh!"	
elif teaching_assistants < students /5 :
	print "Keep recruiting TAs"
else:
	print "Aren't the TAs great though?"

#therefore need 3 more TA's 

#MORE EXAMPLES OF CONDITIONALS

name= "Carina"

if name != '':
	print "Hello, {0}!".format(name)
else:
	print "Name cannot be blank!"

#another way to say it!
if name == '':
	print "Name cannot be blank!"
else:
	print "Hello, {0}!".format(name)


Volunteers = 90
Goal= 100

if Volunteers == Goal:
	print "Goal reached!"
elif Volunteers < Goal:
	print "You are behind!"
else: 
	print "At Capacity! Try again next year!"

#or if, else, else

article = """Hear Me Code is more than just a coding class... it's just as much about building community and developing the next set of women leaders in tech."""

if "Hear Me Code" in article:
	print "Hear Me Code was mentioned in this article!"
else:
	print "This article is about something else."

#Complex Conditionals

# if state.upper() == 'DC':
# 	print "District of Columbia"

# if email_address.count('@') > 1:
# 	print "{0} is not a valid email".format(email_address)

# if len(phone) <7:
# 	print "This phone number is too short!"

	#Compound Conditionals need and to run

	#and both variables equal the same then run

	#or doesn't have to have equal variables to run

	#Line 7 on equal nested conditionals 

lesson = 4

if lesson == 1:
	print "Strings and Conditionals"
elif lesson == 2:
	print "Lists and Loops"
elif lesson == 3:
	print "Dictionaries and Files"
elif lesson >= 4:
	print "We don't teach these in person anymore"
	print "But they're available for self-study"

	if lesson ==4:
		print "Functions"
	elif lesson ==5:
		print "APIs"

#ASSIGNMENT (Code =translate information into a language comp can understand)
#Python Lesson Playtime Lesson 01 twitter.py

# Difficulty Level: Beginner
# Exercise: Tweet length calculator

# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Hear Me Code class was so much fun today!"

tweet = "Hear Me Code class was so much fun today!"

# Measure the length of that tweet.

print len(tweet)

# Was that tweet more than 140 characters?
#   If so, tell the user it was too long!

# Was that tweet 140 or fewer characters?
#   If so, tell the user how witty they are!

# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit


len_tweet = len(tweet)

if len_tweet > 140:
	print "Tweet is too long"
elif len_tweet == 140:
	print "You've reached the limit"
elif len_tweet < 140:
	print "You're very witty"
else:
	print """The tweet is {0} characters. You have {1} characters left""".format(len(tweet), 140-len(tweet)) 


# Part three:
# Twitter announced they are changing their character limit to 280, but they might change it again.
# Can you make your code flexible enough so that you don't have to replace the character limit in multiple places in your code?

def say_hello(name):
	'''Accepts one argument that's a string. Returns a string saying hello to name.'''
	#return "Hello %s!" %name

	#result = say_hello("Cari")
	return "Hello" + name + ""

print result 
