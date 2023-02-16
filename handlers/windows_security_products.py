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
                if "Signatures Out of Date" not in findings.keys():
                    findings["Signatures Out of Date"] = []
                findings["Signatures Out of Date"].append(name)
            if state != "On":
                if "Feature Disabled" not in findings.keys():
                    findings["Feature Disabled"] = []
                findings["Feature Disabled"].append(name)


    return(findings)
        
