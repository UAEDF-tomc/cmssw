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

def getIdLabel(args):
    idProbe, directory, region = args
    return directory.split('To')[0] + 'To' + idProbe + "_" + region


class options:
    input           = "../../crab/crab_projects_80X_v12/DYToLL_Madgraph.root"
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

    # Manual fix to avoid failed fits
    #if myOptions.idLabel == "GsfElectronToTight2D3D_barrel_20p0To30p0_0p0To0p8":  
    #  myOptions.failBkgPdf = "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.02, 0, 1], peakFail[90.0, 70, 80])"
    #  myOptions.passBkgPdf = "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.02, 0, 1], peakPass[90.0, 70, 80])"

    makeConfigForTemplates.main(myOptions)

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
  jobs.append(("Mini3",                                           "CutBasedTightElectronToIso",     region))

from multiprocessing import Pool
pool = Pool(processes=16)
pool.map(runGetTemplatesFromMC, jobs)
pool.close()
pool.join()

# Adding everything to all_pdfs, a bit complex as CMSSW doesn't accept more than 255 arguments to a PSet
for fit in ['nominalFit', 'altSigFit']:
  with open(os.path.join(tnpPackage, 'python', fit + 'Susy.py'), 'w') as f:
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

# For background shape systematic, remove lines with RooCMSShape
with open(os.path.join(tnpPackage, 'python', 'altBkgFit.py'), 'w') as f:
  with open(os.path.join(tnpPackage, 'python', 'nominalFit.py'), 'r') as r:
    for line in r:
      if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[-0.001, -.1, .1])",\n')
      elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[-0.001, -.1, .1])",\n')
      else:                                           f.write(line)
