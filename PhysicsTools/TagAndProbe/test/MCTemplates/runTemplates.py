#! /usr/bin/env python
import getTemplatesFromMC
import makeConfigForTemplates
import os, glob

tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')
templateProduction = "templatesSusy"
try:
  os.makedirs(os.path.join(tnpPackage, 'data', templateProduction))
except:
  pass

failedFits = ["CutBasedStopsDileptonToRelIso012_barrel_10p0To20p0_0p0To0p8",
              "CutBasedStopsDileptonToRelIso012_crack_10p0To20p0_1p442To1p566",
              "CutBasedStopsDileptonToRelIso012_endcap_10p0To20p0_1p566To2p0",
              "CutBasedStopsDileptonToRelIso012_barrel_20p0To35p0_0p0To0p8",
              "CutBasedStopsDileptonToRelIso012_barrel_20p0To35p0_0p8To1p442",
              "CutBasedStopsDileptonToRelIso012_crack_20p0To35p0_1p442To1p566",
              "CutBasedStopsDileptonToRelIso012_endcap_20p0To35p0_1p566To2p0",
              "CutBasedStopsDileptonToRelIso012_endcap_20p0To35p0_2p0To2p5",
              "CutBasedStopsDileptonToRelIso012_barrel_35p0To50p0_0p0To0p8",
              "CutBasedStopsDileptonToRelIso012_barrel_35p0To50p0_0p8To1p442",
              "CutBasedStopsDileptonToRelIso012_crack_35p0To50p0_1p442To1p566",
              "CutBasedStopsDileptonToRelIso012_crack_35p0To50p0_1p442To1p566",
              "CutBasedStopsDileptonToRelIso012_barrel_50p0To100p0_0p0To0p8",
              "CutBasedStopsDileptonToRelIso012_barrel_50p0To100p0_0p8To1p442",
              "CutBasedStopsDileptonToRelIso012_barrel_100p0To200p0_0p0To0p8",
              "CutBasedStopsDileptonToRelIso012_barrel_100p0To200p0_0p8To1p442",
              "CutBasedStopsDileptonToRelIso012_crack_100p0To200p0_1p442To1p566",
              "CutBasedStopsDileptonToRelIso012_endcap_200p0To500p0_1p566To2p0",
              "GsfElectronToCutBasedSpring15L_crack_10p0To20p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15L_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15L_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15L_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15L_endcap_20p0To35p0_1p566To2p0",
              "GsfElectronToCutBasedSpring15L_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15L_barrel_35p0To50p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15L_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15L_barrel_50p0To100p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15L_crack_100p0To200p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15M_crack_10p0To20p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15M_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15M_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15M_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15M_endcap_20p0To35p0_1p566To2p0",
              "GsfElectronToCutBasedSpring15M_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15M_barrel_35p0To50p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15M_barrel_35p0To50p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15M_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15M_barrel_50p0To100p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15M_crack_100p0To200p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15T_crack_10p0To20p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15T_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15T_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15T_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15T_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15T_barrel_35p0To50p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15T_barrel_35p0To50p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15T_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15T_barrel_50p0To100p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15T_crack_100p0To200p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15T_barrel_200p0To500p0_0p0To0p8",
              "GsfElectronToCutBasedSpring15T_barrel_200p0To500p0_0p8To1p442",
              "GsfElectronToCutBasedSpring15T_endcap_200p0To500p0_1p566To2p0",
              "GsfElectronToCutBasedSpring15V_crack_10p0To20p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15V_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToCutBasedSpring15V_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToCutBasedSpring15V_endcap_20p0To35p0_1p566To2p0",
              "GsfElectronToCutBasedSpring15V_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToCutBasedStopsDilepton_crack_10p0To20p0_1p442To1p566",
              "GsfElectronToCutBasedStopsDilepton_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToCutBasedStopsDilepton_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToCutBasedStopsDilepton_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToCutBasedStopsDilepton_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToCutBasedStopsDilepton_barrel_35p0To50p0_0p0To0p8",
              "GsfElectronToCutBasedStopsDilepton_barrel_35p0To50p0_0p8To1p442",
              "GsfElectronToCutBasedStopsDilepton_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_endcap_20p0To35p0_1p566To2p0",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8mini04_barrel_200p0To500p0_0p0To0p8",
              "GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04_crack_10p0To20p0_1p442To1p566",
              "GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8mini04_barrel_200p0To500p0_0p0To0p8",
              "GsfElectronToMVATightIDEmuTightIP2DSIP3D4_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToMVATightIDEmuTightIP2DSIP3D4_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToMVATightIDEmuTightIP2DSIP3D4_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToMVATightIDEmuTightIP2DSIP3D4_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToMVATightIDEmuTightIP2DSIP3D4_barrel_200p0To500p0_0p0To0p8",
              "GsfElectronToMVATightTightIP2DSIP3D4_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToMVATightTightIP2DSIP3D4_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToMVATightTightIP2DSIP3D4_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToMVATightTightIP2DSIP3D4_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToMVAVLooseFOIDEmuTightIP2D_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToMVAVLooseFOIDEmuTightIP2D_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToMVAVLooseFOIDEmuTightIP2D_barrel_50p0To100p0_0p0To0p8",
              "GsfElectronToMVAVLooseTightIP2D_endcap_10p0To20p0_2p0To2p5",
              "GsfElectronToMVAVLooseTightIP2D_barrel_20p0To35p0_0p0To0p8",
              "GsfElectronToMVAVLooseTightIP2D_crack_20p0To35p0_1p442To1p566",
              "GsfElectronToMVAVLooseTightIP2D_endcap_20p0To35p0_2p0To2p5",
              "GsfElectronToMVAVLooseTightIP2D_barrel_50p0To100p0_0p0To0p8",
              "MVATightConvIHit0ElectronToCharge_barrel_20p0To35p0_0p0To0p8",
              "TightConvIHit0ElectronToCharge_barrel_35p0To50p0_0p8To1p442",
              "MVATightElectronToConvVetoIHit0_barrel_20p0To35p0_0p0To0p8",
              "MVATightElectronToConvVetoIHit0_barrel_50p0To100p0_0p0To0p8",
              "MVATightElectronToMultiIsoM_barrel_20p0To35p0_0p0To0p8",
              "MVATightElectronToMultiIsoM_barrel_20p0To35p0_0p8To1p442",
              "MVATightElectronToMultiIsoM_crack_20p0To35p0_1p442To1p566",
              "MVATightElectronToMultiIsoM_endcap_20p0To35p0_1p566To2p0",
              "MVATightElectronToMultiIsoM_barrel_35p0To50p0_0p0To0p8",
              "MVATightElectronToMultiIsoM_barrel_35p0To50p0_0p8To1p442",
              "MVATightElectronToMultiIsoM_barrel_50p0To100p0_0p0To0p8",
              "MVATightElectronToMultiIsoT_barrel_20p0To35p0_0p0To0p8",
              "MVATightElectronToMultiIsoT_barrel_50p0To100p0_0p0To0p8",
              "MVATightElectronToMultiIsoT_barrel_50p0To100p0_0p8To1p442",
              "MVATightElectronToMultiIsoTISOEmu_barrel_20p0To35p0_0p0To0p8",
              "MVATightElectronToMultiIsoTISOEmu_barrel_50p0To100p0_0p0To0p8",
              "MVAVLooseElectronToConvVetoIHit1_barrel_10p0To20p0_0p0To0p8",
              "MVAVLooseElectronToConvVetoIHit1_crack_10p0To20p0_1p442To1p566",
              "MVAVLooseElectronToConvVetoIHit1_endcap_10p0To20p0_1p566To2p0",
              "MVAVLooseElectronToConvVetoIHit1_barrel_20p0To35p0_0p0To0p8",
              "MVAVLooseElectronToConvVetoIHit1_crack_20p0To35p0_1p442To1p566",
              "MVAVLooseElectronToConvVetoIHit1_barrel_50p0To100p0_0p0To0p8",
              "MVAVLooseElectronToMini2_barrel_20p0To35p0_0p0To0p8",
              "MVAVLooseElectronToMini2_crack_20p0To35p0_1p442To1p566",
              "MVAVLooseElectronToMini2_endcap_20p0To35p0_1p566To2p0",
              "MVAVLooseElectronToMini2_endcap_20p0To35p0_2p0To2p5",
              "MVAVLooseElectronToMini2_barrel_35p0To50p0_0p0To0p8",
              "MVAVLooseElectronToMini2_barrel_50p0To100p0_0p0To0p8",
              "MVAVLooseElectronToMini2_barrel_50p0To100p0_0p8To1p442",
              "MVAVLooseElectronToMini2_crack_100p0To200p0_1p442To1p566",
              "MVAVLooseElectronToMini2_endcap_100p0To200p0_2p0To2p5",
              "MVAVLooseElectronToMini2_endcap_200p0To500p0_2p0To2p5",
              "MVAVLooseElectronToMini4_barrel_20p0To35p0_0p0To0p8",
              "MVAVLooseElectronToMini4_endcap_20p0To35p0_1p566To2p0",
              "MVAVLooseElectronToMini4_barrel_50p0To100p0_0p8To1p442",
              "MVAVLooseElectronToMini4_crack_100p0To200p0_1p442To1p566",
              "MVAVLooseElectronToMini4_endcap_100p0To200p0_1p566To2p0",
              "MVAVLooseElectronToMini4_endcap_100p0To200p0_2p0To2p5",
              "MVAVLooseElectronToMini_barrel_20p0To35p0_0p0To0p8",
              "MVAVLooseElectronToMini_crack_20p0To35p0_1p442To1p566",
              "MVAVLooseElectronToMini_barrel_50p0To100p0_0p0To0p8",
              "MVAVLooseElectronToMini_endcap_200p0To500p0_1p566To2p0"
              ]
