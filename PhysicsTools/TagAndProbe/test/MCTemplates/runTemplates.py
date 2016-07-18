#! /usr/bin/env python
import getTemplatesFromMC
import makeConfigForTemplates
import os

templateProduction = "templatesSusy"
try:
  os.makedirs(os.path.join('..', '..', 'data', templateProduction))
except:
  pass

class options:
    input           = "../../crab/crab_projects_80X_v8/DYToLL_Madgraph.root"
    output          = "mc_templates.root"
    directory       = "GsfElectronToID"
    idprobe         = "passingMedium"
    var1Bins        = "10,20,30,40,50,200"
    var2Bins        = "0.0,0.8,1.4442,1.566,,2.5"
    var1Name        = "probe_Ele_pt"
    var2Name        = "probe_sc_abseta"
    addProbeCut     = ""
    weightVarName   = "totWeight"
    tagTauVarName   = "" # "tag_Ele_dRTau"
    probeTauVarName = "" # "probe_dRTau
    idLabel         = ""
    failBkgPdf      = "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])"
    passBkgPdf      = "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])"

def runGetTemplatesFromMC(args):
    idProbe, directory, region = args

    myOptions = options()

    if region == "alleta":     options.var2Bins = "0,2.5"
    if region == "barrel":     options.var2Bins = "0,0.8,1.442"
    if region == "crack":      options.var2Bins = "1.442,1.566"
    if region == "endcap":     options.var2Bins = "1.566,2.5"

    myOptions.idLabel      = directory.split('To')[0] + 'To' + idProbe + "_" + region
    myOptions.output       = os.path.join('..', '..', 'data', templateProduction, myOptions.idLabel + ".root")
    myOptions.directory    = directory
    myOptions.idprobe      = "passing" + idProbe
    getTemplatesFromMC.main(myOptions)

    myOptions.outputFile   = os.path.join('..', '..', 'python', "commonFit_" + myOptions.idLabel + ".py")
    myOptions.templateFile = myOptions.output
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
  jobs.append(("LeptonMvaM",                                      "GsfElectronToID",                region))
  jobs.append(("LeptonMvaVT",                                     "GsfElectronToID",                region))
  jobs.append(("CutBasedTTZ",                                     "GsfElectronToID",                region))
  jobs.append(("CutBasedIllia",                                   "GsfElectronToID",                region))
  jobs.append(("LeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04",        "GsfElectronToID",                region))
  jobs.append(("LeptonMvaMIDEmuTightIP2DSIP3D8miniIso04",         "GsfElectronToID",                region))

  jobs.append(("Mini",                                            "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini",                                            "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini2",                                           "MVAVLooseElectronToIso",         region))
  jobs.append(("Mini4",                                           "MVAVLooseElectronToIso",         region))
  jobs.append(("ConvIHit1",                                       "MVAVLooseElectronToIso",         region))

  jobs.append(("MultiIsoT",                                       "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoVT",                                      "MVATightElectronToIso",          region))
  jobs.append(("MultiIsoEmu",                                     "MVATightElectronToIso",          region))
  jobs.append(("ConvIHit0",                                       "MVATightElectronToIso",          region))
  jobs.append(("ConvIHit0Chg",                                    "MVATightElectronToIso",          region))

  jobs.append(("ConvIHit0",                                       "MVATightNoEMuElectronToIso",     region))
  jobs.append(("ConvIHit0Chg",                                    "MVATightConvIHit0ElectronToIso", region))

  jobs.append(("MultiIsoVT",                                      "CutBasedTightElectronToIso",     region))

#from multiprocessing import Pool
#pool = Pool(processes=16)
#pool.map(runGetTemplatesFromMC, jobs)
#pool.close()
#pool.join()

os.system('rm ../../python/commonFit.py')
with open('../../python/commonFit.py', 'w') as f:
  f.write('import FWCore.ParameterSet.Config as cms\n')
  f.write('all_pdfs = cms.PSet(\n')
  for (idProbe, dir, region) in jobs:
    idLabel = dir.split('To')[0] + 'To' + idProbe + "_" + region
    with open(os.path.join('..','..','python', "commonFit_" + idLabel + ".py"), "r") as r:
      f.writelines(r.readlines()[3:-2])
  f.write(')\n')
