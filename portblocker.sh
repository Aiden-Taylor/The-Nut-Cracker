#!/bin/bash

allunits() {
  blockports
  terminateservices
}
blockports() {
  maxcannotseethiscolor = 1
  while(($maxcannotseethiscolor = 1))
  do
    read -p "do you want to deport a port y/n" yn
    if (($yn = "y"))
    then
      read -p "port number you want gone" yeetport
      ufw block $yeetport
    else
      maxcannotseethiscolor = 0
    fi
  done
}
terminateservices() {
 maxisaverynicehumanbeingonoppisiteday = 1
 read -p "do you wan services listed, bubby?" goose
 if ((goose = "y"))
 then
  systemctl list-unit-files
 fi
 while (($maxcannotseethiscolor = 1))
 do
   read -p "eliminate services you dirty fucking good for nothing goddamn weeaboo" bep
   if (($bep = "y"))
   then
     read -p "service to go" servicething
     systemctl stop $servicething
     systemctl disable $servicething
     systemctl daemon-reload
     systemctl reset-failed
    else
     maxisaverynicehumanbeingonoppisiteday = 0
    fi
 done
}
