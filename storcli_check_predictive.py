#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import subprocess

def find_values(id, obj):
    results = []
    def _find_values(id, obj):
        try:
            for key, value in obj.iteritems():
                if key == id:
                    results.append(value)
                elif not isinstance(value, basestring):
                    _find_values(id, value)
        except AttributeError:
            pass

        try:
            for item in obj:
                if not isinstance(item, basestring):
                    _find_values(id, item)
        except TypeError:
            pass

    if not isinstance(obj, basestring):
        _find_values(id, obj)
    return results

try:
 json_data=subprocess.check_output('sudo /opt/MegaRAID/storcli/storcli64 /call /eall /sall show all J',shell=True)
 d = json.loads(str(json_data))
 print sum(find_values('Predictive Failure Count', d))

except: print 1


