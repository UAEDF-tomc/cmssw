import FWCore.ParameterSet.Config as cms
#### .ID with data and MC: 
####     cmsRun fitMuonID_id.py data all 
####     cmsRun fitMuonID_id.py mc

import sys, os, shutil
args = sys.argv[1:]
scenario = "data_all"
if len(args) > 2: scenario = args[2]
print "Will run scenario", scenario
sample = 'JSON1280'
if len(args) > 3: sample = args[3]
print 'the sample is', sample 

process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

def getCategories(wps, isData):
  categories = cms.PSet()
  for wp in wps: setattr(categories, wp, cms.vstring(wp, "dummy[pass=1,fail=0]"))
  return categories


Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer", NumCPU = cms.uint32(1), SaveWorkspace = cms.bool(False),
    Variables = cms.PSet(
        #weight                           = cms.vstring("weight","-100","100",""),
        mass                              = cms.vstring("Tag-muon Mass", "70", "130", "GeV/c^{2}"),
        pt                                = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        #eta                              = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta                            = cms.vstring("muon |#eta|", "0", "2.5", ""),
        #phi                              = cms.vstring("muon #phi at vertex", "-3.1416", "3.1416", ""),
        #charge                           = cms.vstring("muon charge", "-2.5", "2.5", ""),
        #combRelIsoPF04dBeta              = cms.vstring("dBeta rel iso dR 0.4", "-2", "9999999", ""),
        #combRelIsoPF03dBeta              = cms.vstring("dBeta rel iso dR 0.3", "-2", "9999999", ""),
        tag_pt                            = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
        tag_nVertices                     = cms.vstring("Number of vertices", "0", "999", ""),
        #tag_abseta                       = cms.vstring("|eta| of tag muon", "0", "2.5", ""),
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

    Categories = getCategories(['Loose', 'Medium', 'tag_IsoMu24']),

    Expressions = cms.PSet(
      Feb2018LooseVar      = cms.vstring("Feb2018LooseVar",    "Medium==1 && abs(dB)<0.05 && abs(dzPV)<0.1 && abs(SIP)<8.0 && miniCombRelIsoTTH<0.4", "Loose", "dB", "dzPV", "SIP", "miniCombRelIsoTTH"),
      Feb2018LeptonMvaLVar = cms.vstring("Feb2018LeptonMvaL",  "mvaIdTTH > 0.8"),
      Feb2018LeptonMvaMVar = cms.vstring("Feb2018LeptonMvaM",  "mvaIdTTH > 0.85"),
      Feb2018LeptonMvaTVar = cms.vstring("Feb2018LeptonMvaT",  "mvaIdTTH > 0.9"),
      tkSigmaPtOverPtVar   = cms.vstring("tkSigmaPtOverPtVar", "tkSigmaPtOverPt<0.2"),
    ),

    Cuts = cms.PSet(
      Feb2018Loose      = cms.vstring("Feb2018Loose",      "Feb2018LooseVar",      "0.5"),
      Feb2018LeptonMvaL = cms.vstring("Feb2018LeptonMvaL", "Feb2018LeptonMvaLVar", "0.5"),
      Feb2018LeptonMvaM = cms.vstring("Feb2018LeptonMvaM", "Feb2018LeptonMvaMVar", "0.5"),
      Feb2018LeptonMvaT = cms.vstring("Feb2018LeptonMvaT", "Feb2018LeptonMvaTVar", "0.5"),
      tkSigmaPtOverPt   = cms.vstring("tkSigmaPtOverPt",   "tkSigmaPtOverPtVar",   "0.5"),
    ),

                          
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
            #par3
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


def getBins(dict, passVar=None)
  bins = cms.PSet(
      pt                      = cms.vdouble(20, 500),
      eta                     = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
      pair_probeMultiplicity  = cms.vdouble(0.5, 1.5),
      #tag selections
      tag_pt                  = cms.vdouble(25, 500),
      tag_IsoMu24             = cms.vstring("pass"), 
      tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
  )
  for var, binning in dict.iteritems(): setattr(bins, var,     cms.vdouble(*binning))
  if passVar:                           setattr(bins, passVar, cms.vstring('pass'))
  return bins

ETA_BINS                         = getBins({'pt' : (20, 500), 'eta' : (-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4)})
COARSE_ETA_BINS                  = getBins({'pt' : (20, 500), 'eta' : (0.0, 0.9, 1.2, 2.1, 2.4)})
VTX_BINS_ETA24                   = getBins({'pt' : (20, 500), 'abseta' : (0.0, 2.4), 'tag_nVertices' : (0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5)})
PT_ALLETA_BINS                   = getBins({'pt' : (20, 25, 30, 40, 50, 60, 80, 120, 200), 'abseta' : (0.0, 2.4)})
PT_ETA_BINS                      = getBins({'pt' : (20, 25, 30, 40, 50, 60, 120), 'abseta' : ( 0., 0.9, 1.2, 2.1, 2.4)})
LOWPT_ETA_BINS                   = getBins({'pt' : (15, 20, 25, 30, 40, 50, 60, 80, 120, 200), 'abseta' : (0., 0.9, 1.2, 2.1, 2.4)}) 
LOWPT_ETA_BINS_VTX_OVER_LOOSE    = getBins({'pt' : (15, 20, 25, 30, 40, 50, 60, 80, 120, 200), 'abseta' : (5, 10, 15, 20, 25, 30, 40, 50, 60, 120), 'tag_nVertices' : (0.5, 20.5, 30.5, 60.5)}, passVar='Feb2018Loose')
VTX_COARSEBINS_ETA24             = getBins({'pt' : (15, 200), 'tag_nVertices' : (0.5, 5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5, 40.5, 45.5, 50.5, 55.5, 60.5)})
VTX_COARSEBINS_ETA24_OVER_LOOSE  = getBins({'pt' : (15, 200), 'tag_nVertices' : (0.5, 5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5, 40.5, 45.5, 50.5, 55.5, 60.5)}, passVar='Feb2018Loose')

tuplesDir = '/user/tomc/public/tagAndProbe/merged/'
if scenario == 'data':
  if sample == 'all': sample = ['B','C','D','E','F','G','H-v2','H-v3']
  else:               sample = [sample]
  samples = [(tuplesDir + 'run' + r + '.root') for r in sample]
elif scenario == 'mc':
  samples = [tuplesDir + 'DY.root']

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


idBins = []
for par in ['pt_abseta_vtx', 'coarsevtx']:
  if   par=='pt_abseta_vtx': bins = LOWPT_ETA_BINS_VTX_OVER_LOOSE
  elif par=='coarsevtx':     bins = VTX_COARSEBINS_ETA24_OVER_LOOSE

  for var in ['Feb2018Loose','Feb2018LeptonMvaL','Feb2018LeptonMvaM','Feb2018LeptonMvaT']:
    idBins.append(var, 'NUM_' + var + '_DEN_loose_PAR_' + par, bins)


for num, name, den in ID_BINS:
    output = os.getcwd() + '/efficiencies/'
    try:    os.makedirs(output)
    except: pass
    outputFileName = output + "/TnP_%s_%s.root" % (scenario, name)
    print "Output: " + outputFileName 

    module = process.TnP_MuonID.clone(OutputFileName = cms.string(outputFileName))
    shape = cms.vstring("vpvPlusExpo")

    setattr(module.Efficiencies, num+"_"+name, cms.PSet(
        EfficiencyCategoryAndState = cms.vstring(num,"below"),
        UnbinnedVariables          = cms.vstring("mass") if scenario=='data' else cms.vstring(mass_variable,"weight"),
        BinnedVariables            = den.clone(),
        BinToPDFmap                = shape
        ))
    setattr(process, "TnP_MuonID_"+num+"_"+name, module)        
    setattr(process, "run_"+num+"_"+name,        cms.Path(module))

#from customizeTnPforSysts import customizeTnPforSysts
#customizeTnPforSysts(process)
