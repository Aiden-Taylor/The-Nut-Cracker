#!/usr/bin/env bash
read -p "User to be removed? userrem
user_exists=$(getent passwd $userrem)
if [[ -z "$user_exists" ]]
then
       echo "User $userrem does not exist"
else
       userdel -rf "$userrem"
       echo "Omae wa mou shindeiru, motherfucker. I yeeted $userrem"
fi
[ $? -eq 0 ] && echo "$userrem has been removed from system!" || echo "Failed to remove a user!"
