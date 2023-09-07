import os
import sys
username = os.environ.get("USER")
sms = os.environ["USER_LIST"].split(",")

if username in sms:
   print("Username " + username + " exists in sme list")
   sys.exit(0)
else:
   print("Username " + username + " DOES NOT exists in sme list")
   sys.exit(1)
