#!/usr/bin/python
print("Handler for the uptime table")

findings={}

def run(detected_os,data):
    if int(data['days']) > 30:
        findings['uptime'] = "The uptime is greater than 30 days, patches may not be applied."


    return(findings)
        
