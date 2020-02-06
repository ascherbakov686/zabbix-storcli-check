#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import subprocess

failed=0
pd_normalStates=['Onln','GHS','DHS','UGood']
vd_normalStates=['Optl']

try:
 json_data=subprocess.check_output('sudo /opt/MegaRAID/storcli/storcli64 /call show J',shell=True)
 d = json.loads(str(json_data))

 for di in d['Controllers']:
   resp = di['Response Data']

   for PD in resp['PD LIST']:
       if PD['State'] not in pd_normalStates: failed+=1

   for VD in resp['VD LIST']:
       if VD['State'] not in vd_normalStates: failed+=1

 print failed

except: print 1
