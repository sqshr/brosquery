#!/usr/bin/python
delay=False
findings={}
import requests,os,csv
from io import StringIO
cache_file= "bad_domains.csv"
cache_path = "cache"

def run(detected_os,data):
    if os.path.isfile(os.path.join(cache_path,cache_file)):
        f = open(os.path.join(cache_path,cache_file), "r")
        baddomaincsv = f.read()
        f.close()
    else:
        baddomaincsv = requests.get("https://raw.githubusercontent.com/stamparm/blackbook/master/blackbook.csv").text
        f = open(os.path.join(cache_path,cache_file), "w")
        f.write(baddomaincsv)
        f.close()

    baddomainsdict = {}
    baddomainsdict = csv.DictReader(StringIO(baddomaincsv))

    cacheddomains = []
    baddomains = []
    for record in data:
        domain = record['name']
        cacheddomains.append(domain)
    for record in baddomainsdict:
        baddomain = record['Domain']
        baddomains.append(baddomain)
    
    for item in cacheddomains:
        if item in baddomains:
            issue_title = "Malware Domain in DNS Cache"
            if issue_title not in findings.keys():
                findings[issue_title] = []
            findings[issue_title].append(item)
    

    return(findings)
        
