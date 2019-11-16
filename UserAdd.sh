#!/usr/bin/env bash

#args: username, password
read -p "User name?" user
read -s -p "Password?" passw
echo "Adding user $user..."
egrep "^$user" /etc/passwd >/dev/null
pass=$(perl -e 'print crypt($ARGV[0], "password")' $passw)
useradd -m -p $pass $user
[ $? -eq 0 ] && echo "$user has been added to system!" || echo "Failed to add a user!"
