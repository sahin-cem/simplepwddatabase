#!/usr/bin/env python

import getpass
import bcrypt
import os
import pwdtools
from pwdtools import bcolors


if not os.path.exists("password.txt"):
    with open("password.txt", "wb"): 
        pass


userpass = pwdtools.linestripsplit("password.txt", ":")

choice = None


def main():
    global choice
    while type(choice) != int:
        choice = input(bcolors.OKCYAN + "What would you like to do?\n\n1. Set a new user\n2. Check password\n____________________\n\n Please select either 1 or 2: " + bcolors.ENDC)
        try:
            choice = int(choice)
            break
        except ValueError:
            print(bcolors.WARNING + "\nError: Please select either 1 or 2: \n" + bcolors.ENDC)
            continue
    return choice


def success():
    print(bcolors.OKGREEN + "Success!\n" + bcolors.ENDC)




def write_user():
    while True:
        username = input(bcolors.OKBLUE + "Please set your username: " + bcolors.ENDC).lower()
        if username in userpass:
            print(bcolors.FAIL + "Error: Username already in Database!\n" + bcolors.ENDC)
            continue
        else:
            password = getpass.getpass(bcolors.OKBLUE + "Please set a password: " + bcolors.ENDC).encode("utf-8") #userinput string which isnt shown, encoded to hash the pwd
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            with open("password.txt", "ab") as fobj: #open a file with write and byte parameters
                fobj.write("{}:{}\n".format(username, hashed).encode("utf-8")) #write a line into the file and encode it
                success()
                break


def check_user():
    while True:
        username = input(bcolors.OKBLUE + "Enter your username: " + bcolors.ENDC).lower()
        if username in userpass:
            password = getpass.getpass(bcolors.OKBLUE + "Please enter your password: " + bcolors.ENDC).encode("utf-8")
            hashed = userpass[username].encode("utf-8")
            if bcrypt.checkpw(password, hashed):
                success()
                break
            else:
                print(bcolors.FAIL + "Wrong password!\n" + bcolors.ENDC)
                quit()
        else:
            print(bcolors.WARNING + "Username not in database, try again." + bcolors.ENDC)
            continue


main()

if choice == 1:
    write_user()

if choice == 2:
    check_user()
