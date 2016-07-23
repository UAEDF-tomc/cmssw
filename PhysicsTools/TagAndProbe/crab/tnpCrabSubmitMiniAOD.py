#!/usr/bin/env python
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
import os
os.system("eval `scramv1 runtime -sh`")

# Always first copy the latest version of the makeTree.py
import shutil
shutil.copyfile('../test/makeTree.py', 'makeTree.py')

config = config()

submitVersion = "80X_v12"

if os.environ["USER"] in ['tomc']:
  mainOutputDir = '/store/user/tomc/tnp/80X/%s' % submitVersion
  config.Site.storageSite = 'T2_BE_IIHE'
  config.User.voGroup = 'becms'
else:
  raise Exception('User settings not known')


config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'

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

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 5
    config.JobType.pyCfgParams  = ['isMC=True']
    config.JobType.allowUndistributedCMSSW = True 
    
    config.General.requestName  = 'DYToLL_mcAtNLO'
    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
    submit(config)

    config.General.requestName  = 'DYToLL_madgraph'
    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM'
    submit(config)

    config.General.requestName  = 'DYToLL_powheg'
    config.Data.inputDataset    = '/DYToEE_NNPDF30_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM'
    submit(config)

#    config.General.requestName  = 'WJets_madgraph'
#    config.Data.inputDataset    = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v2/MINIAODSIM'
#    submit(config)


 #   config.General.requestName  = 'ttbar_madgraph'
 #   config.Data.inputDataset    = '/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
 #   submit(config)


    ##### now submit DATA
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'data')
    config.Data.splitting     = 'LumiBased'
    config.Data.lumiMask      = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
    config.Data.unitsPerJob   = 50
    config.JobType.pyCfgParams  = ['isMC=False']

    config.General.requestName  = '2016_RunB'
    config.Data.inputDataset    = '/SingleElectron/Run2016B-PromptReco-v2/MINIAOD'
    submit(config)
