#python test_dummy_list.py $CIRCLECI_USERNAME

import os
import sys

username = sys.argv[1]
sms = os.environ["User_List"].split(",")
user_list = os.environ.get("User_List")
if not user_list:
    print("Error: User_List environment variable not set.")
    exit(1)
random_user = random.choice(sms)
if random_user in sms:
   print("Username " + random_user + " exists in sme list")
   sys.exit(0)
else:
   print("Username " + random_user + " DOES NOT exists in sme list")
   sys.exit(1)
