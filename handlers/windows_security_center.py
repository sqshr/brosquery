#!/usr/bin/python
findings={}

def run(detected_os,data):
    for key,value in data[0].items():
        if value != "Good":
            findings[key] = "The value for "+key+" was not reported as good by Windows Security Center"


    return(findings)
        
