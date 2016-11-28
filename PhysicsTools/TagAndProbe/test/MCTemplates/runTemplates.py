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

failedFits = ["GsfElectronToFOID2D_barrel_10p0To20p0_0p0To0p8",
              "GsfElectronToLoose2D_endcap_20p0To30p0_2p0To2p5",
              "GsfElectronToTight2D3D_endcap_20p0To30p0_1p566To2p0",
             ]


failedFitsAltSig = ["GsfElectronToMedium_crack_10p0To20p0_1p442To1p566",
		    "GsfElectronToTight_endcap_10p0To20p0_1p566To2p0",
		    "GsfElectronToVeto_barrel_10p0To20p0_0p0To0p8",
		    "GsfElectronToVeto_endcap_10p0To20p0_1p566To2p0",
		    "GsfElectronToVeto_barrel_10p0To20p0_0p8To1p442",
		    "MVATightConvIHit0ElectronToConvIHit0Chg_barrel_10p0To20p0_0p0To0p8",
		    "MVATightConvIHit0ElectronToConvIHit0Chg_barrel_10p0To20p0_0p8To1p442",
		    "MVATightElectronToMultiIsoM_endcap_50p0To100p0_1p566To2p0",
		    "CutBasedTightElectronToMini_barrel_10p0To20p0_0p0To0p8",
		    "CutBasedTightElectronToMini_barrel_10p0To20p0_0p8To1p442",
		    "GsfElectronToCutBasedIllia_crack_10p0To20p0_1p442To1p566",
		    "GsfElectronToCutBasedTTZ_crack_10p0To20p0_1p442To1p566",
		    "MVATightElectronToMultiIsoVT_barrel_100p0To2000p0_0p0To0p8",
                   ]

def getIdLabel(args):
    idProbe, directory, region = args
    return directory.split('To')[0] + 'To' + idProbe + "_" + region


class options:
    input           = os.path.join(tnpPackage, 'crab', 'crab_projects_80X_v15', 'DYToLL_Madgraph.root')
    output          = "mc_templates.root"
    directory       = "GsfElectronToID"
    idprobe         = "passingMedium"
    var1Bins        = "10,20,30,40,50,100,2000"
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
  jobs.append(("Veto",                                            "GsfElectronToID",                region))
  jobs.append(("Loose",                                           "GsfElectronToID",                region))
  jobs.append(("Medium",                                          "GsfElectronToID",                region))
  jobs.append(("Tight",                                           "GsfElectronToID",                region))
  jobs.append(("Loose2D",                                         "GsfElectronToID",                region))
  jobs.append(("FOID2D",                                          "GsfElectronToID",                region))
  jobs.append(("Tight2D3D",                                       "GsfElectronToID",                region))
  jobs.append(("TightID2D3D",                                     "GsfElectronToID",                region))
  jobs.append(("CutBasedTTZ",                                     "GsfElectronToID",                region))
  jobs.append(("CutBasedIllia",                                   "GsfElectronToID",                region))
  jobs.append(("CutBasedStopsDilepton",                           "GsfElectronToID",                region))
  jobs.append(("LeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04",        "GsfElectronToID",                region))
  jobs.append(("LeptonMvaMIDEmuTightIP2DSIP3D8miniIso04",         "GsfElectronToID",                region))

  jobs.append(("Mini",                                            "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini2",                                           "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini4",                                           "MVAVLooseElectronToIso",         region))
  jobs.append(("ConvIHit1",                                       "MVAVLooseElectronToIso",         region))

  jobs.append(("MultiIsoM",                                       "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoT",                                       "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoVT",                                      "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoEmu",                                     "MVATightElectronToIso",          region))
  jobs.append(("ConvIHit0",                                       "MVATightElectronToIso",          region))
  jobs.append(("ConvIHit0Chg",                                    "MVATightElectronToIso",          region))

  jobs.append(("ConvIHit0",                                       "MVATightNoEMuElectronToIso",     region))
  jobs.append(("ConvIHit0Chg",                                    "MVATightConvIHit0ElectronToIso", region))

  jobs.append(("MultiIsoVT",                                      "CutBasedTightElectronToIso",     region))
  jobs.append(("Mini",                                            "CutBasedTightElectronToIso",     region))
  jobs.append(("Mini2",                                           "CutBasedTightElectronToIso",     region))
  jobs.append(("Mini4",                                           "CutBasedTightElectronToIso",     region))
  jobs.append(("Mini",                                            "CutBasedMediumElectronToIso",    region))
  jobs.append(("Mini",                                            "CutBasedLooseElectronToIso",     region))
  jobs.append(("Mini",                                            "CutBasedVetoElectronToIso",      region))

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
