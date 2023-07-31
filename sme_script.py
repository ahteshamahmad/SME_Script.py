#python test_dummy_list.py $CIRCLECI_USERNAME

import os
import sys

username = sys.argv[0]
sms = os.environ["smes"].split(",")

if username in sms:
   print("Username " + username + " exists in sme list")
else:
   print("Username " + username + " DOES NOT exists in sme list")
