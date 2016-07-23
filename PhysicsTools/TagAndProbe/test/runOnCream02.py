#!/usr/bin/env python
import os

import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--dryRun", action='store_true', default=False, help="dry run?")
argParser.add_argument("--step",   action='store',      default=0,     help="which step?")
args = argParser.parse_args()

#dataOrMC = "onlyMC=True"
def submitJobs(isData, extraParam = None):
  dataOrMC = "onlyData=True" if isData else "onlyMC=True"
  for jobId in range(28):
      logfile = "log/" + dataOrMC.split('=')[0].split('only')[-1] + "_" + ((extraParam + "_") if extraParam else "") + str(jobId) + ".log"
      command = "qsub -v command=\"cmsRun fitterSusy.py " + dataOrMC + " " + (extraParam if extraParam else "") + " jobId="+ str(jobId) +"\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=1:00:00 runFits.sh"
      if args.dryRun: print command
      else:           os.system(command)

# Before step 1: ./MCTemplates/runTemplates.py

if int(args.step) == 1:
  submitJobs(False)				# nominal MC
  submitJobs(True)				# nominal data

if int(args.step) == 2:
  submitJobs(False, "altMC=True")		# systematics
  submitJobs(True,  "altTag=True")
  submitJobs(True,  "altBkg=True")
  submitJobs(False, "altSig=0")                 # for altSig: first do MC

# Between step 2 and step3: ./MCTemplates/fixParamFromMCFit.py 

if int(args.step) == 3:
  submitJobs(True,  "altSig=0")                 # the altSig alternatives
  submitJobs(True,  "altSig=1")
  submitJobs(True,  "altSig=2")
  submitJobs(True,  "altSig=3")
