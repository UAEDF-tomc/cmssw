#!/usr/bin/env python

import os, time
def launch(command, logfile, nodes=12):
    os.system("qsub -v dir=" + os.getcwd() + ",command=\"" + command + "\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=12:00:00 -l nodes=8 $CMSSW_BASE/src/MuonAnalysis/TagAndProbe/test/Fitting/runFits.sh &> .qsub.log")
    with open('.qsub.log','r') as qsublog:
      for l in qsublog:
        if 'Invalid credential' in l:
          time.sleep(10)
          launch(command, logfile)

try:    os.makedirs('log')
except: pass
for j in range(1, 4):
  for i in range(1, 8):
    launch('cmsRun fitMuonID.py data ' + str(i) + ' ' + str(j), 'log/data_' + str(i) + '_' + str(j) + '.log')
    launch('cmsRun fitMuonID.py mc ' + str(i) + ' ' + str(j),   'log/mc_' + str(i) + '_' + str(j) + '.log')
