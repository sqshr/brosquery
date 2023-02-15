#!/usr/bin/python
import sys,os,argparse,json,re

parser = argparse.ArgumentParser(description='If you have Windows output on a Linux box, make sure to run "find . -type f -print0 | xargs -0 dos2unix" first.')
parser.add_argument('input', default='./', help='Directory containing osquery data.')
parser.add_argument('--ignore', help='Tables to ignore', nargs='+')
args = parser.parse_args()

ignored = args.ignore
print(ignored)
handlerdir = "./handlers/"
handlers = os.listdir(handlerdir)
sys.path.append(os.path.abspath(handlerdir))
import shared_data

tables = []
if os.path.isdir(args.input):
    tables = os.listdir(args.input)

#Gets the OS Information
def getos():
    f = open(os.path.join(args.input, "os_version.json"))
    content = f.read()
    f.close
    data = json.loads(content)[0]
    if re.search("Windows", data["codename"]):
        return("Windows")

detected_os = getos()
print(""" _                                               
| |__  _ __ ___  ___  __ _ _   _  ___ _ __ _   _ 
| '_ \| '__/ _ \/ __|/ _` | | | |/ _ \ '__| | | |
| |_) | | | (_) \__ \ (_| | |_| |  __/ |  | |_| |
|_.__/|_|  \___/|___/\__, |\__,_|\___|_|   \__, |
  osquery build reviews |_|   by sqshr     |___/ """)
print("[+] OS Detected as "+detected_os)


findings = {}
unhandledtables = []
delayed_handlers = {}
for table in tables:
    location = os.path.join(args.input, table)
    handlername = table.strip().removesuffix(".json")
    if handlername not in ignored and os.path.isfile(os.path.join(handlerdir,handlername+".py")):
        f = open(location, "r")
        content = f.read()
        f.close()
        data = json.loads(content)
        checker = __import__(handlername)
        if checker.delay:
            delayed_handlers[handlername] = data
        else:
            handlerfindings = checker.run(detected_os,data)
            if handlerfindings:
                for key,value in handlerfindings.items():
                    findings[handlername+"-"+key] = value

    else:
        unhandledtables.append(handlername)

for key in delayed_handlers.keys():
    handlername = key
    data = delayed_handlers[key]
    checker = __import__(handlername)
    handlerfindings = checker.run(detected_os,data)
    if handlerfindings:
        for key,value in handlerfindings.items():
            findings[handlername+"-"+key] = value



print("The following issues have been identified :")
for key, value in findings.items():
    print(key+"   -   "+value)
print("\n\n\n\n")
print("The following tables have not been handled, and should be manually reviewed: "+", ".join(unhandledtables))
