#!/usr/bin/python
delay=False
import shared_data
userdict={}

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for user in data:
            uid = user['uid']
            name = user['username']
            userdict[uid] = name

shared_data.userdict=userdict
        
