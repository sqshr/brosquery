#!/usr/bin/python
import sys,os,argparse,json,re

parser = argparse.ArgumentParser(description='If you have Windows output on a Linux box, make sure to run "find . -type f -print0 | xargs -0 dos2unix" first.')
parser.add_argument('input', default='./', help='Directory containing osquery data.')
args = parser.parse_args()

handlerdir = "./handlers/"
handlers = os.listdir(handlerdir)
sys.path.append(os.path.abspath(handlerdir))

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
print("[+] OS Detected as "+detected_os)

for table in tables:
    location = os.path.join(args.input, table)
    handlername = table.strip().removesuffix(".json")
    if os.path.isfile(os.path.join(handlerdir,handlername+".py")):
        f = open(location, "r")
        content = f.read()
        f.close()
        data = json.loads(content)[0]
        print("[+] Parsing "+handlername)
        #imported = getattr(__import__(handlername, fromlist=["checks"]), "checks")
        checker = __import__(handlername)
        #checker.__dict__.update(data)
        checker.run(detected_os,data)

    else:
        print("[-] No handler found for "+handlername)

