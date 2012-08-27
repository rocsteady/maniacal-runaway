#!/usr/local/bin/python
#Python program - needs more.
#Candace Cheney
import subprocess
import re

processes = subprocess.check_output ( ['ps','-ef'] )
lines = processes.split( '\n' )
for line in lines:
        process = re.split( '\s+', line )
        # process[0] is the user
        if process[0] == 'root':
                continue
        # TODO other filtering criteria here
        print line

