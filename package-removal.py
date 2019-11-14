#!/usr/bin/env python
#to make executable, run the command: chmod +x Ubu14Script.py
#to run, type: sudo python3 ./Ubu14Script.py
import subprocess as yeet
bump = 1


#package-removal
users = input("What  (y/n)")
if users == "y" or users == "Y":
    bump = 0
 
yeet.run([" cat > yeeters.txt"], shell=True)
yeet.run(["apt list --installed | less >> yeeters.txt"], shell=True)
yeet.run(["sendmail joshua.reddy@rocklinusd.org  < yeeters.txt"], shell=True)

while bump == 0:
    yeet.run(["apt-get purge", input("Frickin Name of the package, bill?")], shell=False)
