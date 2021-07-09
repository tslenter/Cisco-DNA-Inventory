#Import modules
import requests
import os
from requests.auth import HTTPBasicAuth
import urllib3
from prettytable import PrettyTable
import argparse

#Disable HTTPS validation
urllib3.disable_warnings()

#Set variables to None
hostname = None
username = None
password = None

#Global information
print("More information https://github.com/tslenter/Cisco-DNA-Inventory/ or https://www.remotesyslog.com/")
print('Running from directory: ', os.getcwd())

#Add arguments
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--hostname',  help='Enter a hostname or ip of the Cisco DNA Controller', required=True)
parser.add_argument('-u','--username', help='Add a username', required=True)
parser.add_argument('-p', '--password', help='Add a password', required=True)
args = parser.parse_args()

#Extract variables from namespace to global
globals().update(vars(args))

#Create table
dnac_devices = PrettyTable(['Hostname','Platform Id','Software Type','Software Version','Up Time', 'Serial Nu', 'MGMT IP' ])
dnac_devices.padding_width = 1

#Generate token for DNA Controller
def dnac_login(host, passwrd, user):
    # Generate token
    BASE_URL = 'https://' + host
    AUTH_URL = '/dna/system/api/v1/auth/token'
    USERNAME = user
    PASSWORD = passwrd

    response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
    token = response.json()['Token']
    return token

#Extract data from DNA controller
def network_device_list(token, host):
    url = "https://" + host + "/api/v1/network-device"
    headers["x-auth-token"] = token
    response = requests.get(url, headers=headers, verify=False)
    data = response.json()
    for item in data['response']:
        dnac_devices.add_row([item["hostname"],item["platformId"],item["softwareType"],item["softwareVersion"],item["upTime"], item["serialNumber"], item["managementIpAddress"]])

#Login to DNA Controller
if hostname or username or password != None:
    print("Started session on: " + hostname)
    print("Started session with user: " + username)
    login = dnac_login(hostname, password, username)
    network_device_list(login, hostname)
    print(dnac_devices)
else:
    print("Did you use the parameters to run this command?")
