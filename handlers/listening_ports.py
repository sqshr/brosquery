#!/usr/bin/python
findings={}
delay=True
import shared_data

def run(detected_os,data):
    shared_data.report['Listening Sockets']=[]
    ignore = ["::","127.0.0.1","::1"]
    if "windows" in detected_os.lower():
        for listener in data:
            address = listener['address']
            port = listener['port']
            pid = listener['pid']
            cmdline = shared_data.processdict[pid]['cmdline']
            #cmdline=""
            if address not in ignore:
                shared_data.report['Listening Sockets'].append(address+":"+port+" is running "+cmdline)
    


            




        
