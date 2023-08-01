#python test_dummy_list.py $CIRCLECI_USERNAME

import os
import sys

username = sys.argv[1]
sms = os.environ["User_List"].split(",")
if username in sms:
   print("Username " + username + " exists in sme list")
   sys.exit(0)
else:
   print("Username " + username + " DOES NOT exists in sme list")
   sys.exit(1)
