import subprocess as yeet
import time as bruhmoment
yeet.Popen(["chmod +x UserAdd.sh"], shell=True)
users = input("Does a user need to be added, poopyhead? (y/n)")
if users == "y" or users == "Y":
    bump = 0
while bump == 0:
    yeet.Popen(["./UserAdd.sh",], shell=True)
    bruhmoment.sleep(1)
    users = input("Does a user need to be added, poopyhead? (y/n)")
    if users == "n" or users == "N":
        bump = 0
