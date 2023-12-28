import os
import sys
username = os.environ.get("CIRCLE_USER").strip()  # Remove leading/trailing spaces
sms = [s.strip() for s in os.environ["USER_LIST"].split(",")]  # Remove leading/trailing spaces from each element 12345
print(username)
print(sms)

if username in sms:
   print("Username " + username + " exists in sme list")
   sys.exit(0)
else:
   print("Username " + username + " DOES NOT exists in sme list")
   sys.exit(1)
