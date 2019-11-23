#!/bin/bash
echo "Welcome to The Nut Cracker, an effort from the #1 most average team in Cyber Patriot"
echo "Brought to you by competitors from The Forbidden Burrito"
echo "Note: never use capital for yes or no questions, fatty"
echo "Question defaults to no with no input, dumb fu... dude."
echo "Please God tell me you've done the Forensics..."
read -p "Have you?" foren
if [$foren == "y"]
then
    echo "GOGOGO ALL UNITS IN TO DESTROY THEM COMMIES"
    echo "I mean... vulnerabilities"
    allunits
else
    echo "Nuking the vulnerabilities will probably give you no chance at the Forensics..."
    echo "Come back when you're done"
    exit
fi

allunits(){
    echo "Starting to yeet Cooper"
    useryeet
    userneet
    passhurl
    programyeet
    programneet
    exit
}

useryeet(){
    gogogo=1
    while [$gogogo == 1]
        read -p "Do you wanna yeet a user, fart sniffer?" yn
        if [$yn == "y"]
        then
            read -p "Who to remove?" yeet
            userdel $yeet
        else
            gogogo=0
        fi
    done
}

userneet(){
    gogogo=1
    while [$gogogo == 1]
        read -p "Do you wanna add a user, poop licker?" yn
        if [$yn == "y"]
        then
            read -p "Who to add?" add
            read -p -s "What password?" pass
            useradd -m -p $pass $add
        else
            gogogo=0
        fi
    done
}

passhurl(){
    gogogo=1
    while [$gogogo == 1]
        read -p "Would you like to change all of the user passwords?" yn
        if [$yn == "y"]
        then
            echo "Changing all passwords to !@mBatM@n!"
            many=cut -d: -f1 /etc/passwd | wc -l
            for i in many
            do
                #cut -d: -f1 /etc/passwd | cut -d: -f1 /etc/passwd | sed $i !d
            done
        else
             gogogo=0
        fi
    done
}

programyeet(){
    gogogo=1
    while [$gogogo == 1]
        read -p "Would you like to yeet programs, booger connoiseur?" yn
        if [$yn == "y"]
        then
            read -p "What program to remove?" progyeet
            apt-get purge -y $progyeet
        else
            gogogo=0
        fi
    done
}

programneet(){
    gogogo=1
    while [$gogogo == 1]
        read -p "Would you like to add programs, black hole... I mean... Josh?" yn
        if [$yn == "y"]
        then
            read -p "What program to add?" progadd
            apt-get install -y $progadd
        else
            gogogo=0
        fi
    done
}

gameyeet(){
    read -p "Would you like to automatically remove games, Ivan?" yn
    if [$yn == "y"]
    then
        apt-get purge -y gnome-games-common gbrainy
        apt-get purge -y aisleriot gnome-sudoku mahjongg ace-of-penguins gnomine gbrainy
        apt-get -y autoremove
        gogogo=1
        while [$gogogo == 1]
            read -p "Any uncommon games to remove, brickhead?" yn
            if [$yn == "y"]
            then
                read -p "What game to remove?" gmyeet
                apt-get purge -y $gmyeet
            else
                gogogo=0
            fi
        done
    else
        echo "Ok, you epic gamer"
    fi
}

upgradenoot() {
    read -p "Would you like to configure automatic upgrades?" yn
    if [$yn == "y"]
    then 
        apt-get install unatteneded-upgrades
        nano /etc/apt/apt.conf.d/50unattended-upgrades
        sed -i '/"${distro_id}:${distro_codename}-updates";/ c\"${distro_id}:${distro_codename}-updates";' /etc/apt/apt.conf.d/50unattended-upgrades
        echo 'APT::Periodic::Update-Package-Lists "1"; APT::Periodic::Download-Upgradeable-Packages "1"; APT::Periodic::AutocleanInterval "7"; APT::Periodic::Unattended-Upgrade "1";' > /etc/apt/apt.conf.d/20auto-upgrades
}
