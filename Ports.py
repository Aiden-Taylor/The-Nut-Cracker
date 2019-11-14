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
