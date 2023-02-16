#!/usr/bin/python
delay=False
import shared_data
ipaddressdict={}

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for interface in data:
            print(interface)
            name = interface['friendly_name']
            address = interface['address']
            mask = interface['mask']
            atype = interface['type']
            if atype == "dhcp":
                ipaddressdict[name]={'address':address,'mask':mask}

shared_data.ipaddressdict=ipaddressdict
        
