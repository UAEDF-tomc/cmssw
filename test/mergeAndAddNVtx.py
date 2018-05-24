#!/usr/bin/env python




import os,glob,time

localDir = '/user/tomc/public/tagAndProbe2/'

samples = ['DY', 'runB', 'runC', 'runD' ,'runE', 'runF', 'runG', 'runH-v2', 'runH-v3']


def launch(command, logfile):
    if runLocal: os.system(command + ' &> ' + logfile + ' &')
    else:        os.system("qsub -v dir=" + os.getcwd() + ",command=\"" + command + "\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=5:00:00 $CMSSW_BASE/src/MuonAnalysis/TagAndProbe/test/skimTnP.sh &> .qsub.log")
    with open('.qsub.log','r') as qsublog:
      for l in qsublog:
        if 'Invalid credential' in l:
          time.sleep(10)
          launch(command, logfile, runLocal)


try:    os.makedirs(os.path.join(localDir, 'merged'))
except: pass
mydir = os.getcwd()
os.chdir(localDir)
for sample in samples:
  os.system('hadd -f merged/' + sample + '.root ' + sample + '/*withIsoAndMva.root')
os.chdir(mydir)

dataFiles = [os.path.join(localDir, 'merged', s + '.root') for s in samples if 'run' in s]
mcFile    = os.path.join(localDir, 'merged', 'DY.root')
mcFileNew = os.path.join(localDir, 'merged', 'DY_vtxWeighted.root')

command  = './addNVtxWeight \"' + ' '.join(dataFiles) + '\" ' + mcFile + ' ' + mcFileNew
os.system(command)

