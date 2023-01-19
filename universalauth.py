#!/usr/bin/env python3

import getpass
import bcrypt
import pwdtools
from pwdtools import bcolors

def msg(startColor, string, endColor=bcolors.ENDC):
  print(startColor + string + endColor)


def success():
    msg(bcolors.OKGREEN, 
        "\nSuccess!\n")
    return 0


def menue():
  msg(bcolors.OKCYAN,
        "What would you like to do?\n\n"
        "1. Set a new user\n"
        "2. Check password\n"
        "3. Exit password safe\n\n "
        "Please select either 1, 2 or 3: \n")


def write_user(password_file):
  username = input(bcolors.OKBLUE + "Please set your username: ").lower()
  userpass = pwdtools.linestripsplit(password_file, ":")

  if username in userpass:
    msg(bcolors.FAIL,
        "ERROR: USERNAME ALREADY IN DATABASE")
    return 1

  password = getpass.getpass(bcolors.OKBLUE + "Please set a password: ").encode("utf-8")
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  with open("password.txt", "ab") as fobj:
    fobj.write(f"{username}:{hashed}\n".encode("utf-8")) 
    return success()


def check_user(password_file):
  username = input(bcolors.OKBLUE + "Enter your username: " + bcolors.ENDC).lower()
  userpass = pwdtools.linestripsplit(password_file, ":")

  if not(username in userpass):
    msg(bcolors.FAIL, 
        "ERROR: USERNAME NOT IN DATABASE")
    return 1

  password = getpass.getpass(bcolors.OKBLUE + "Please enter your password: " + bcolors.ENDC).encode("utf-8")
  hashed = userpass[username].encode("utf-8")
  if bcrypt.checkpw(password, hashed):
    return success()

  msg(bcolors.FAIL, 
    "ERROR: WRONG PASSWORD")
  return 1


def main():
  state = 0

  password_file = "password.txt"
  pwdtools.check_create_file(password_file)

  while True:
    match state:
      case 0:
        menue()
        choice = input( )
        try:
            state = int(choice)
        except ValueError:
            state = choice
      case 1:
        print("Write user: ")
        write_user(password_file)
        state = 0
      case 2:        
        print("Check user: ")
        check_user(password_file)
        state = 0
      case 3:        
        print("Goodbye ... ")
        quit()      
      case _:
        print("Invalid choice")
        state = 0


if __name__ == "__main__":
  main()