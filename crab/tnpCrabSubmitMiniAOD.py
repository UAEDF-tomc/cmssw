#!/usr/bin/env python
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
import os,time
os.system("eval `scramv1 runtime -sh`")

# Always first copy the latest version of the makeTree.py
import shutil
shutil.copyfile('../test/tp_from_aod_MC.py',   'tp_from_aod_MC.py')
shutil.copyfile('../test/tp_from_aod_Data.py', 'tp_from_aod_Data.py')

config = config()

submitVersion = "February2018_v2"

if os.environ["USER"] in ['tomc']:
  mainOutputDir           = os.path.join('/store/user/tomc/tnp_muons', submitVersion)
  config.Site.storageSite = 'T2_BE_IIHE'
  config.User.voGroup     = 'becms'
else:
  raise Exception('User settings not known')


config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = 'tp_from_aod_MC.py'
config.Data.allowNonValidInputDataset = False

config.Data.inputDBS = 'global'
config.Data.publication = False


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_projects_%s' % submitVersion

    def submit(config, requestName, inputDataset):
        config.General.requestName = requestName
        config.Data.inputDataset   = inputDataset
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)
        time.sleep(30)


    ##### submit MC
    config.Data.outLFNDirBase              = os.path.join(mainOutputDir, 'mc')
    config.Data.splitting                  = 'FileBased'
    config.Data.unitsPerJob                = 5
    config.JobType.sendExternalFolder      = True
    config.JobType.allowUndistributedCMSSW = True 
    
   # submit(config, 'DYToLL_mcAtNLO',           '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM')
   # submit(config, 'DYToLL_madgraph',          '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16reHLT80-PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext1-v1/AODSIM')

    ##### now submit DATA
    config.Data.outLFNDirBase  = os.path.join(mainOutputDir, 'data')
    config.Data.splitting      = 'LumiBased'
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.unitsPerJob    = 50
    config.JobType.psetName    = 'tp_from_aod_Data.py'

   # submit(config, 'Run2016B',    '/SingleMuon/Run2016B-23Sep2016-v3/AOD')
   # submit(config, 'Run2016C',    '/SingleMuon/Run2016C-23Sep2016-v1/AOD')
   # submit(config, 'Run2016D',    '/SingleMuon/Run2016D-23Sep2016-v1/AOD')
   # submit(config, 'Run2016E',    '/SingleMuon/Run2016E-23Sep2016-v1/AOD')
   # submit(config, 'Run2016F',    '/SingleMuon/Run2016F-23Sep2016-v1/AOD')
   # submit(config, 'Run2016G',    '/SingleMuon/Run2016G-23Sep2016-v1/AOD')
    submit(config, 'Run2016H-v2', '/SingleMuon/Run2016H-PromptReco-v2/AOD')
    submit(config, 'Run2016H-v3', '/SingleMuon/Run2016H-PromptReco-v3/AOD')


