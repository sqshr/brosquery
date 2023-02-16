#!/usr/bin/python
import shared_data
delay=False
processdict={}

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for process in data:
            cmdline = process['cmdline']
            pid = process['pid']
            uid = process['uid']
            processdict[pid]={'cmdline':cmdline,'uid':uid}

shared_data.processdict=processdict
        
