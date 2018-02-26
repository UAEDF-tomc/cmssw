import FWCore.ParameterSet.Config as cms
#### .ID with data and MC: 
####     cmsRun fitMuonID_id.py data 1
####     cmsRun fitMuonID_id.py mc 1

import sys, os, shutil
args = sys.argv[1:]
scenario, id = tuple(sys.argv[2:])

process           = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source    = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1))

def getCategories(wps):
  categories = cms.PSet()
  for wp in wps: setattr(categories, wp, cms.vstring(wp, "dummy[pass=1,fail=0]"))
  return categories


Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer", NumCPU = cms.uint32(12), SaveWorkspace = cms.bool(False),
    Variables = cms.PSet(
        weight                            = cms.vstring("weight","-100","100",""),
        mass                              = cms.vstring("Tag-muon Mass", "70", "130", "GeV/c^{2}"),
        pt                                = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        abseta                            = cms.vstring("muon |#eta|", "0", "2.5", ""),
        tag_pt                            = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
        tag_nVertices                     = cms.vstring("Number of vertices", "0", "999", ""),
        tag_combRelIsoPF04dBeta           = cms.vstring("Tag dBeta rel iso dR 0.4", "-2", "9999999", ""),
        dB                                = cms.vstring("dB", "-1000", "1000", ""),
        dzPV                              = cms.vstring("dzPV", "-1000", "1000", ""),
        SIP                               = cms.vstring("SIP", "-1000", "1000", ""),
        pair_probeMultiplicity            = cms.vstring("pair_probeMultiplicity", "0","30",""),
        miniCombRelIsoTTH                 = cms.vstring("miniCombRelIsoTTH" ,  "-2", "9999999", ""),
        JetBTagCSV                        = cms.vstring("JetBTagCSV"     , "-10",       "1", ""),
        mvaIdTTH                          = cms.vstring("mvaIdTTH"       ,  "-1",       "1", ""),
        tkSigmaPtOverPt                   = cms.vstring("tkSigmaPtOverPt",   "0", "9999999", ""),
        fixedGridRhoFastjetCentralNeutral = cms.vstring("fixedGridRhoFastjetCentralNeutral", "-1", "9999999", ""),
    ),


    Expressions = cms.PSet(tkSigmaPtOverPtVar = cms.vstring("tkSigmaPtOverPtVar", "tkSigmaPtOverPt<0.2")),
    Cuts        = cms.PSet(tkSigmaPtOverPt    = cms.vstring("tkSigmaPtOverPt",   "tkSigmaPtOverPtVar",   "0.5")),

    Categories = getCategories(['Feb2018Loose', 'Feb2018LeptonMvaL', 'Feb2018LeptonMvaM', 'Feb2018LeptonMvaT', 'tag_IsoMu24']),
                          
    PDFs = cms.PSet(
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "Exponential::backgroundPass(mass, lp[0,-5,5])",
            "Exponential::backgroundFail(mass, lf[0,-5,5])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])",
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpoMin70 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])",
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCheb = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])",
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])",
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            #par3
            "RooChebychev::backgroundPass(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})",
            "RooChebychev::backgroundFail(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        voigtPlusCheb = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])",
            "RooChebychev::backgroundPass(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})",
            "RooChebychev::backgroundFail(mass, {a0[0.25,0,0.5], a1[-0.25,-1,0.1],a2[0.,-0.25,0.25]})",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        )
    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(False),

    Efficiencies = cms.PSet(),
)


def getBins(dict, passVar=None):
  bins = cms.PSet(
      pair_probeMultiplicity  = cms.vdouble(0.5, 1.5),
      tag_pt                  = cms.vdouble(25, 500),
      tag_IsoMu24             = cms.vstring("pass"), 
      tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
  )
  for var, binning in dict.iteritems(): setattr(bins, var,     cms.vdouble(*binning))
  if passVar:                           setattr(bins, passVar, cms.vstring('pass'))
  return bins

bins = {}
def getBinning(binning, refPoint):
  if binning == 'pt_eta':     return getBins({'pt' : (15, 20, 25, 30, 40, 50, 60, 80, 120, 200), 'abseta' : (5, 10, 15, 20, 25, 30, 40, 50, 60, 120)}, passVar=refPoint),
  if binning == 'pt_eta_vtx': return getBins({'pt' : (15, 20, 25, 30, 40, 50, 60, 80, 120, 200), 'abseta' : (5, 10, 15, 20, 25, 30, 40, 50, 60, 120), 'tag_nVertices' : (0.5, 20.5, 30.5, 60.5)}, passVar=refPoint),
  if binning == 'vtx':        return getBins({'pt' : (15, 200), 'abseta' : (0.0, 2.4), 'tag_nVertices' : (0.5, 5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5, 40.5, 45.5, 50.5, 55.5, 60.5)}, passVar=refPoint),

tuplesDir = '/user/tomc/public/tagAndProbe/merged/'
if scenario == 'data':
  sample  = ['B','C','D','E','F','G','H-v2','H-v3']
  samples = [(tuplesDir + 'run' + r + '.root') for r in sample]
elif scenario == 'mc':
  samples = [tuplesDir + 'DY_vtxWeighted.root']

process.TnP_MuonID = Template.clone(
    InputFileNames = cms.vstring(*samples),
    InputTreeName = cms.string("fitter_tree"),
    InputDirectoryName = cms.string("tpTree"),
    OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
    Efficiencies = cms.PSet(),
)

if scenario == 'mc':
  process.TnP_MuonID.WeightVariable = cms.string("weight")
  process.TnP_MuonID.Variables.weight = cms.vstring("weight","-10","10","")


def addModules(num, refPoint, binning):
  name = 'NUM_' + num + '_DEN_' + (den if den else 'reco') + '_PAR_' + binning

  output = os.getcwd() + '/efficiencies/'
  try:    os.makedirs(output)
  except: pass
  outputFileName = output + "/TnP_%s_%s.root" % (scenario, name)
  print "Output: " + outputFileName 

  module = process.TnP_MuonID.clone(OutputFileName = cms.string(outputFileName))
  shape = cms.vstring("vpvPlusExpo")

  setattr(module.Efficiencies, num+"_"+name, cms.PSet(
      EfficiencyCategoryAndState = cms.vstring(num,"below"),
      UnbinnedVariables          = cms.vstring("mass") if scenario=='data' else cms.vstring("mass", "weight"),
      BinnedVariables            = getBinning(binning, refPoint),
      BinToPDFmap                = shape
      ))
  setattr(process, "TnP_MuonID_"+num+"_"+name, module)        
  setattr(process, "run_"+num+"_"+name,        cms.Path(module))

binning = 'pt_eta'
if id==1: addModules('Feb2018Loose',      None,                binning)
if id==2: addModules('Feb2018LeptonMvaL', 'Feb2018Loose',      binning)
if id==3: addModules('Feb2018LeptonMvaM', 'Feb2018Loose',      binning)
if id==4: addModules('Feb2018LeptonMvaT', 'Feb2018Loose',      binning)
if id==5: addModules('tkSigmaPtOverPt',   'Feb2018LeptonMvaL', binning)
if id==6: addModules('tkSigmaPtOverPt',   'Feb2018LeptonMvaM', binning)
if id==7: addModules('tkSigmaPtOverPt',   'Feb2018LeptonMvaT', binning)


#from customizeTnPforSysts import customizeTnPforSysts
#customizeTnPforSysts(process)
