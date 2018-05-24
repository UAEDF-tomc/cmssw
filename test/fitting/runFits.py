#!/usr/bin/env python
import os,glob,time,subprocess

def system(command):
  return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

def launch(command, logfile):
  try:    out = system("qsub -v dir=" + os.getcwd() + ",command=\"" + command + "\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=12:00:00 -l nodes=8 $CMSSW_BASE/src/MuonAnalysis/TagAndProbe/test/fitting/runFits.sh")
  except: out = 'failed'
  if not out.count('.cream02.iihe.ac.be'):
      print 'Submission failed: ' + out
      time.sleep(10)
      launch(command, logfile)


try:    os.makedirs('log')
except: pass

workingPoints = [('TTVLoose',           'None'),
                 ('TTVLeptonMvaTTZ4l',  'TTVLoose'),
                 ('TTVLeptonMvaTTZ3l',  'TTVLoose'),
                 ('TTVLeptonMvaTTW',    'TTVLoose'),
                 ('TTVLeptonMvatZq',    'TTVLoose'),
                 ('tkSigmaPtOverPtCut', 'TTVLeptonMvaTTW')]

for wp, ref in workingPoints:
  for year in ['2016', '2017']:
    for scenario in ['data', 'mc']:
      for binning in ['pt_eta', 'pt_vtx', 'pt_jets']:
        for sys in ['nominal', 'altMass1', 'altMass2', 'altTag1', 'altTag2', 'altShape'] if scenario=='data' else ['nominal', 'altMC']:
          command = 'cmsRun fitMuonID.py ' + ' '.join([wp, ref, scenario, year, binning, sys])
          if command != 'cmsRun fitMuonID.py TTVLeptonMvaTTZ3l TTVLoose data 2016 pt_jets altMass2': continue
          launch(command,  'log/' + '_'.join([wp, ref, scenario, year, binning, sys]) + '.log')
          print command
