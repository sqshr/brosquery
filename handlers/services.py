#!/usr/bin/python
delay=False
findings={}
import os

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for service in data:
            path = os.path.normpath(service['path'])
            display_name = service['display_name']
            splitpath = os.path.splitext(path)
            checkpath = splitpath[0]
            if " " in checkpath and not checkpath.startswith('\"'):
                if "Unquoted Service Path" not in findings.keys():
                    findings["Unquoted Service Path"]=[]
                findings["Unquoted Service Path"].append(display_name)


    return(findings)
        
