import subprocess
import socket
import sys
from datetime import datetime

#Blank your screen

subprocess.call('clear', shell=True)

remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteserver)


