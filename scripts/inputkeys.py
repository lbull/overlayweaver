#!/usr/bin/python
import getpass
import sys
import telnetlib

if (len(sys.argv) != 2):
  print "usage: \n " + sys.argv[0] + " <port>"
  sys.exit(-1)

HOST = "bull-labs.com"
port = sys.argv[1]
#user = raw_input("Enter your remote account: ")
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST, port)

#tn.read_until("login: ")
#tn.write(user + "\n")
#if password:
#    tn.read_until("Password: ")
#    tn.write(password + "\n")

for i in range(10000):
  tn.write("put key" + str(i) + " value" + str(i) + "\n")

tn.write("get -status key9000\n")  
tn.write("quit\n")

print tn.read_all() 
