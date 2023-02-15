#!/usr/bin/python
delay=False
findings={}

def run(detected_os,data):
    if int(data[0]['days']) > 30:
        findings['uptime'] = "The uptime is greater than 30 days, patches may not be applied."


    return(findings)
        
