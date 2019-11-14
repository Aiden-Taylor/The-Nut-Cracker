#!/usr/bin/env python
#to make executable, run the command: chmod +x Ubu14Script.py
#to run, type: sudo python3 ./Ubu14Script.py

import subprocess as yeet
import threading as marxismRules
print("Welcome to Aiden's Nut Cracker, better check your cup")
print("Also, pay homage to Aiden, he is about to get you fat points")
bump = 1

#Logs
yeet.run([" cat > log.txt"], shell=True)

def concurrent_command(command_stuff) {
	yeet.run([command_stuff],shell=True)
}

#upgrade time
if input("Upgrade, Quakebuttock? (y/n)") == ("y" or "Y"):
    threads = []
    print("installing upgrades and updates, fatty. Oh, I mean Cooper")
    yeet.run(["apt-get upgrade"], shell=True)
    bees = marxismRules.Thread(target=concurrent_command,args=("apt-get upgrade"))
    bees.start()
    threads.append(bees)
    yeet.run(["apt-get update"], shell=True)
    bees = marxismRules.Thread(target=concurrent_command,args=("apt-get update"))
    bees.start()
    threads.append(bees)
    for thread in threads:
        thread.join()
    yeet.run(['echo "Updates Installed Hopefully" >> log.txt'], shell=True)
    
#Ports
kekel = input("Do you wan some ports?")
if kekel == "y" or kekel =="Y":
	things = ["69","6660","6661","6662","6663","6664","6665","6666","6667","6668","6669","23","135","411","412","61","21","20","3389","25","139"]
	kekel = input("Specifically block ports or just let the program go through its list ya weed smokin, cop shootin, bike stealin, watermelon munchin, finger lickin, white woman rapin, go for nothin respectable white person? (Y/N)")
	if kekel == "Y":
		kekel = input("put in ports you want to block in format of     10,23,22,80... its pretty sad i need to explicitly state this, really goes to show the amount of brain cells you have")
		things = kekel.split(",")
	for port in things: 
		yeet.run(["ufw deny",port],shell=False)
		print("Port #" + port + " has been blocked :)")
		yeet.run(['echo "port #' + port + ' is done heker" >> log.txt'],shell=False)
	kekel = input("Do you want to save changes across reboot? (Y/N)")
	if kekel == "Y":
		yeet.run(["service iptables save"],shell=False)
	yeet.run(['echo "ports are heked you heker" >> log.txt'],shell=False)
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#                                        MOVING ON TO SERVICES
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
kekel = input("u wan some services mr dummy head?")
if kekel == "y" or kekel == "Y":
	things = ["telnet","vsftpd","apache2"]
	kekel = input("Specifically block services or just let the program go through its list ya weed smokin, cop shootin, bike stealin, watermelon munchin, finger lickin, white woman rapin, go for nothin respectable white person? (Y/N)")
	if kekel == "Y":
		kekel = input("put in services you want to block in format of     telnet,ftp,service_name...")
		print("PS ur mom is a ho")
		things = kekel.split(",")
	for service in things:
		yeet.run(["systemctl stop",service],shell=False)
		yeet.run(["systemctl disable",service],shell=False)
		yeet.run(["systemctl daemon-reload"],shell=False)
		yeet.run(["systemctl reset-failed"],shell=False)
		print("Service " + service + " has been blocked :)")
		yeet.run(['echo "Service '+service+' is blocked" >> log.txt'],shell=False)
	yeet.run(['echo "Services done just like ur mom" >> log.txt'],shell=False)
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#                                        MOVING ON TO USERS
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#user removal
users = input("Does a user need to be removed, fart sniffer? (y/n)")
if users == "y" or users == "Y":
    bump = 0
while bump == 0:
    x = input("Name of the user, idiot?")
    yeet.run(["userdel", x], shell=False)
    yeet.run(['echo "Omae wa mou shindeiru', x,'" >> log.txt'], shell=True)
    users = input("Does another user need to be removed, booger connoisseur? (y/n)")
    if users != "y" and users != "Y":
        bump = 1
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#                                        MOVING ON TO PACKAGES
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#package-removal
users = input("What  (y/n)")
if users == "y" or users == "Y":
    bump = 0
 
yeet.run([" cat > yeeters.txt"], shell=True)
yeet.run(["apt list --installed | less >> yeeters.txt"], shell=True)
yeet.run(["sendmail joshua.reddy@rocklinusd.org  < yeeters.txt"], shell=True)

while bump == 0:
    yeet.run(["apt-get --purge remove", input("Frickin Name of the package, bill?")], shell=False)
    
    #yeet.run(["Y")], shell=False)
    users = input("Does another fucker need to be removed,ass_man? (y/n)")
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
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#                                        MOVING ON TO ADMINS
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
if input("Does anyone need to be removed from admin permissions, dummy? (y/n)") == ("y" or "Y"):
    bump = 0
while bump == 0:
    yeet.run(["deluser", input("Name of the user, idiot?"), "sudo"], shell=False)
    users = input("Does anyone else need to be removed from admin permissions, Ivan? (y/n)")
    if users != "y" and users != "Y":
        bump = 1       
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#                                        MOVING ON TO GAME REMOVAL
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#***game removal
joe = input("Ok epic gamer, do you want me to delete gnome-games-common, aisleriot, sudoku, mahjongg, ace-of-penguins, gnomine, and gbrainy? (y/n)")
if joe == "y" or joe == "Y":
  yeet.run(["sudo apt-get purge gnome-games-common gbrainy && sudo apt-get autoremove"], shell=True)
  yeet.run(["sudo apt-get purge aisleriot gnome-sudoku mahjongg ace-of-penguins gnomine gbrainy"], shell=True)
joe = input("Any uncommon games to remove, my zooma? (y/n)")
if joe == "y" or joe == "Y":
  yeet.run(["sudo apt-get purge", input("What's the game package name, ear banger?")], shell=False)

#TODO
'''
#block ports ftp, vsftpd, --Jackson
#replacing files for pwd policies and ect --Aiden
    yeet.run(["cp -f [original file] [new file]"], shell=True) #change pass age/complexity in replacement file(s)
#automatic update stuffs --Aiden
    yeet.run(["apt-get install unattended-upgrades"], shell=True)
    yeet.run(["cp -f /etc/apt/apt.conf.d/10periodic [new file]"], shell=True) #change freq in replacement file
#ssh root login stuffs --Aiden
    yeet.run(["cp -f /etc/ssh/sshd_config [new file]"], shell=True) #change PermitRootLogin to no
#***application removal --Josh
    #write all packages to file
    #use sendmail to email file to off-image computer
    #https://tecadmin.net/ways-to-send-email-from-linux-command-line/
    #query for package purge
 #query for adding groups 
 #disable guest
 
'''
