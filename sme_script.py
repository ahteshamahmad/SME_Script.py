import os
import sys
username = os.environ["USER"]
sms = os.environ["USER_LIST"].split(",")
print(username)
print(sms)

if username in sms:
   print("Username " + username + " exists in sme list")
   sys.exit(0)
else:
   print("Username " + username + " DOES NOT exists in sme list")
   sys.exit(1)
