import requests
import time
import random
usersf = open("userlist.txt","r").read()
users = usersf.splitlines()
while True:
    user,passwd = random.choice(users).split(":")
    postdata = {"ssn":user,"password":passwd}
    print("logging in as {} with password {}".format(user,passwd))
    requests.post("https://api.internal/login", data=postdata)
    time.sleep(random.randrange(2,14))
