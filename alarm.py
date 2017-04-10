import time, webbrowser, random, os

#Check if the user has the Youtube.txt file having youtube links
if os.path.isfile("Youtube.txt") == False:
	print "ERROR: Youtube.txt file not created. Creating file..."

	#error if creating and already exists and write only file
	flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY 

	#creating a file and setting flags
	filecreate = os.open("Youtube.txt", flags)
	with os.fdopen(fisierCreat, 'w') as fileCreated:
	    fileCreated.write("https://youtu.be/BZg8BhBWyo8")


#The User can set the time they want to wake up
Alarm = raw_input("What time do you want to wake up? (Follow HH:MMAM/PM Fomart): ")

#First state the Time variable so it's usable in the while-loop
Time = time.strftime("%I:%M%p")

#This opens the text file with the youtube links
with open("Youtube.txt") as f:
	#the urls are stored in the url_values variable 
	url_values = f.readlines()


#Run the loop till the time is not equal. You can even print the time.
while Time != Alarm:
	print "The time is " + Time
	
	#Restating the Time variable allows the time to refresh
	Time = time.strftime("%I:%M%p")
	
	#This keeps the loop from flooding the command line with updates of the time :P
	time.sleep(1)

#If the Time variable is equal to the Alarm string, this code activates
if Time == Alarm:
	print "Time to Wake up!"
	#from the variable url_values, a random link is chosen and then that link is stored in random_video variable
	random_video = random.choice(url_values)
	#Using the webbrowser library, it opens this youtube video link.
	
webbrowser.open(random_video)