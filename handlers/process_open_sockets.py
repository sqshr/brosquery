#!/usr/bin/python
findings={}
delay=True
import shared_data, ipaddress
networks = []

def run(detected_os,data):
    if "windows" in detected_os.lower():
        for value in shared_data.ipaddressdict.values():
            ip = value['address']
            mask = value['mask']
            networks.append(ip+"/"+mask)
        for connection in data:
            destip = connection['remote_address']
            for network in networks:
                try:
                    if ipaddress.IPv4Address(destip) and ipaddress.IPv4Address(destip) in ipaddress.IPv4Network(network, False):
                        print("[!] Potential lateral movement detected from "+ip+" to "+destip)
                except:
                    pass

