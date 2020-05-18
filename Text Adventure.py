# User Inputs 
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

# Introduction
name = input("What do they call you, travaler?\n")
print("Hmmmm, " + name + ". I've seen better but fine, let us start our journey!")
print("Shortly after you find yourself standing in a wasteland.")
print("Are you willing to learn the ways of the wasteland and make a true name for yourself " + name + "?\n")
 
# First choice 
response = ""
while response not in yes_no:
    response = input("A raider is running at you with a knife, there is a gun at your feet, do you use it?\nyes/no\n")
    if response == "yes":
        print("You shot him square in the chest, don't worry he would've did the same to you.\n")
    elif response == "no":
        print("The raider charged straight into you, slamming the knife into your chest. I knew you weren't cut out " + name + ".")
        quit()
    else: 
        print("I don't know what to do.\n")
 
# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a city in ruins.")
    print("To your right, there is more wasteland.")
    print("You could go forwards, there is a trading camp there but unless you have something worth trading, good luck.")
    print("Behind you is a hideout crawling with raiders.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("You venture into the bustling city known as Other World")
        quit()
    elif response == "right":
        print("You travel farther and farther into the wasteland. You stumble upon a shack\n")
    elif response == "forward":
        print("You walk the distance to the camp.\n")
        response = "" 
    elif response == "backward":
        print("You reload your gun, 20 bullets left, and sneak into the raiders hideout.")
        quit()
    else:
        print("What do you suggest ?\n")

print("To be continued")