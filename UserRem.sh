#!/usr/bin/env bash
looop=1
while "$looop"; do
        read -p "User to be removed? userrem
        user_exists=$(getent passwd $userrem)
        if [[ -z "$user_exists" ]];
        then
                echo "User $userrem does not exist"
        else
                userdel -rf "$userrem"
                echo "Omae wa mou shindeiru, motherfucker. I yeeted $userrem"
        fi
        read -r "Remove another user y/n" next
        if [[ "$next" != "Y" ]] && [[ "$next != "y" ]];
        then
                looop=0
        fi
done
