import subprocess as yeet
kekel = input("You wan to do the upating thing you knuckle headed bufoon")
if kekel == "Y" or kekel == "y":
  yeet.run(["apt-get install unattended-upgrades"],shell=False)
  yeet.run(["sed -i '16,19d' /etc/apt/apt.conf.d/50unattended"],shell=True)
  yeet.run(["sed -i 's/[//  \"$]/   \"$/g' /etc/apt/apt.conf.d/50unattended"],shell=True)
  yeet.ru(["sed -i 's///g' /etc/apt/apt.conf.d/10period"],shell=True)
 
