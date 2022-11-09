#!/usr/bin/python3
import requests
import time
import random
usersf = open("userlist.txt","r").read()
users = usersf.splitlines()
while True:
    user,passwd = random.choice(users).split(":")
    postdata = {"ssn":user,"password":passwd}
    print("logging in with SSN {} and password {}".format(user,passwd))
    requests.post("https://api.internal/login", data=postdata, verify=False)
    time.sleep(random.randrange(2,14))
