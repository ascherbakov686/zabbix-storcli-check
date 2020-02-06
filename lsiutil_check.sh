#!/bin/bash

a="$1,$2,$3,$4,$5,$6" #example string 21,3,1,0,0,0

r=$(sudo /usr/sbin/lsiutil -p 1 -a $a | grep State | cut -d ':' -f 2 |  tr -d '[:space:]'); if [[ "$r" == "optimal,enabled" ]]; then echo 0;else echo 1; fi;