failedFitsAltSig = []

def getIdLabel(args):
    idProbe, directory, region = args
    return directory.split('To')[0] + 'To' + idProbe + "_" + region


class options:
    input           = os.path.join(tnpPackage, 'crab', 'crab_projects_Moriond2017_v3', 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-herwigpp_30M.root')
    output          = "mc_templates.root"
    directory       = "GsfElectronToID"
    idprobe         = "passingMedium"
    var1Bins        = "10,20,35,50,100,200,500"
    var2Bins        = "0.0,0.8,1.4442,1.566,2.0,2.5"
    var1Name        = "probe_Ele_pt"
    var2Name        = "probe_sc_abseta"
    addProbeCut     = ""
    weightVarName   = "totWeight"
    tagTauVarName   = "" # "tag_Ele_dRTau"
    probeTauVarName = "" # "probe_dRTau
    idLabel         = ""
    failBkgPdf      = "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])"
    passBkgPdf      = "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])"
    altSig          = False

def runGetTemplatesFromMC(args):
    idProbe, directory, region = args

    myOptions = options()

    if region == "alleta":     options.var2Bins = "0,2.5"
    if region == "barrel":     options.var2Bins = "0,0.8,1.442"
    if region == "crack":      options.var2Bins = "1.442,1.566"
    if region == "endcap":     options.var2Bins = "1.566,2.0,2.5"

    myOptions.idLabel      = getIdLabel(args)
    myOptions.output       = os.path.join(tnpPackage, 'data', templateProduction, myOptions.idLabel + ".root")
    myOptions.directory    = directory
    myOptions.idprobe      = "passing" + idProbe
    getTemplatesFromMC.main(myOptions)

    myOptions.outputFile   = os.path.join(tnpPackage, 'python', "nominalFit_" + myOptions.idLabel + ".py")
    myOptions.templateFile = myOptions.output

    # Manual fix to avoid failed fits, we take a slightly different parameter
    if myOptions.idLabel in failedFits:
      myOptions.failBkgPdf = "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.02, 0, 1], peakFail[90.0, 70, 80])"
      myOptions.passBkgPdf = "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.02, 0, 1], peakPass[90.0, 70, 80])"

    makeConfigForTemplates.main(myOptions)

    # Also manual fix in the altSig MC case
    if myOptions.idLabel in failedFitsAltSig:
      myOptions.failBkgPdf = "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.02, 0, 1], peakFail[90.0, 70, 80])"
      myOptions.passBkgPdf = "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.02, 0, 1], peakPass[90.0, 70, 80])"

    myOptions.altSig       = True  # Also make templates for MC to be used for the altSig systematic
    myOptions.outputFile   = os.path.join(tnpPackage, 'python', "altSigFit_" + myOptions.idLabel + ".py")
    makeConfigForTemplates.main(myOptions)
    

jobs = []
for region in ["alleta","barrel","crack","endcap"]:
  jobs.append(("CutBasedSpring15V",                               "GsfElectronToID",                region))
  jobs.append(("CutBasedSpring15L",                               "GsfElectronToID",                region))
  jobs.append(("CutBasedSpring15M",                               "GsfElectronToID",                region))
  jobs.append(("CutBasedSpring15T",                               "GsfElectronToID",                region))
  jobs.append(("MVAVLooseTightIP2D",                              "GsfElectronToID",                region))
  jobs.append(("MVAVLooseFOIDEmuTightIP2D",                       "GsfElectronToID",                region))
  jobs.append(("MVATightTightIP2DSIP3D4",                         "GsfElectronToID",                region))
  jobs.append(("MVATightIDEmuTightIP2DSIP3D4",                    "GsfElectronToID",                region))
  jobs.append(("CutBasedStopsDilepton",                           "GsfElectronToID",                region))
  jobs.append(("LeptonMvaVTIDEmuTightIP2DSIP3D8mini04",           "GsfElectronToID",                region))
  jobs.append(("LeptonMvaMIDEmuTightIP2DSIP3D8mini04",            "GsfElectronToID",                region))

  jobs.append(("Mini",                                            "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini2",                                           "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini4",                                           "MVAVLooseElectronToIso",         region))
  jobs.append(("ConvVetoIHit1",                                   "MVAVLooseElectronToIso",         region))

  jobs.append(("MultiIsoM",                                       "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoT",                                       "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoTISOEmu",                                 "MVATightElectronToIso",          region))
  jobs.append(("ConvVetoIHit0",                                   "MVATightElectronToIso",          region))

  jobs.append(("Charge",                                          "MVATightConvIHit0ElectronToIso", region))

  jobs.append(("RelIso012",                                       "CutBasedStopsDileptonToIso",     region))

from multiprocessing import Pool
pool = Pool(processes=16)
pool.map(runGetTemplatesFromMC, jobs)
pool.close()
pool.join()

# Adding everything to all_pdfs, a bit complex as CMSSW doesn't accept more than 255 arguments to a PSet
for fit in ['nominalFit', 'altSigFit']:
  with open(os.path.join(tnpPackage, 'python', fit + '.py'), 'w') as f:
    f.write('import FWCore.ParameterSet.Config as cms\n\n')

    for args in jobs:
      f.write('pdfs_' + getIdLabel(args) + ' = cms.PSet(\n')
      with open(os.path.join(tnpPackage, 'python', fit + "_" + getIdLabel(args) + ".py"), "r") as r:
	f.writelines(r.readlines()[3:-2])
      f.write(')\n\n')

    f.write('all_pdfs = cms.PSet(\n')
    for args in jobs:
      f.write('  pdfs_' + getIdLabel(args) + ',\n')
    f.write(')')

  import glob, os
  map(os.remove, glob.glob(os.path.join(tnpPackage, 'python', fit + '_*.p*')))

# For background shape systematic, replace RooCMSShape with RooExponetial (take three alternatives for initial parameters to be sure at least one fit succeeds)
with open(os.path.join(tnpPackage, 'python', 'altBkgFit_alternative0.py'), 'w') as f:
  with open(os.path.join(tnpPackage, 'python', 'nominalFit.py'), 'r') as r:
    for line in r:
      if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[-0.001, -.1, .1])",\n')
      elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[-0.001, -.1, .1])",\n')
      else:                                           f.write(line)

with open(os.path.join(tnpPackage, 'python', 'altBkgFit_alternative1.py'), 'w') as f:
  with open(os.path.join(tnpPackage, 'python', 'nominalFit.py'), 'r') as r:
    for line in r:
      if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[0.02, -.1, .1])",\n')
      elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[0.02, -.1, .1])",\n')
      else:                                           f.write(line)

with open(os.path.join(tnpPackage, 'python', 'altBkgFit_alternative2.py'), 'w') as f:
  with open(os.path.join(tnpPackage, 'python', 'nominalFit.py'), 'r') as r:
    for line in r:
      if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[-0.02, -.1, .1])",\n')
      elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[-0.02, -.1, .1])",\n')
      else:                                           f.write(line)
