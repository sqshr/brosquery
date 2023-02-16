#!/usr/bin/python
findings={}
delay=True
import shared_data

def run(detected_os,data):
    ignore = ["::","127.0.0.1","::1"]
    if "windows" in detected_os.lower():
        print("[+] Listening Ports:")
        for listener in data:
            address = listener['address']
            port = listener['port']
            pid = listener['pid']
            cmdline = shared_data.processdict[pid]['cmdline']
            #cmdline=""
            if address not in ignore:
                  print(address+":"+port+" is running "+cmdline)
    


            




        
