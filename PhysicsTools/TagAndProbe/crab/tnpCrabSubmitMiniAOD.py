#!/usr/bin/env python
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
import os,time
os.system("eval `scramv1 runtime -sh`")

# Always first copy the latest version of the makeTree.py
import shutil
shutil.copyfile('../test/makeTree.py', 'makeTree.py')

config = config()

submitVersion = "Moriond2017_ttg3"

if os.environ["USER"] in ['tomc']:
  mainOutputDir           = os.path.join('/store/user/tomc/tnp', submitVersion)
  config.Site.storageSite = 'T2_BE_IIHE'
  config.User.voGroup     = 'becms'
else:
  raise Exception('User settings not known')


config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = 'makeTree.py'
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
    config.JobType.pyCfgParams             = ['isMC=True']
    config.JobType.sendExternalFolder      = True
    config.JobType.allowUndistributedCMSSW = True 
    
    submit(config, 'DYToLL_mcAtNLO',           '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv2-PUMoriond17_HCALDebug_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM')
#   submit(config, 'DYToLL_madgraph_herwigpp', '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-herwigpp_30M/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM')
    submit(config, 'DYToLL_madgraph',          '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM')
#   submit(config, 'DYToLL_powheg',   '/DYToEE_NNPDF30_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM')

    ##### now submit DATA
    config.Data.outLFNDirBase  = os.path.join(mainOutputDir, 'data')
    config.Data.splitting      = 'LumiBased'
    config.Data.lumiMask       = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
    config.Data.unitsPerJob    = 50
    config.JobType.pyCfgParams = ['isMC=False']

    submit(config, 'Run2016B-v1', '/SingleElectron/Run2016B-03Feb2017_ver1-v1/MINIAOD')
    submit(config, 'Run2016B-v2', '/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD')
    submit(config, 'Run2016C',    '/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD')
    submit(config, 'Run2016D',    '/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD')
    submit(config, 'Run2016E',    '/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD')
    submit(config, 'Run2016F',    '/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD')
    submit(config, 'Run2016G',    '/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD')
    submit(config, 'Run2016H-v2', '/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD')
    submit(config, 'Run2016H-v3', '/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD')


