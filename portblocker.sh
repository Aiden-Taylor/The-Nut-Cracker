#!/bin/bash

allunits() {
  blockports
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
