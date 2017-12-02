import getpass
import glob
import os
import hashlib
import binascii
import sys
import subprocess

"""
  Tool-Name      : Module Loader
  Tool Version   : V 0.10.3
  Python Version : 3.5.2
  Dev            : wyv3rn
  Data           : 2017-16-08
"""

# The Main Menue Function
def menue():
    while True:
        lowchoice = input("Enter Command: ")
        lowchoice.lower()
        if lowchoice == "start":
            Module_Loader()
        elif lowchoice == "exit":
            print("shutting down")
            break
        else:
            print("wrong command please Retype")

def menue2():
    while True:
        print("Enter help more Information")
        dragonstrorm = input("Enter Command : \n")
        dragonstrorm.lower()
        if dragonstrorm == "help":
            print("version-info = gets you the version of all Modules | ")
        elif dragonstrorm == "version-info":
            print("Module-Loader : V 0.10.3 \n)")
            print(":::::::::::::::::::::::::::::")
            print("Base-Char-System : IN DEV \n")
        else:
            print("Wrong Command retry please... ")

# Passphrase Check
def start():
    print("Sayris-AI - V 0.10.3 \n")
    while True:
        # Accept the passphrase and hash it.
        entered_password_hash = binascii.hexlify(
            hashlib.md5(getpass.getpass("Enter Passphrase: ").encode("utf-8")).digest())
        accepted_password = True

        # Process all hashes and break if a password is valid.
        with open("keyframe.txt", "r", encoding="utf-8") as handle:
            for current_hash in handle:
                current_hash = bytes(current_hash.rstrip('\n').encode("utf-8"))

                if current_hash == entered_password_hash:
                    break
            else:
                accepted_password = False

        # Handle the auth result.
        if accepted_password:
            print("Accepted.")
            menue()
        else:
            print("Unauthorized access.")


# Main Module_Loader / Module Starter
def Module_Loader():
    print("Start Modul-Loader \n")
    # Searches the ./Modules folder for .py files
    enter = input("\nSStart All Modules where will be found ?")
    if enter == "yes":
        os.chdir("./Modules")
        for file in glob.glob("*.py"):
            print("/Modules " + file)
        # Start all Found .py Modules in Seperate Terminals
        for founded_modules in glob.glob("*.py"):
            pathofmod = os.getcwd()
            print("Start Modul : " + founded_modules + "\n")
			# Enter Python Version in python without 3 for python2 starts
            subprocess.Popen('xterm -hold -e python3 ' + pathofmod + '/' + founded_modules, shell=True)     
        menue2()

# Goes Back to Main Menue
    elif enter == "no":
        print("Go Back to Menue...")
        menue()
    else:
        print("retry enter")
start()
