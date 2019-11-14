#!/usr/bin/env python
#to make executable, run the command: chmod +x Ubu14Script.py
#to run, type: sudo python3 ./Ubu14Script.py

import subprocess as yeet
print("Welcome to Aiden's Nut Cracker, better check your cup")
print("Also, pay homage to Aiden, he is about to get you fat points")
bump = 1

#user removal
users = input("Does a user need to be removed, fart sniffer? (y/n)")
if users == "y" or users == "Y":
    bump = 0
while bump == 0:
    yeet.run(["userdel", input("Name of the user, idiot?")], shell=False)
    users = input("Does another user need to be removed, booger connoisseur? (y/n)")
    if users != "y" and users != "Y":
        bump = 1

#bum daemon install
if input("Install bum, forehead? (y/n)") == ("y" or "Y"):
    print("Installing bum")
    yeet.run(["apt-get install bum"], shell=False)

#UfW install/enable
if input("Set up UFW, brick? (y/n)") == ("y" or "Y"):
    print("Installing and enabling UFW")
    yeet.run(["apt-get install ufw"], shell=False)
    yeet.run(["ufw enable"], shell=False)

#admin removal
if input("Does anyone need to be removed from admin permissions, dummy? (y/n)") == ("y" or "Y"):
    bump = 0
while bump == 0:
    yeet.run(["deluser", input("Name of the user, idiot?"), "sudo"], shell=False)
    users = input("Does anyone else need to be removed from admin permissions, Ivan? (y/n)")
    if users != "y" and users != "Y":
        bump = 1
        
#upgrade time
print("installing upgrades and updates, fatty. Oh, I mean Cooper")
yeet.run(["apt-get upgrade"], shell=True)
yeet.run("apt-get update")

#***game removal
joe = input("Ok epic gamer, do you want me to delete gnome-games-common, aisleriot, sudoku, mahjongg, ace-of-penguins, gnomine, and gbrainy? (y/n)")
if joe = "y" or joe = "Y":
  yeet.run(["sudo apt-get purge gnome-games-common gbrainy && sudo apt-get autoremove"], shell=True)
  yeet.run(["sudo apt-get purge aisleriot gnome-sudoku mahjongg ace-of-penguins gnomine gbrainy"], shell=True)
joe = input("Any uncommon games to remove, my zooma? (y/n)")
if joe = "y" or joe = "Y":
  yeet.run(["sudo apt-get purge", input("What's the game package name, ear banger?")], shell=False)

#TODO
'''
#block ports ftp, vsftpd, 
#replacing files for pwd policies and ect
yeet.run(["cp -f [original file] [new file]"], shell=True) #change pass age/complexity in replacement file(s)
#automatic update stuffs
yeet.run(["apt-get install unattended-upgrades"], shell=True)
yeet.run(["cp -f /etc/apt/apt.conf.d/10periodic [new file]"], shell=True) #change freq in replacement file
#ssh root login stuffs
yeet.run(["cp -f /etc/ssh/sshd_config [new file]"], shell=True) #change PermitRootLogin to no
#***application removal
#write all packages to file
#use sendmail to email file to off-image computer
#https://tecadmin.net/ways-to-send-email-from-linux-command-line/
#query for package purge
'''
