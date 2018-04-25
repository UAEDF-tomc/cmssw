import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import os


options = VarParsing('analysis')
options.register("runBToF",        False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute for run B To F")
options.register("runGH",          False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute for run G and H")
options.register("onlyData",       False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute data efficiencies")
options.register("onlyMC",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Only compute mc efficiencies")
options.register("jobId",          -1,     VarParsing.multiplicity.singleton, VarParsing.varType.int,   "jobId")
options.register("doAct",          False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Bin in activity instead of eta for isolation efficiencies")
options.register("altMC",          False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Take alternative MC")
options.register("altTag",         False,  VarParsing.multiplicity.singleton, VarParsing.varType.bool,  "Take alternative tag selection")
options.register("altBkg",         -1,     VarParsing.multiplicity.singleton, VarParsing.varType.int,   "Take alternative background shape")
options.register("altSig",         -1,     VarParsing.multiplicity.singleton, VarParsing.varType.int,   "Take alternative signal shape")
options.parseArguments()

useJets =False
options.doAct=False

tuplesDir = '/user/tomc/tagAndProbe/electrons/tuples/Moriond18_v3/' + ('2016' if is2016 else '2017') + '/'

effDir    = ('efficiencies_njets' if useJets else 'efficiencies_PV') if options.doAct else 'efficiencies'
dataFile  = 'data.root'
mcFile    = 'DY_madgraph.root'

if options.runBToF:
  effDir  += '_runBToF'
  dataFile = dataFile.replace('data','runBToF')
elif options.runGH:
  effDir  += '_runGH'
  dataFile = dataFile.replace('data','runGH')

outputDir = "./" + effDir + "/nominal"

if options.altMC:
  mcFile    = 'DY_amcatnlo.root'
  outputDir = "./" + effDir + "/altMC"

if options.altTag:
  outputDir = "./" + effDir + "/altTag"
  import PhysicsTools.TagAndProbe.altTagFit as common
elif options.altBkg >= 0:
  common = __import__('PhysicsTools.TagAndProbe.altBkgFit_alternative' + str(options.altBkg), fromlist=['all_pdfs'])
  outputDir = "./" + effDir + "/altBkg" + str(options.altBkg)
elif options.altSig >= 0:
  if options.onlyMC: import PhysicsTools.TagAndProbe.altSigFit as common
  else:              common = __import__('PhysicsTools.TagAndProbe.altSigFit_alternative' + str(options.altSig), fromlist=['all_pdfs'])
  outputDir = "./" + effDir + "/altSig" + str(options.altSig)
else:
  import PhysicsTools.TagAndProbe.nominalFit as common


def makeDirs(dir):
  try:    os.makedirs(dir)
  except: pass

makeDirs('temp')
makeDirs(outputDir)

# Note: not using regexes at the moment (just string comparison). Also official package doesn't use the regexes actually and was just picking the pdf's based on the order they were given
def BinSpec(name):
  if options.doAct:
    bins = cms.vstring("ERROR_TEMPLATE_NOT_FOUND_ERROR") # first default
    for ptBin in range(7):
      if ptBin == 0: ptRange = "10p0To20p0"
      if ptBin == 1: ptRange = "20p0To30p0"
      if ptBin == 2: ptRange = "30p0To40p0"
      if ptBin == 3: ptRange = "40p0To50p0"
      if ptBin == 4: ptRange = "50p0To100p0"
      if ptBin == 5: ptRange = "100p0To200p0"
#     if ptBin == 6: ptRange = "200p0To500p0"
      if useJets:
        for njetsBin, njets in enumerate(['m0p5To0p5','0p5To1p5','1p5To2p5','2p5To3p5','3p5To4p5','4p5To6p5']):
          bins.append("event_njets_bin" + str(njetsBin) + "__probe_Ele_pt_bin" + str(ptBin))     # bin mapped to
          bins.append(name+ "_njets_" + ptRange + "_" + njets)                   # pdf
      else:
        for pvBin, pvRange in enumerate(['0p0To5p0','5p0To10p0','10p0To15p0','15p0To20p0','20p0To25p0','25p0To30p0','30p0To35p0','35p0To40p0','40p0To45p0','45p0To9999p0']):
          bins.append("event_nPV_bin" + str(pvBin) + "__probe_Ele_pt_bin" + str(ptBin))     # bin mapped to
          bins.append(name+ "_PV_" + ptRange + "_" + pvRange)                   # pdf
    print bins
    return bins
  else:
    bins = cms.vstring("ERROR_TEMPLATE_NOT_FOUND_ERROR") # first default
    for ptBin in range(7):
      if ptBin == 0: ptRange = "10p0To20p0"
      if ptBin == 1: ptRange = "20p0To30p0"
      if ptBin == 2: ptRange = "30p0To40p0"
      if ptBin == 3: ptRange = "40p0To50p0"
      if ptBin == 4: ptRange = "50p0To100p0"
      if ptBin == 5: ptRange = "100p0To200p0"
 #     if ptBin == 6: ptRange = "200p0To500p0"
      for etaBin in range(5):
        if etaBin <= 1: region = "barrel"
        if etaBin == 2: region = "crack"
        if etaBin >= 3: region = "endcap"
        if etaBin == 0: etaRange = "0p0To0p8"
        if etaBin == 1: etaRange = "0p8To1p442"
        if etaBin == 2: etaRange = "1p442To1p566"
        if etaBin == 3: etaRange = "1p566To2p0"
        if etaBin == 4: etaRange = "2p0To2p5"
        bins.append("probe_Ele_pt_bin" + str(ptBin) + "__probe_sc_abseta_bin" + str(etaBin))     # bin mapped to
        bins.append(name+ "_" + region + "_" + ptRange + "_" + etaRange)                         # pdf

      bins.append("probe_Ele_pt_bin" + str(ptBin) + "__probe_ele_RelAct_bin")
      bins.append(name + "_alleta_" + ptRange + "_0p0To2p5")
      bins.append("probe_Ele_pt_bin" + str(ptBin) + "__event_nPV_bin")
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
if options.doAct:
  if useJets:
    IDEfficiencyBins = cms.PSet(
      probe_Ele_pt    = cms.vdouble(10. ,20. ,30., 40.,50., 100., 200., 500.),
      event_njets     = cms.vdouble(-0.5,0.5,1.5,2.5,3.5,4.5,6.5),
      )
  else:
    IDEfficiencyBins = cms.PSet(
      probe_Ele_pt    = cms.vdouble(10. ,20. ,30., 40.,50., 100., 200., 500.),
      event_nPV       = cms.vdouble(0.,5.,10.,15.,20.,25.,30.,35.,40.,45.,9999.),
      )
else:
  IDEfficiencyBins = cms.PSet(
  #  probe_Ele_pt    = cms.vdouble(10. ,20. ,30., 40.,50., 100., 200., 500.),
    probe_Ele_pt    = cms.vdouble(10. ,20. ,30., 40.,50., 100., 200.),
    probe_sc_abseta = cms.vdouble(0., 0.8, 1.442, 1.566, 2.0, 2.5),
  )

IsoEfficiencyBins = IDEfficiencyBins

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
      event_nPV        = cms.vstring("Event N_{PV}", "0", "1000000", ""),
      event_njets      = cms.vstring("Event N_{jets}", "-.5", "6.5", ""),
      probe_Ele_pt     = cms.vstring("Probe p_{T}", "10", "500", "GeV/c"),
      probe_sc_abseta  = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
      probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""),
      tag_Ele_pt       = cms.vstring("Tag p_{T}", "0.", "1000000000", "GeV/c"), # Apparently you need to add the variables which you want to use in the cut, becuase why make it simple if you can do do something more complex?
      tag_Ele_trigMVA  = cms.vstring("Tag trigMVA", "0.", "1000000000", ""),
      #Ele_dRTau       = cms.vstring("Ele_dRTau", "0.2", "100000", ""),
      #probe_dRTau     = cms.vstring("probe_dRTau", "0.2", "100000", ""),
    )
    if not isData: variables.totWeight = cms.vstring("totWeight", "0", "100000000", "")
    return variables
 


def getAnalyzer(wp, dir, isData, isIso):
    analyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
      TempDirectory            = cms.string('temp/' + outputDir.split('/')[-1]),
      InputFileNames           = cms.vstring(dataFile if isData else mcFile),
      InputDirectoryName       = cms.string(dir),
      InputTreeName            = cms.string("fitter_tree"), 
      OutputFileName           = cms.string(os.path.join(outputDir, "eff_" + ("data" if isData else "mc") + "_" + dir.split('To')[0] + "To" + wp + ".root")),
      NumCPU                   = cms.uint32(6),
      SaveWorkspace            = cms.bool(False),       # Time comsuming/could cause crashes if set True
      doCutAndCount            = cms.bool(not (isData or options.altSig == 0)),  # Only for MC, but now when we provide the altSig parameter because then we fit the MC
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
    if not isData:     analyzer.Cuts            = cms.PSet(mcTrue = cms.vstring("mcTrue", "0.99", "above"))
    if options.altTag: analyzer.Cuts            = cms.PSet(ptCut = cms.vstring("tag_Ele_pt", "35", "above"), mvaCut = cms.vstring("tag_Ele_trigMVA", "0.95", "above"))
    return analyzer

process.seq = cms.Sequence()

def addToProcess(workingpoint, dir, isData, isIso):
    moduleName = ("Data" if isData else "MC") + dir + workingpoint
    setattr(process, moduleName, getAnalyzer(workingpoint, dir, isData, isIso))
#     process.seq += getattr(process, moduleName)

                                     # workingpoint  # directory                    # data or MC      # isIso
if options.jobId == 0: addToProcess("TTVLoose",      "EleToId",                     options.onlyData, False)
if options.jobId == 1: addToProcess("TTVLeptonMvaL", "TTVLooseToLeptonMva",         options.onlyData, False)
if options.jobId == 2: addToProcess("TTVLeptonMvaM", "TTVLooseToLeptonMva",         options.onlyData, False)
if options.jobId == 3: addToProcess("TTVLeptonMvaT", "TTVLooseToLeptonMva",         options.onlyData, False)
if options.jobId == 4: addToProcess("TightCharge",   "TTVLeptonMvaLToTightCharge",  options.onlyData, False)
if options.jobId == 5: addToProcess("TightCharge",   "TTVLeptonMvaMToTightCharge",  options.onlyData, False)
if options.jobId == 6: addToProcess("TightCharge",   "TTVLeptonMvaTToTightCharge",  options.onlyData, False)
process.fit = cms.Path(process.seq)
