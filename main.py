import os # For reading directorys and saving files.
from datetime import date # For saving attendance based on the date
import base64 # For when i create class codes (REALLY UN-NEEDED DID IT FOR THE LOOKS)

classname = ""
# This just makes sure its defined before I set it.

def setup(): # This is the class creator / setup
    classname = input("What is the name of the class you want to set up? ")
    os.mkdir("H://Classes/" + classname) # Makes the folder for the class | If you see H:// its cause of school computers

    studentammount = int(input("How many students? ")) # Asks this so I dont have to always ask if you are done after every name
    studentammountpt2 = 0 # Used for while loop. Essentailly just takes the number of stundents mentioned and if it isnt that it adds one to this number.
    students = [] # Creates student list (Soon to be set.)
    f = open("H://Classes/" + classname + "/people.txt", "w") # Creates the file for the list of students, and opens it to be written.
    while studentammount >= studentammountpt2:
        if studentammountpt2 == studentammount:
            studentammountpt2 += 1
            print("You are done filling out student names. The names you have saved are: ") # Double check u didnt typo on someones name
            print(students) # Prints the list of students.
            pog = input("Do you want to restart? (Y/N) ") 
            if any(pog.lower() == f for f in ["yes", 'y', '1', 'ye']):
                print("Restarting...") 
                studentammountpt2 = 0 # Clears the amount of ppl gone through
                students.clear() # Clears the list. and than sends you back to the begining.
            if any(pog.lower() == l for l in ['no', 'n', '0']):
                print("Saving to file...") 
                f.write(','.join(students)) # Makes it easier to read later.
                f.close() # Closes access to the people.txt file
                yasgn = input("Do you want to copy the class code? (Y/N) ")
                if any(yasgn.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Your class code is: " + classcodes(classname)) # Prints the code of the class list.
                print("Restart the program to continue attendance!") # It kinda brokey so i just said make it restart
                exit(1)
        else:
            students.append(input("What is their name? ")) # Adds the student name to the list
            studentammountpt2 += 1 # Adds 1 to the secondary number to keep the while loop running until it hits the student number


def classcodes(classname):  # creates the class code and returns with the b64 string
    f = open("H://Classes/" + classname + "/people.txt", "r")
    deez = classname + "," + f.read()
    f.close()
    osad = base64.b64encode(deez.encode("ASCII"))
    return osad.decode("ASCII")


def readfromandsep(textfile, seperator): # reads from a file than seperates it by the seperator (BY ME)
    f = open(textfile, "r")
    return f.read().split(seperator)


def seperatetext(text, seperator): # Same as last but without the opening of files.
    return text.split(seperator)


def attendance(): 
    pog = readfromandsep("H://Classes/" + classname + "/people.txt", ",") # Takes the file and seperates the "NAME,NAME,NAME" format.
    # students = len(pog) # reads number of items
    attendance = [] # creates the list for the "NAME is here, NAME isnt here" format
    for i in range(len(pog)): # for each item in the list it asks if they are here
        yes = input("Is " + pog[i] + " here? (Y/N) ")
        if any(yes.lower() == f for f in ["yes", 'y', '1', 'ye']):
            attendance.append(" " + pog[i] + " is here")
        if any(yes.lower() == l for l in ['no', 'n', '0']):
            attendance.append(" " + pog[i] + " isnt here")
    r = open("H://Classes/" + classname + "/attendance" + str(date.today()) + ".txt", "w") # Creates file and writes too it
    r.write("Date: " + str(date.today()) + "\n") # Adds the date for easy reading
    r.write(','.join(attendance)) # Writes the list of the "NAME is here, NAME isnt here" format
    r.close() # closes so it doesnt mem leak
    print("Saved attendance for the day to Classes/" + classname + "/attendance" + str(date.today()) + ".txt") # Just tells you a quick link to your files
    exit(1) # program is done, nothing more after this point


if os.path.exists("H://Classes") == False: # If my classes file doesnt exist than make it
    os.mkdir("H://Classes")


gaming = input("Would you like to input a classcode? (Y/N) ")
if any(gaming.lower() == f for f in ["yes", 'y', '1', 'ye']):
    troll = input("Please paste it now: ") # Class codes are formated like: "CLASSNAME,NAME,NAME,NAME" than encrypted for looks, legit would work without but it looks cooler this way
    pogaming = seperatetext(base64.b64decode(troll.encode("ASCII")).decode("ASCII"), ",") # This took me way too long for 1 line, Essentially when you need to encode or decode a b64 string in python you have to encode it to bytes than decode it than conver those bytes to a string.
    if else pogaming[0] in os.listdir("H://Classes"):
        os.mkdir("H://Classes/" + pogaming[0]) # Make the class file if it doesnt exist, they just allows you to overwrite classes
    f = open("H://Classes/" + pogaming[0] + "/people.txt", "w")
    f.write(','.join(pogaming[:0] + pogaming[0 + 1:])) # Adds every item in the list except the first item (Removes the classname from the students list)
    f.close()
    print("Students: "+','.join(pogaming[:0] + pogaming[0 + 1:]))
    
dir = os.listdir("H://Classes") # had to move this because after inputing a classcode it still thought the directory was empty
if len(dir) == 0: # Checks if the directory for classes is empty if it is it sends you to setup a class
    # print("Empty directory")
    setup()
if len(dir) >= 1: # If your directory has 1 or more items than ask if you want to use them.
    pog = input(
        "You already have some classes setup do you want to use them? Yes to use custom classes, Type no to create a new class. (Y/N) ")
    if any(pog.lower() == f for f in ["yes", 'y', '1', 'ye']):
        for x in range(len(dir)):
            epic = input(dir[x] + ": (Y/N) ") # Lists out every class folder than asks if you want to use it
            if any(epic.lower() == f for f in ["yes", 'y', '1', 'ye']):
                classname = dir[x]
                blicky = input("Do you want to copy the class code? (Y/N) ")
                if any(blicky.lower() == f for f in ["yes", 'y', '1', 'ye']):
                    print("Your Class code is: " + classcodes(classname))
                attendance() # sends you to the attendance def 
    if any(pog.lower() == f for f in ['no', 'n', '0']):
        setup()


