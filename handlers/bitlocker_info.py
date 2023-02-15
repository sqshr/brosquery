#!/usr/bin/python
findings={}
delay=False

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for drive in data:
            global drive_letter
            drive_letter = drive['drive_letter']
            if drive['encryption_method'] == "None":
                findings["drive_unencrypted"] = "Drive "+drive_letter+" is not encrypted"


    return(findings)
        
