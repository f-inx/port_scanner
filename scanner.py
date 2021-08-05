#/bin/python3
# Goal to check port open or not

import sys
import socket
from datetime import datetime

#Define out target
if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) # TRanslate hostname to IPv4
else:
        print("Invalid amount of arguments.")
        print("SYntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
        for port in range(1,65535):
               s = socket.socket(soclet.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(1)
               result = s.connect_ex((target,port)) #return an error indicator
               if result == 0:
                       print("Port {} is open".format(port))
               s.close()
               
expect KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
 
 expect socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
        
 expect socket.error:
        print("Couldn't connect to server.")
        sys.exit()
     
