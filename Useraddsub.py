import subsystem as yeet
users = input("Does a user need to be added, poopyhead? (y/n)")
if users == "y" or users == "Y":
    bump = 0
while bump == 0:
    yeet.Popen(["./UserAdd.sh",], shell=True)
    users = input("Does a user need to be added, poopyhead? (y/n)")
    if users == "n" or users == "N":
        bump = 0
