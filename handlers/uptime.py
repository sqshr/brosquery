#!/usr/bin/python
print("Handler for the uptime table")

def run(detected_os,data):
    if int(data['days']) > 30:
        print("uptime bad")
    else:
        print("uptime good")
