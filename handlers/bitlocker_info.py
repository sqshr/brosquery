#!/usr/bin/python
findings={}
delay=False

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for drive in data:
            global drive_letter
            drive_letter = drive['drive_letter']
            if drive['encryption_method'] == "None":
                issue_title = "Unencrypted Drive"
                if issue_title not in findings.keys():
                    findings[issue_title] = []
                findings[issue_title].append(drive_letter)


    return(findings)
        
