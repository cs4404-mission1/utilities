import requests
import time
import random
usersf = open("userlist.txt","r").read()
users = usersf.splitlines()
while True:
    time.sleep(random.randrange(2,14))
    user,passwd = random.choice(users).split(":")
    postdata = {"ssn":user,"password":passwd}
    print("logging in as {} with password {}".format(user,passwd))
    requests.post("http://127.0.0.1:8000/login", data=postdata)
