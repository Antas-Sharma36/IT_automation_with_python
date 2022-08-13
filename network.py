#!/usr/bin/env python3

import requests
import socket

def check_localhost():
        localhost= socket.gethostbyname('localhost')
        #print("Localhost=",localhost)
        if (str(localhost) == "127.0.0.1"):
                return True
        else:
                #print("Oops")
                return False

def check_connectivity():
        request = requests.get("http://www.google.com")
        #print("REquest=",str(request))
        if str(request) == "<Response [200]>" :
                return True
        else:
                return False

