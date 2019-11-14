import subprocess as yeet
things = ["69","6660","6661","6662","6663","6664","6665","6666","6667","6668","6669","23","135","411","412","61","21","20","3389","25","139"]
kekel = input("Specifically block ports or just let the program go through its list ya weed smokin, cop shootin, bike stealin, watermelon munchin, finger lickin, white woman rapin, go for nothin respectable white person? (Y/N)")
if kekel == "Y":
	kekel = input("put in ports you want to block in format of     10,23,22,80... its pretty sad i need to explicitly state this, really goes to show the amount of brain cells you have")
	things = kekel.split(",")
for port in things:
	yeet.run(["iptables -A INPUT -p tcp --destination-port",port,"-j DROP"],shell=false)
	yeet.run(["iptables -A OUTPUT -p tcp --destination-port",port,"-j DROP"],shell=false)
	print("Port #" + port + " has been blocked :)")
kekel = input("Do you want to save changes across reboot? (Y/N)")
if kekel == "Y":
	yeet.run(["service iptables save"],shell=false)
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
#                                        MOVING ON TO SERVICES
#---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---=---
things = ["telnet","vsftpd","apache2"]
kekel = input("Specifically block services or just let the program go through its list ya weed smokin, cop shootin, bike stealin, watermelon munchin, finger lickin, white woman rapin, go for nothin respectable white person? (Y/N)")
if kekel == "Y":
	kekel = input("put in services you want to block in format of     telnet,ftp,service_name...")
	print("PS ur mom is a ho")
	things = kekel.split(",")
for service in things:
	yeet.run(["systemctl stop",service],shell=false)
	yeet.run(["systemctl disable",service],shell=false)
    yeet.run(["systemctl daemon-reload"],shell=false)
    yeet.run(["systemctl reset-failed"],shell=false)
	print("Service " + service + " has been blocked :)")
print("all done :)")
