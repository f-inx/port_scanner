# port_scanner
Shows what port opens on the IP

[The scripts explanation]

- Define target

→ this if else block checks whether or not the sys.argv[1] i.e. [scanner.py](http://scanner.py) (sys.argv[0]) <ip/website> (sys.argv[1]) is an ip or a website

→ If IP Address just move on to the port scan part, if website name it will translate it to IP address

→ Else we print out error message


- Add pretty banner show IP target and time

→ just showing target IP Address and time start scan


- Basic mechanism of the port scan

→ This for loop scans from port 1 to 65535

→ If the port open, it shows the confirmation message


- Error handling for port scan

→ First error is for keyboard interrupt i.e. exiting process with ctrl + c.

→ Second error is for where the website name not available IP

→ Third error if you don't have Internet
