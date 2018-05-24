import FWCore.ParameterSet.Config as cms

import sys, os, shutil
wp, ref, scenario, year, binning, sys = tuple(sys.argv[-6:])
outDir = os.path.join(os.getcwd(), 'efficiencies', year, binning, scenario, sys)

process           = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source    = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1))

def getCategories(wps):
  categories = cms.PSet()
  for wp in wps: setattr(categories, wp, cms.vstring(wp, "dummy[pass=1,fail=0]"))
  return categories

def getExpressions(wps):
  expressions = cms.PSet()
  for wp in wps: setattr(expressions, wp + 'Var', cms.vstring(wp + 'Var', wp + '==1', wp))
  return expressions

def getCuts(wps):
  cuts = cms.PSet()
  for wp in wps: setattr(cuts, wp + 'Cut', cms.vstring(wp + 'Cut', wp + 'Var', '0.5'))
  return cuts


#
# Define samples
#
tuplesDir = '/user/tomc/public/tagAndProbe/' + year + '/merged/'
if scenario == 'data':
  sample  = ['B','C','D','E','F','G','H-v2','H-v3'] if year=='2016' else ['B','C','D','E','F']
  samples = [(tuplesDir + 'run' + r + '.root') for r in sample]
elif scenario == 'mc':
  samples = [tuplesDir + 'DY' + ('_LO' if sys=='altMC' else '') + '_vtxWeighted.root']

#
# Template
#
template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer", NumCPU = cms.uint32(8), SaveWorkspace = cms.bool(False),
  Variables = cms.PSet(
    mass                    = cms.vstring("Tag-muon Mass", "60" if sys=="altMass1" else "70", "120" if sys=="altMass2" else "130", "GeV/c^{2}"),
    pt                      = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
    abseta                  = cms.vstring("muon |#eta|", "0", "2.5", ""),
    tag_pt                  = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
    tag_nVertices           = cms.vstring("Number of vertices", "0", "999", ""),
    tag_combRelIsoPF04dBeta = cms.vstring("Tag dBeta rel iso dR 0.4", "-2", "9999999", ""),
    pair_probeMultiplicity  = cms.vstring("pair_probeMultiplicity", "0","30",""),
    pair_nJets30            = cms.vstring("pair_nJets30", "-1","10",""),
  ),

  Expressions = getExpressions(['TTVLoose', 'TTVLeptonMvaTTZ4l', 'TTVLeptonMvaTTZ3l', 'TTVLeptonMvaTTW', 'TTVLeptonMvatZq', 'tkSigmaPtOverPtCut']),
  Cuts        = getCuts(['TTVLoose', 'TTVLeptonMvaTTZ4l', 'TTVLeptonMvaTTZ3l', 'TTVLeptonMvaTTW', 'TTVLeptonMvatZq', 'tkSigmaPtOverPtCut']),
  Categories  = getCategories(['tag_IsoMu24', 'TTVLoose', 'TTVLeptonMvaTTZ4l', 'TTVLeptonMvaTTZ3l', 'TTVLeptonMvaTTW', 'TTVLeptonMvatZq', 'tkSigmaPtOverPtCut']),

  PDFs = cms.PSet(
    vpvPlusExpo = cms.vstring(
      "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
      "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
      "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
      "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
      "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
      "efficiency[0.9,0,1]",
      "signalFractionInPassing[0.9]",
    ),

    vpvPlusCMS = cms.vstring(
      "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
      "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
      "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
      "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.02, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])",
      "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.02, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass)",
      "efficiency[0.9,0.7,1]",
      "signalFractionInPassing[0.9]",
    ),
  ),

  binnedFit             = cms.bool(True),
  binsForFit            = cms.uint32(40),
  saveDistributionsPlot = cms.bool(False),

  Efficiencies          = cms.PSet(),
  InputFileNames        = cms.vstring(*samples),
  OutputFileName        = cms.string(""),
  InputTreeName         = cms.string("fitter_tree"),
  InputDirectoryName    = cms.string("tpTree"),
)

if scenario == 'mc':
  template.WeightVariable   = cms.string("weight")
  template.Variables.weight = cms.vstring("weight","-10","10","")

def getBins(binnings, passVar=None):
  bins = cms.PSet(
      pair_probeMultiplicity  = cms.vdouble(0.5, 1.5),
      tag_pt                  = cms.vdouble(25, 500),
      tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2 if sys=="altTag1" else (0.3 if sys=="altTag2" else 0.25)),
  )
  if year=='2017':                setattr(bins, 'tag_IsoMu24', cms.vstring("pass"))
  for var, binning in binnings:   setattr(bins, var,           cms.vdouble(*binning))
  if passVar and passVar!='None': setattr(bins, passVar,       cms.vstring('pass'))
  return bins

def getBinning(binning, refPoint):
  if binning == 'test':       return getBins([('pt', (40, 50)),                            ('abseta',        (0., 0.9, 1.2, 2.1, 2.4))],                    passVar=refPoint)
  if binning == 'pt_eta':     return getBins([('pt', (10, 20, 30, 40, 50, 100, 200, 500)), ('abseta',        (0., 0.9, 1.2, 2.1, 2.4))],                    passVar=refPoint)
  if binning == 'pt_vtx':     return getBins([('pt', (10, 20, 30, 40, 50, 100, 200, 500)), ('tag_nVertices', (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 999))], passVar=refPoint)
  if binning == 'pt_jets':    return getBins([('pt', (10, 20, 30, 40, 50, 100, 200, 500)), ('pair_nJets30',  (-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 6.5))],        passVar=refPoint)

def addModules(num, refPoint, binning):
  name = 'NUM_' + num + '_DEN_' + (refPoint if refPoint else 'reco') + '_PAR_' + binning

  try:    os.makedirs(outDir)
  except: pass
  outputFileName = outDir + '/TnP_' + ref + 'To' + wp + '.root'
  print "Output: " + outputFileName 

  module = template.clone(OutputFileName = cms.string(outputFileName))
  shape = cms.vstring("vpvPlusCMS" if sys=="altShape" else "vpvPlusExpo")
  setattr(module.Efficiencies, num+"_"+name, cms.PSet(
      EfficiencyCategoryAndState = cms.vstring(num + 'Cut', 'above'),
      UnbinnedVariables          = cms.vstring("mass") if scenario=='data' else cms.vstring("mass", "weight"),
      BinnedVariables            = getBinning(binning, refPoint),
      BinToPDFmap                = shape
      ))

  print module.Categories
  print module.Efficiencies
  setattr(process, "TnP_MuonID_"+num+"_"+name, module)        
  setattr(process, "run_"+num+"_"+name, cms.Path(module))

addModules(wp, ref, binning)
