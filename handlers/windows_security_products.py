#!/usr/bin/python
delay=False
findings={}

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for product in data:
            name = product['name']
            signatures_up_to_date = product['signatures_up_to_date']
            state = product['state']
            if signatures_up_to_date != "1":
                findings[name+"-sigs"] = "The signatures for "+name+" are not up to date."
            if state != "On":
                findings[name+"-state"] = name+" is disabled."


    return(findings)
        
