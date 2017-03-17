#!/usr/bin/env python

import sys
import glob
import subprocess
import json

solc = sys.argv[1]
report = open("report.txt", "w")

for f in sorted(glob.glob("*.sol")):
    proc = subprocess.Popen([solc, '--combined-json', 'bin', f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()
    try:
        result = json.loads(out.strip())
        for contractName in result['contracts'].keys():
            report.write(contractName + ' ' + result['contracts'][contractName]['bin'] + '\n')
    except:
        report.write(f + ": ERROR\n")
