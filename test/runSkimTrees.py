#!/usr/bin/env python




import os,glob,time

versionDir = '/pnfs/iihe/cms/store/user/tomc/tnp_muons/February2018_v2/'

samples = {'DY'      : 'mc/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/crab_DYToLL_mcAtNLO/*/*/*.root',
           'DY_LO'   : 'mc/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_DYToLL_madgraph/*/*/*.root',
           'runB'    : 'data/SingleMuon/crab_Run2016B/*/*/*.root',
           'runC'    : 'data/SingleMuon/crab_Run2016C/*/*/*.root',
           'runD'    : 'data/SingleMuon/crab_Run2016D/*/*/*.root',
           'runE'    : 'data/SingleMuon/crab_Run2016E/*/*/*.root',
           'runF'    : 'data/SingleMuon/crab_Run2016F/*/*/*.root',
           'runG'    : 'data/SingleMuon/crab_Run2016G/*/*/*.root',
           'runH-v2' : 'data/SingleMuon/crab_Run2016H-v2/*/*/*.root',
           'runH-v3' : 'data/SingleMuon/crab_Run2016H-v3/*/*/*.root'}


cut  = "tag_IsoMu24==1 && tag_combRelIsoPF04dBeta<0.2 && tag_pt>25 && pair_probeMultiplicity>0.5 && pair_probeMultiplicity<1.5 && pt>15 && abseta<2.4 && Loose==1 && abs(dB)<0.05 && abs(dzPV)<0.1 && abs(SIP)<8"
sel  = "mass pt eta abseta SIP dB dzPV combRelIsoPF03 segmentCompatibility JetNDauCharged miniIsoCharged miniIsoNeutrals miniIsoPUCharged miniIsoPhotons Loose Medium JetPtRel JetPtRatio JetBTagCSV tkSigmaPtOverPt tag_nVertices fixedGridRhoFastjetCentralNeutral pair_nJets30"


def launch(command, logfile):
    os.system("qsub -v dir=" + os.getcwd() + ",command=\"" + command + "\" -q localgrid@cream02 -o " + logfile + " -e " + logfile + " -l walltime=5:00:00 $CMSSW_BASE/src/MuonAnalysis/TagAndProbe/test/skimTnP.sh &> .qsub.log")
    with open('.qsub.log','r') as qsublog:
      for l in qsublog:
        if 'Invalid credential' in l:
          time.sleep(10)
          launch(command, logfile)


for sample, path in samples.iteritems():
  print versionDir + '/' + path
  inputFiles = glob.glob(versionDir + '/' + path)
  for inputFile in inputFiles:
    outFile = '/user/tomc/public/tagAndProbe/' + sample + '/' + inputFile.split('/')[-1]
    outTag  = outFile.replace('.root','')
    logFile = outFile.replace('.root','.log')
    try:    os.makedirs(os.path.dirname(logFile))
    except: pass
    command  = './skimTree ' + inputFile + ' ' + outFile + ' -d tpTree -t fitter_tree -c \'' + cut + '\' -r \'all\' -k \'' + sel + '\';'
    command  = '\\\"' + command + '\\\"'
    launch(command, logFile)
