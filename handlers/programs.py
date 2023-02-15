#!/usr/bin/python
import requests,json,urllib,os,ast
delay=False
findings={}
outofdate=[]
#
# Using this URL to try to version check all installed software: https://github.com/microsoft/winget-pkgs/issues/1646
#


def run(detected_os,data):
    global applist
    applist = {}
    if os.path.isfile("cache/applist.cache"):
        #print("Using cached applist file")
        f = open("cache/applist.cache","r")
        applist = ast.literal_eval(f.read())
        f.close()
    else:
        response = urllib.request.urlopen("https://api.github.com/repos/microsoft/winget-pkgs/git/trees/master")
        jsondata = json.loads(response.read())
        sha = ""
        for item in jsondata['tree']:
            if item['path'] == "manifests":
                shahash = item['sha']
        response = urllib.request.urlopen("https://api.github.com/repos/microsoft/winget-pkgs/git/trees/"+shahash+"?depth=1")
        applist = json.loads(response.read())['tree']
        f = open("cache/applist.cache","w")
        f.write(str(applist))
        f.close()

    #This will get the specific data for items beginning with a supplied character
    def getcache(firstchar):
        #print("[-] Getting cache for "+firstchar)
        letterlist = {}
        if os.path.isfile("cache/"+firstchar+".appcache"):
            #print("Using cached applist file")
            f = open("cache/"+firstchar+".appcache","r")
            letterlist = json.loads(str(f.read()))['tree']
        else:
            #print("[!] Getting new cache for "+firstchar)
            global applist
            for item in applist:
                name = item["path"]
                if name == firstchar:
                    url = item["url"]
                    response = urllib.request.urlopen(url+"?recursive=1")
                    letterlist = json.loads(response.read())
                    with open("cache/"+name+".appcache","w", encoding="utf-8") as f:
                        json.dump(letterlist,f)
                    f.close()
                    letterlist = letterlist['tree']
        return(letterlist)

    def getlatestversion(url):
        response = urllib.request.urlopen(url)
        versiondict = json.loads(response.read())['tree']
        versionlist = []
        for version in versiondict:
            versionlist.append(version['path'])
        return(str(versionlist[-1]))


    for program in data:
        name = program['name']
        publisher = program['publisher']
        #print("[+] Looking for app: "+name)
        version = program['version']
        possiblenames = []
        possiblenames.append(name.replace(" ",""))
        possiblenames.append(name.replace(" ","."))
        possiblenames.append(name.replace(" ","-"))
        possiblenames.append(name.replace(" ","_"))
        if publisher:
            checklist = getcache(publisher[0].lower())
        
        for app in checklist:
            fullname = app['path']
            name = app['path'].split("/")
            for possiblename in possiblenames:
                if len(name) == 2 and fullname.lower().find(possiblename.lower()):
                    latest = getlatestversion(app['url'])
                    if version != latest:
                        outofdate.append(name[1]+" is running at version "+version+". The latest is "+latest)
                    

    findings["outofdate"] = "\n".join(outofdate) 


    return(findings)
        
