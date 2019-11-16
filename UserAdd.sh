#!/usr/bin/env bash

#args: username, password

echo "Adding user $0 with pass $1"
egrep "^$0" /etc/passwd >/dev/null
pass=$(perl -e 'print crypt($ARGV[0], "password")' $1)
useradd -m -p $pass $0
[ $? -eq 0 ] && echo "$0 has been added to system!" || echo "Failed to add a user!"
