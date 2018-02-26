#!/usr/bin/env python

import os, time
def launch(command, logfile, nodes=12):
    os.system("qsub -v dir=" + os.getcwd() + ",command=\"" + command + "\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=12:00:00 -l nodes=12 $CMSSW_BASE/src/MuonAnalysis/TagAndProbe/test/Fitting/runFits.sh &> .qsub.log")
    with open('.qsub.log','r') as qsublog:
      for l in qsublog:
        if 'Invalid credential' in l:
          time.sleep(10)
          launch(command, logfile)

try:    os.makedirs('log')
except: pass
for i in range(1, 8):
  launch('cmsRun fitMuonID.py data' + str(i), 'log/data_' + str(i) + '.log')
  launch('cmsRun fitMuonID.py mc' + str(i),   'log/mc_' + str(i) + '.log')
