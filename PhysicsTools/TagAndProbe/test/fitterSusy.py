import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import os

dataFile  = "../crab/crab_projects_80X_v8/data.root"
mcFile    = "../crab/crab_projects_80X_v8/DYToLL_Madgraph.root"
outputDir = "./nominal"

options = VarParsing('analysis')
options.register("onlyData",       False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute data efficiencies")
options.register("onlyMC",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute mc efficiencies")
options.register("onlyId",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute Gsf->Id efficiencies")
options.register("onlyIso",        False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute Id->Id+Iso efficiencies")
options.register("doAct",          False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Bin in activity instead of eta for isolation efficiencies")
options.register("altMC",          False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Take alternative MC")
options.register("altTag",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Take alternative tag selection")
options.register("altBkg",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Take alternative background shape")
options.register("altSig",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Take alternative signal shape")
options.parseArguments()

if options.altMC:
  mcFile    = "../crab/crab_projects_80X_v8/DYToLL_mcAtNLO.root"
 # mcFile    = "../crab/crab_projects_80X_v8/DYToEE_Powheg.root"
  outputDir = "./altMC"

if options.altTag:
  outputDir = "./altTag"

if options.altBkg:
  import PhysicsTools.TagAndProbe.commonFitSusy_exponential as common
  outputDir = "./altBkg"
elif options.altSig:
  import PhysicsTools.TagAndProbe.commonFitSusy_CB as common
  outputDir = "./altSig"
else:
  import PhysicsTools.TagAndProbe.commonFitSusy as common


try:
  os.makedirs(outputDir)
except:
  pass

def BinSpec(name):
    bins = cms.vstring("ERROR_TEMPLATE_NOT_FOUND_ERROR") # first default
    for ptBin in range(5):
      if ptBin == 0: ptRange = "10p0To20p0"
      if ptBin == 1: ptRange = "20p0To30p0"
      if ptBin == 2: ptRange = "30p0To40p0"
      if ptBin == 3: ptRange = "40p0To50p0"
      if ptBin == 4: ptRange = "50p0To100p0"
      if ptBin == 5: ptRange = "100p0To200p0"
      if ptBin == 6: ptRange = "200p0To2000p0"
      for etaBin in range(4):
        if etaBin <= 1: region = "barrel"
        if etaBin == 2: region = "crack"
        if etaBin == 3: region = "endcap"
        if etaBin == 0: etaRange = "0p0To0p8"
        if etaBin == 1: etaRange = "0p8To1p442"
        if etaBin == 2: etaRange = "1p442To1p566"
        if etaBin == 3: etaRange = "1p566To2p5"
        bins.append("*probe_Ele_pt_bin" + str(ptBin) + "*probe_sc_abseta_bin" + str(etaBin) + "*")     # bin mapped to
        bins.append(name+ "_" + region + "_" + ptRange + "_" + etaRange)                               # pdf

      bins.append("*probe_Ele_pt_bin" + str(ptBin) + "*probe_ele_RelAct_bin*")
      bins.append(name + "_alleta_" + ptRange + "_0p0To2p5")
      bins.append("*probe_Ele_pt_bin" + str(ptBin) + "*event_nPV_bin*")
      bins.append(name + "_alleta_" + ptRange + "_0p0To2p5")
    return bins



if not options.onlyMC:
    for pdf in common.all_pdfs.__dict__:
        param = common.all_pdfs.getParameter(pdf)
        if type(param) is not cms.vstring:
            continue
        i = 0
        for line in getattr(common.all_pdfs, pdf):
            if line.find("signalFractionInPassing") != -1:
                getattr(common.all_pdfs, pdf)[i] = line.replace("[1.0]","[0.9,0.,1.]")
            i = i + 1

process           = cms.Process("TagProbe")
process.source    = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations               = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

#specifies the binning of parameters
IDEfficiencyBins = cms.PSet(
    probe_Ele_pt    = cms.vdouble(10. ,20. ,30. ,40. ,50., 100.,200., 2000.),
    #event_nPV      = cms.vdouble(0.,5.,10.,15.,20.,100.),
    probe_sc_abseta = cms.vdouble(0., 0.8, 1.442, 1.566, 2.0, 2.5),
    )

if not options.doAct:
    IsoEfficiencyBins = IDEfficiencyBins
    trail = "eta"
else:
    IsoEfficiencyBins = cms.PSet(
        probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. , 100., 200., 2000.),
        #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
        probe_ele_RelAct = cms.vdouble(0., 0.02, 0.05, 0.15, 1., 99999.),
        )
    trail = "act"


def getBinningSpecification(wp, dir, isData, isIso):
  return cms.PSet(
#   UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    UnbinnedVariables = cms.vstring("mass") if isData else cms.vstring("mass", "totWeight"),
    BinnedVariables = cms.PSet(IsoEfficiencyBins if isIso else IDEfficiencyBins) if isData else cms.PSet(IsoEfficiencyBins if isIso else IDEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = BinSpec(dir.split('To')[0] + 'To' + wp),
  )

# defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
# there will be a separate output directory for each calculation that includes a
# simultaneous fit, side band subtraction and counting.
def getEfficiencies(wp, dir, isData, isIso):
   Efficiencies = cms.PSet()
   setattr(Efficiencies, wp if isData else "MCtruth_" + wp, 
     cms.PSet(getBinningSpecification(wp, dir, isData, isIso),
              EfficiencyCategoryAndState = cms.vstring("passing" + wp, "pass"),
     ),
   )
   return Efficiencies

# defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculation
def getCategories(wp, isData):
    categories = cms.PSet()
    setattr(categories, "passing" + wp, cms.vstring("passing" + wp, "dummy[pass=1,fail=0]"))
    if not isData: categories.mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]")
    return categories


# defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
def getVariables(isData):
    variables = cms.PSet(
      mass             = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
      #event_nPV       = cms.vstring("Event N_{PV}", "0", "1000000", ""),
      probe_Ele_pt     = cms.vstring("Probe p_{T}", "10", "200", "GeV/c"),
      probe_sc_abseta  = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
      probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""),
      #tag_Ele_pt      = cms.vstring("Tag p_{T}", "35.", "1000000000", "GeV/c"),
      #Ele_dRTau       = cms.vstring("Ele_dRTau", "0.2", "100000", ""),
      #probe_dRTau     = cms.vstring("probe_dRTau", "0.2", "100000", ""),
    )
    if not isData: variables.totWeight = cms.vstring("totWeight", "0", "100000000", "")
    return variables
 


def getAnalyzer(wp, dir, isData, isIso):
    analyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
      TempDirectory            = cms.string('temp_' + outputDir.split('./')[-1]),
      InputFileNames           = cms.vstring(dataFile if isData else mcFile),
      InputDirectoryName       = cms.string(dir),
      InputTreeName            = cms.string("fitter_tree"), 
      OutputFileName           = cms.string(os.path.join(outputDir, "eff_" + ("data" if isData else "mc") + "_" + wp + (("_" + trail) if isIso else "") + ".root")),
      NumCPU                   = cms.uint32(6),
      SaveWorkspace            = cms.bool(False),       # Time comsuming/could cause crashes if set True
      doCutAndCount            = cms.bool(not isData),  # Only for MC
      floatShapeParameters     = cms.bool(True),
  #   fixVars                  = cms.vstring("meanP","sigmaP","meanF","sigmaF"), # switch off fixed vars
      binnedFit                = cms.bool(True),
      binsForFit               = cms.uint32(60),
      Variables                = getVariables(isData),
      Categories               = getCategories(wp, isData),
      PDFs                     = common.all_pdfs,
      Efficiencies             = getEfficiencies(wp, dir, isData, isIso),
    )
    if not isData:     analyzer.WeightVariable  = cms.string("totWeight")
    if options.altTag: analyzer.Cuts            = cms.PSet(ptCut = cms.vstring("tag_Ele_pt", "35", "above"), mvaCut = cms.vstring("tag_Ele_trigMVA", "0.95", "above"))
    return analyzer

# MC
process.McGsfElectronToVeto                                       = getAnalyzer("Veto",                                     "GsfElectronToID",                False, False)
process.McGsfElectronToLoose                                      = getAnalyzer("Loose",                                    "GsfElectronToID",                False, False)
process.McGsfElectronToMedium                                     = getAnalyzer("Medium",                                   "GsfElectronToID",                False, False)
process.McGsfElectronToTight                                      = getAnalyzer("Tight",                                    "GsfElectronToID",                False, False)
process.McGsfElectronToLoose2D                                    = getAnalyzer("Loose2D",                                  "GsfElectronToID",                False, False)
process.McGsfElectronToFOID2D                                     = getAnalyzer("FOID2D",                                   "GsfElectronToID",                False, False)
process.McGsfElectronToTight2D3D                                  = getAnalyzer("Tight2D3D",                                "GsfElectronToID",                False, False)
process.McGsfElectronToTightID2D3D                                = getAnalyzer("TightID2D3D",                              "GsfElectronToID",                False, False)
process.McGsfElectronToLeptonMvaM                                 = getAnalyzer("LeptonMvaM",                               "GsfElectronToID",                False, False)
process.McGsfElectronToLeptonMvaVT                                = getAnalyzer("LeptonMvaVT",                              "GsfElectronToID",                False, False)
process.McGsfElectronToCutBasedTTZ                                = getAnalyzer("CutBasedTTZ",                              "GsfElectronToID",                False, False)
process.McGsfElectronToCutBasedIllia                              = getAnalyzer("CutBasedIllia",                            "GsfElectronToID",                False, False)
process.McGsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04   = getAnalyzer("LeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04", "GsfElectronToID",                False, False)
process.McGsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04    = getAnalyzer("LeptonMvaMIDEmuTightIP2DSIP3D8miniIso04",  "GsfElectronToID",                False, False)

process.McMVAVLooseElectronToMini                                 = getAnalyzer("Mini",                                     "MVAVLooseElectronToIso",         False, True)
process.McMVAVLooseElectronToMini2                                = getAnalyzer("Mini2",                                    "MVAVLooseElectronToIso",         False, True)
process.McMVAVLooseElectronToMini4                                = getAnalyzer("Mini4",                                    "MVAVLooseElectronToIso",         False, True)
process.McMVAVLooseElectronToConvIHit1                            = getAnalyzer("ConvIHit1",                                "MVAVLooseElectronToIso",         False, True)

process.McMVATightElectronToMultiIsoT                             = getAnalyzer("MultiIsoT",                                "MVATightElectronToIso",          False, True)
process.McMVATightElectronToMultiIsoVT                            = getAnalyzer("MultiIsoVT",                               "MVATightElectronToIso",          False, True)
process.McMVATightElectronToMultiIsoEmu                           = getAnalyzer("MultiIsoEmu",                              "MVATightElectronToIso",          False, True)
process.McMVATightElectronToConvIHit1                             = getAnalyzer("ConvIHit0",                                "MVATightElectronToIso",          False, True)
process.McMVATightElectronToConvIHit0Chg                          = getAnalyzer("ConvIHit0Chg",                             "MVATightElectronToIso",          False, True)

process.McMVATightNoEMuElectronToConvIHit0                        = getAnalyzer("ConvIHit0",                                "MVATightNoEMuElectronToIso",     False, True)
process.McMVATightConvIHit0ElectronToConvIHit0Chg                 = getAnalyzer("ConvIHit0Chg",                             "MVATightConvIHit0ElectronToIso", False, True)

process.McCutBasedTightElectronToMultiIsoVT                       = getAnalyzer("MultiIsoVT",                               "CutBasedTightElectronToIso",     False, True)

# Data
process.DataGsfElectronToVeto                                     = getAnalyzer("Veto",                                     "GsfElectronToID",                True,  False)
process.DataGsfElectronToLoose                                    = getAnalyzer("Loose",                                    "GsfElectronToID",                True,  False)
process.DataGsfElectronToMedium                                   = getAnalyzer("Medium",                                   "GsfElectronToID",                True,  False)
process.DataGsfElectronToTight                                    = getAnalyzer("Tight",                                    "GsfElectronToID",                True,  False)
process.DataGsfElectronToLoose2D                                  = getAnalyzer("Loose2D",                                  "GsfElectronToID",                True,  False)
process.DataGsfElectronToFOID2D                                   = getAnalyzer("FOID2D",                                   "GsfElectronToID",                True,  False)
process.DataGsfElectronToTight2D3D                                = getAnalyzer("Tight2D3D",                                "GsfElectronToID",                True,  False)
process.DataGsfElectronToTightID2D3D                              = getAnalyzer("TightID2D3D",                              "GsfElectronToID",                True,  False)
process.DataGsfElectronToLeptonMvaM                               = getAnalyzer("LeptonMvaM",                               "GsfElectronToID",                True,  False)
process.DataGsfElectronToLeptonMvaVT                              = getAnalyzer("LeptonMvaVT",                              "GsfElectronToID",                True,  False)
process.DataGsfElectronToCutBasedTTZ                              = getAnalyzer("CutBasedTTZ",                              "GsfElectronToID",                True,  False)
process.DataGsfElectronToCutBasedIllia                            = getAnalyzer("CutBasedIllia",                            "GsfElectronToID",                True,  False)
process.DataGsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 = getAnalyzer("LeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04", "GsfElectronToID",                True,  False)
process.DataGsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04  = getAnalyzer("LeptonMvaMIDEmuTightIP2DSIP3D8miniIso04",  "GsfElectronToID",                True,  False)

process.DataMVAVLooseElectronToMini                               = getAnalyzer("Mini",                                     "MVAVLooseElectronToIso",         True,  True)
process.DataMVAVLooseElectronToMini2                              = getAnalyzer("Mini2",                                    "MVAVLooseElectronToIso",         True,  True)
process.DataMVAVLooseElectronToMini4                              = getAnalyzer("Mini4",                                    "MVAVLooseElectronToIso",         True,  True)
process.DataMVAVLooseElectronToConvIHit1                          = getAnalyzer("ConvIHit1",                                "MVAVLooseElectronToIso",         True,  True)

process.DataMVATightElectronToMultiIsoT                           = getAnalyzer("MultiIsoT",                                "MVATightElectronToIso",          True,  True)
process.DataMVATightElectronToMultiIsoVT                          = getAnalyzer("MultiIsoVT",                               "MVATightElectronToIso",          True,  True)
process.DataMVATightElectronToMultiIsoEmu                         = getAnalyzer("MultiIsoEmu",                              "MVATightElectronToIso",          True,  True)
process.DataMVATightElectronToConvIHit1                           = getAnalyzer("ConvIHit0",                                "MVATightElectronToIso",          True,  True)
process.DataMVATightElectronToConvIHit0Chg                        = getAnalyzer("ConvIHit0Chg",                             "MVATightElectronToIso",          True,  True)

process.DataMVATightNoEMuElectronToConvIHit0                      = getAnalyzer("ConvIHit0",                                "MVATightNoEMuElectronToIso",     True,  True)
process.DataMVATightConvIHit0ElectronToConvIHit0Chg               = getAnalyzer("ConvIHit0Chg",                             "MVATightConvIHit0ElectronToIso", True,  True)

process.DataCutBasedTightElectronToMultiIsoVT                     = getAnalyzer("MultiIsoVT",                               "CutBasedTightElectronToIso",     True,  True)


process.seq = cms.Sequence()

if not options.onlyData and not options.onlyIso:
    process.seq += process.McGsfElectronToVeto
    process.seq += process.McGsfElectronToLoose
    process.seq += process.McGsfElectronToMedium
    process.seq += process.McGsfElectronToTight
    process.seq += process.McGsfElectronToLoose2D
    process.seq += process.McGsfElectronToFOID2D
    process.seq += process.McGsfElectronToTight2D3D
    process.seq += process.McGsfElectronToTightID2D3D
    process.seq += process.McGsfElectronToLeptonMvaM
    process.seq += process.McGsfElectronToLeptonMvaVT
    process.seq += process.McGsfElectronToCutBasedTTZ
    process.seq += process.McGsfElectronToCutBasedIllia
    process.seq += process.McGsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04
    process.seq += process.McGsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04

if not options.onlyData and not options.onlyId:
    process.seq += process.McMVAVLooseElectronToMini
    process.seq += process.McMVAVLooseElectronToMini2
    process.seq += process.McMVAVLooseElectronToMini4
    process.seq += process.McMVAVLooseElectronToConvIHit1

    process.seq += process.McMVATightElectronToMultiIsoT
    process.seq += process.McMVATightElectronToMultiIsoVT
    process.seq += process.McMVATightElectronToMultiIsoEmu
    process.seq += process.McMVATightElectronToConvIHit1
    process.seq += process.McMVATightElectronToConvIHit0Chg

#    process.seq += process.McMVATightNoEMuElectronToConvIHit0 # does not want to work yet
    process.seq += process.McMVATightConvIHit0ElectronToConvIHit0Chg

    process.seq += process.McCutBasedTightElectronToMultiIsoVT

if not options.onlyMC and not options.onlyIso:
    process.seq += process.DataGsfElectronToVeto
    process.seq += process.DataGsfElectronToLoose
    process.seq += process.DataGsfElectronToMedium
    process.seq += process.DataGsfElectronToTight
    process.seq += process.DataGsfElectronToLoose2D
    process.seq += process.DataGsfElectronToFOID2D
    process.seq += process.DataGsfElectronToTight2D3D
    process.seq += process.DataGsfElectronToTightID2D3D
    process.seq += process.DataGsfElectronToLeptonMvaM
    process.seq += process.DataGsfElectronToLeptonMvaVT
    process.seq += process.DataGsfElectronToCutBasedTTZ
    process.seq += process.DataGsfElectronToCutBasedIllia
    process.seq += process.DataGsfElectronToLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04
    process.seq += process.DataGsfElectronToLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04


if not options.onlyMC and not options.onlyId:
    process.seq += process.DataMVAVLooseElectronToMini
    process.seq += process.DataMVAVLooseElectronToMini2
    process.seq += process.DataMVAVLooseElectronToMini4
    process.seq += process.DataMVAVLooseElectronToConvIHit1

    process.seq += process.DataMVATightElectronToMultiIsoT
    process.seq += process.DataMVATightElectronToMultiIsoVT
    process.seq += process.DataMVATightElectronToMultiIsoEmu
    process.seq += process.DataMVATightElectronToConvIHit1
    process.seq += process.DataMVATightElectronToConvIHit0Chg

#    process.seq += process.DataMVATightNoEMuElectronToConvIHit0 # does not want to work yet
    process.seq += process.DataMVATightConvIHit0ElectronToConvIHit0Chg

    process.seq += process.DataCutBasedTightElectronToMultiIsoVT

process.fit = cms.Path(process.seq)
