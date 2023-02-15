#!/usr/bin/python
import shared_data
delay=False
groupdict={}

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for group in data:
            gid = group['gid']
            name = group['groupname']
            groupdict[gid] = name

shared_data.groupdict=groupdict
        
