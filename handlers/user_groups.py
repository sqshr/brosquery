#!/usr/bin/python
findings={}
delay=True
import shared_data

def run(detected_os,data):
    if "windows" in detected_os.lower():
        group_memberships = {}
        #shared_data.userdict
        #shared_data.groupdict
        for line in data:
            uid = line['uid']
            gid = line['gid']
            username = shared_data.userdict[uid]
            groupname = shared_data.groupdict[gid]
            if gid not in group_memberships.keys():
               group_memberships[gid]=[]
            group_memberships[gid].append(uid)
    
    print("[+] Group Memberships")
    for gid in group_memberships.keys():
        groupname = shared_data.groupdict[gid]
        userlist = group_memberships[gid]
        usernames = []
        for uid in userlist:
            username = shared_data.userdict[uid]
            usernames.append(username)

        print(groupname+": "+', '.join(usernames))


            




        
