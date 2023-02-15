#!/usr/bin/python
delay=False
findings={}

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for key,value in data[0].items():
            if value != "Good":
                findings[key] = "The value for "+key+" was not reported as good by Windows Security Center"


    return(findings)
        
