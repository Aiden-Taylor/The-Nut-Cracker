#!/usr/bin/env python
#removing games
import subprocess as yeet
joe = input("Ok epic gamer, do you want me to delete gnome-games-common, aisleriot, sudoku, mahjongg, ace-of-penguins, gnomine, and gbrainy? (y/n)")
if joe = "y" or joe = "Y":
  yeet.run(["sudo apt-get purge gnome-games-common gbrainy && sudo apt-get autoremove"], shell=True)
  yeet.run(["sudo apt-get purge aisleriot gnome-sudoku mahjongg ace-of-penguins gnomine gbrainy"], shell=True)
joe = input("Any uncommon games to remove, my zooma? (y/n)")
if joe = "y" or joe = "Y":
  yeet.run(["sudo apt-get purge", input("What's the game package name, ear banger?")], shell=False)
