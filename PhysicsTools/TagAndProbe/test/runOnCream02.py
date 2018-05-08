#!/usr/bin/env python
import os, time

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--runLocal", action='store_true', default=False, help="run local?")
argParser.add_argument("--dryRun",   action='store_true', default=False, help="dry run?")
argParser.add_argument("--step",     action='store',      default=0,     help="which step?")
args = argParser.parse_args()


def launch(command, logfile):
  if args.runLocal:
    print command
    os.system(command + ' &> ' + logfile + ' &')
  else:
    os.system("qsub -v command=\"" + command + "\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=4:00:00 runFits.sh &> .qsub.log")
    with open('.qsub.log','r') as qsublog:
      for l in qsublog:
        if 'Invalid credential' in l:
          time.sleep(10)
          launch(command, logfile)


options = [
           ['is2016=False', 'useJets=False', 'usePV=False'],
           ['is2016=False', 'useJets=True',  'usePV=False'],
           ['is2016=False', 'useJets=False', 'usePV=True'],
           ['is2016=True',  'useJets=False', 'usePV=False'],
           ['is2016=True',  'useJets=True',  'usePV=False'],
           ['is2016=True',  'useJets=False', 'usePV=True']
           ]

def submitJobs(isData, extraParam = None):
  for option in options:
    logDir = 'log/'+ ''.join(option)+'/'
    try:    os.makedirs(logDir)
    except: pass

    dataOrMC = "onlyData=True" if isData else "onlyMC=True"
    for jobId in range(6):
        logfile = logDir + dataOrMC.split('=')[0].split('only')[-1] + "_" + ((extraParam + "_") if extraParam else "") + str(jobId) + ".log"
        command = "cmsRun fitterTTV.py " + dataOrMC + " " + (extraParam if extraParam else "") + " jobId="+ str(jobId) + ' ' + ' '.join(option)
        if args.dryRun:  print command
        else:            launch(command, logfile)
        time.sleep(1)

# Before step 1: ./MCTemplates/runTemplates.py

if int(args.step) == 1:
  submitJobs(False)				# nominal MC
  submitJobs(False, "altMC=True")		# systematics
  submitJobs(True,  "altBkg=0")
  submitJobs(True,  "altBkg=1")
  submitJobs(True,  "altBkg=2")

# Steps which might need to be repeated for failed fits
if int(args.step) == 2:
  submitJobs(True)				# nominal data
  submitJobs(True,  "altTag=True")
  submitJobs(False, "altSig=0")                 # for altSig: first do MC

# Between step 2 and step3: ./MCTemplates/fixParamFromMCFit.py 

if int(args.step) == 3:
  submitJobs(True,  "altSig=0")                 # the altSig alternatives
  submitJobs(True,  "altSig=1")
  submitJobs(True,  "altSig=2")
  submitJobs(True,  "altSig=3")
