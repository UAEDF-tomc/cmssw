import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
import PhysicsTools.TagAndProbe.commonFitSusy as common

dataFile = "../crab/crab_projects_80X_v8/data.root"
mcFile   = "../crab/crab_projects_80X_v8/DYToLL_Madgraph.root"

def BinSpec(name):
    return cms.vstring(
        "ERROR_TEMPLATE_NOT_FOUND_ERROR",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin0*",name+"_barrel_10p0To20p0_0p0To0p8",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin0*",name+"_barrel_20p0To30p0_0p0To0p8",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin0*",name+"_barrel_30p0To40p0_0p0To0p8",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin0*",name+"_barrel_40p0To50p0_0p0To0p8",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin0*",name+"_barrel_50p0To200p0_0p0To0p8",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin1*",name+"_barrel_10p0To20p0_0p8To1p442",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin1*",name+"_barrel_20p0To30p0_0p8To1p442",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin1*",name+"_barrel_30p0To40p0_0p8To1p442",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin1*",name+"_barrel_40p0To50p0_0p8To1p442",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin1*",name+"_barrel_50p0To200p0_0p8To1p442",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin2*",name+"_crack_10p0To20p0_1p442To1p566",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin2*",name+"_crack_20p0To30p0_1p442To1p566",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin2*",name+"_crack_30p0To40p0_1p442To1p566",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin2*",name+"_crack_40p0To50p0_1p442To1p566",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin2*",name+"_crack_50p0To200p0_1p442To1p566",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin3*",name+"_endcap_10p0To20p0_1p566To2p5",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin3*",name+"_endcap_20p0To30p0_1p566To2p5",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin3*",name+"_endcap_30p0To40p0_1p566To2p5",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin3*",name+"_endcap_40p0To50p0_1p566To2p5",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin3*",name+"_endcap_50p0To200p0_1p566To2p5",
        "*probe_Ele_pt_bin0*probe_sc_abseta_bin4*",name+"_endcap_10p0To20p0_1p566To2p5",
        "*probe_Ele_pt_bin1*probe_sc_abseta_bin4*",name+"_endcap_20p0To30p0_1p566To2p5",
        "*probe_Ele_pt_bin2*probe_sc_abseta_bin4*",name+"_endcap_30p0To40p0_1p566To2p5",
        "*probe_Ele_pt_bin3*probe_sc_abseta_bin4*",name+"_endcap_40p0To50p0_1p566To2p5",
        "*probe_Ele_pt_bin4*probe_sc_abseta_bin4*",name+"_endcap_50p0To200p0_1p566To2p5",
        "*probe_Ele_pt_bin0*probe_ele_RelAct_bin*",name+"_alleta_10p0To20p0_0p0To2p5",
        "*probe_Ele_pt_bin1*probe_ele_RelAct_bin*",name+"_alleta_20p0To30p0_0p0To2p5",
        "*probe_Ele_pt_bin2*probe_ele_RelAct_bin*",name+"_alleta_30p0To40p0_0p0To2p5",
        "*probe_Ele_pt_bin3*probe_ele_RelAct_bin*",name+"_alleta_40p0To50p0_0p0To2p5",
        "*probe_Ele_pt_bin4*probe_ele_RelAct_bin*",name+"_alleta_50p0To200p0_0p0To2p5",
        "*probe_Ele_pt_bin0*event_nPV_bin*",name+"_alleta_10p0To20p0_0p0To2p5",
        "*probe_Ele_pt_bin1*event_nPV_bin*",name+"_alleta_20p0To30p0_0p0To2p5",
        "*probe_Ele_pt_bin2*event_nPV_bin*",name+"_alleta_30p0To40p0_0p0To2p5",
        "*probe_Ele_pt_bin3*event_nPV_bin*",name+"_alleta_40p0To50p0_0p0To2p5",
        "*probe_Ele_pt_bin4*event_nPV_bin*",name+"_alleta_50p0To200p0_0p0To2p5",
        )

options = VarParsing('analysis')

options.register(
    "noData",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute data efficiencies"
    )

options.register(
    "noMC",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute MC efficiencies"
    )

options.register(
    "noID",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute efficiencies for Gsf->ID"
    )

options.register(
    "noIso",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Don't compute efficiencies for ID->ID+Iso"
    )

options.register(
    "doEta",
    False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Bin in eta instead of activity for isolation efficiencies"
    )

options.parseArguments()

if (not options.noMC) and (not options.noData):
    raise Exception("Must select either data or MC")

if (not options.noData):
    for pdf in common.all_pdfs.__dict__:
        param = common.all_pdfs.getParameter(pdf)
        if type(param) is not cms.vstring:
            continue
        i = 0
        for line in getattr(common.all_pdfs, pdf):
            if line.find("signalFractionInPassing") != -1:
                getattr(common.all_pdfs, pdf)[i] = line.replace("[1.0]","[0.9,0.,1.]")
            i = i + 1

process = cms.Process("TagProbe")
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.destinations = ['cout', 'cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

################################################
#specifies the binning of parameters
IDEfficiencyBins = cms.PSet(
    probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
    #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
    probe_sc_abseta = cms.vdouble(0., 0.8, 1.442, 1.566, 2.0, 2.5),
    )
IsoEfficiencyBins = cms.PSet()
trail = ""
if (options.doEta):
    IsoEfficiencyBins = cms.PSet(
        probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
        #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
        probe_sc_abseta = cms.vdouble(0., 0.8, 1.442, 1.566, 2.0, 2.5),
        )
    trail = "eta"
else:
    IsoEfficiencyBins = cms.PSet(
        probe_Ele_pt = cms.vdouble(10. ,20. ,30. ,40. ,50. ,200.),
        #event_nPV = cms.vdouble(0.,5.,10.,15.,20.,100.),
        probe_ele_RelAct = cms.vdouble(0., 0.02, 0.05, 0.15, 1., 99999.),
        )
    trail = "act"


def getBinningSpecification(wp, isData):
  return cms.PSet(
#   UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    UnbinnedVariables = cms.vstring("mass") if isData else cms.vstring("mass", "totWeight"),
    BinnedVariables = cms.PSet(IDEfficiencyBins, mcTrue = cms.vstring("false") if isData else cms.vstring("true")),
    BinToPDFmap = BinSpec(wp),
  )

# defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
# there will be a separate output directory for each calculation that includes a
# simultaneous fit, side band subtraction and counting.
def getEfficiencies(wp, isData):
   Efficiencies = cms.PSet()
   setattr(Efficiencies, wp if isData else "MCtruth_" + wp, 
     cms.PSet(getBinningSpecification(wp, False),
              EfficiencyCategoryAndState = cms.vstring("passing" + wp, "pass"),
     ),
   )
   return Efficiencies


McVetoBinningSpecification = getBinningSpecification("Veto", False)

McLooseBinningSpecification = McVetoBinningSpecification.clone()
McLooseBinningSpecification.BinToPDFmap = BinSpec("Loose")

McMediumBinningSpecification = McVetoBinningSpecification.clone()
McMediumBinningSpecification.BinToPDFmap = BinSpec("Medium")

McTightBinningSpecification = McVetoBinningSpecification.clone()
McTightBinningSpecification.BinToPDFmap = BinSpec("Tight")

McTight2BinningSpecification = McVetoBinningSpecification.clone()
McTight2BinningSpecification.BinToPDFmap = BinSpec("Tight2")

McLoose2DBinningSpecification = McVetoBinningSpecification.clone()
McLoose2DBinningSpecification.BinToPDFmap = BinSpec("Loose2D")

McFOID2DBinningSpecification = McVetoBinningSpecification.clone()
McFOID2DBinningSpecification.BinToPDFmap = BinSpec("FOID2D")

McTight2D3DBinningSpecification = McVetoBinningSpecification.clone()
McTight2D3DBinningSpecification.BinToPDFmap = BinSpec("Tight2D3D")

McTightID2D3DBinningSpecification = McVetoBinningSpecification.clone()
McTightID2D3DBinningSpecification.BinToPDFmap = BinSpec("TightID2D3D")

McLeptonMvaVLBinningSpecification = McVetoBinningSpecification.clone()
McLeptonMvaVLBinningSpecification.BinToPDFmap = BinSpec("LeptonMvaVL")

McLeptonMvaLBinningSpecification = McVetoBinningSpecification.clone()
McLeptonMvaLBinningSpecification.BinToPDFmap = BinSpec("LeptonMvaL")

McLeptonMvaMBinningSpecification = McVetoBinningSpecification.clone()
McLeptonMvaMBinningSpecification.BinToPDFmap = BinSpec("LeptonMvaM")

McLeptonMvaTBinningSpecification = McVetoBinningSpecification.clone()
McLeptonMvaTBinningSpecification.BinToPDFmap = BinSpec("LeptonMvaT")

McLeptonMvaVTBinningSpecification = McVetoBinningSpecification.clone()
McLeptonMvaVTBinningSpecification.BinToPDFmap = BinSpec("LeptonMvaVT")

McLeptonMvaETBinningSpecification = McVetoBinningSpecification.clone()
McLeptonMvaETBinningSpecification.BinToPDFmap = BinSpec("LeptonMvaET")

McMVAVLooseMiniBinningSpecification = cms.PSet(
#    UnbinnedVariables = cms.vstring("mass", "totWeight", "Ele_dRTau", "probe_dRTau"),
    UnbinnedVariables = cms.vstring("mass", "totWeight"),
    BinnedVariables = cms.PSet(IsoEfficiencyBins, mcTrue = cms.vstring("true")),
    BinToPDFmap = BinSpec("MVAVLooseMini"),
    )

McMVAVLooseMini4BinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVAVLooseMini4BinningSpecification.BinToPDFmap = BinSpec("MVAVLooseMini4")

McMVAVLooseConvIHit1BinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVAVLooseConvIHit1BinningSpecification.BinToPDFmap = BinSpec("MVAVLooseConvIHit1")

McMVATightConvIHit0ChgBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVATightConvIHit0ChgBinningSpecification.BinToPDFmap = BinSpec("MVATightConvIHit0Chg")

McMVATightMultiBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVATightMultiBinningSpecification.BinToPDFmap = BinSpec("MVATightMulti")

McMVATightMultiEmuBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
McMVATightMultiEmuBinningSpecification.BinToPDFmap = BinSpec("MVATightMultiEmu")

DataVetoBinningSpecification = getBinningSpecification("Veto", True)
DataVetoBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataLooseBinningSpecification = McLooseBinningSpecification.clone()
DataLooseBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLooseBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataMediumBinningSpecification = McMediumBinningSpecification.clone()
DataMediumBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMediumBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTightBinningSpecification = McTightBinningSpecification.clone()
DataTightBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTightBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTight2BinningSpecification = McTightBinningSpecification.clone()
DataTight2BinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTight2BinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataLoose2DBinningSpecification = McLoose2DBinningSpecification.clone()
DataLoose2DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLoose2DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataFOID2DBinningSpecification = McFOID2DBinningSpecification.clone()
DataFOID2DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataFOID2DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTight2D3DBinningSpecification = McTight2D3DBinningSpecification.clone()
DataTight2D3DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTight2D3DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataTightID2D3DBinningSpecification = McTightID2D3DBinningSpecification.clone()
DataTightID2D3DBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataTightID2D3DBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)
DataMVAVLooseMiniBinningSpecification = McMVAVLooseMiniBinningSpecification.clone()
DataMVAVLooseMiniBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVAVLooseMiniBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVAVLooseMini4BinningSpecification = McMVAVLooseMini4BinningSpecification.clone()
DataMVAVLooseMini4BinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVAVLooseMini4BinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVAVLooseConvIHit1BinningSpecification = McMVAVLooseConvIHit1BinningSpecification.clone()
DataMVAVLooseConvIHit1BinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVAVLooseConvIHit1BinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVATightConvIHit0ChgBinningSpecification = McMVATightConvIHit0ChgBinningSpecification.clone()
DataMVATightConvIHit0ChgBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVATightConvIHit0ChgBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVATightMultiBinningSpecification = McMVATightMultiBinningSpecification.clone()
DataMVATightMultiBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVATightMultiBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)
DataMVATightMultiEmuBinningSpecification = McMVATightMultiEmuBinningSpecification.clone()
DataMVATightMultiEmuBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataMVATightMultiEmuBinningSpecification.BinnedVariables = cms.PSet(IsoEfficiencyBins)

DataLeptonMvaVLBinningSpecification = McLeptonMvaVLBinningSpecification.clone()
DataLeptonMvaVLBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLeptonMvaVLBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)

DataLeptonMvaLBinningSpecification = McLeptonMvaLBinningSpecification.clone()
DataLeptonMvaLBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLeptonMvaLBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)

DataLeptonMvaMBinningSpecification = McLeptonMvaMBinningSpecification.clone()
DataLeptonMvaMBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLeptonMvaMBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)

DataLeptonMvaTBinningSpecification = McLeptonMvaTBinningSpecification.clone()
DataLeptonMvaTBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLeptonMvaTBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)

DataLeptonMvaVTBinningSpecification = McLeptonMvaVTBinningSpecification.clone()
DataLeptonMvaVTBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLeptonMvaVTBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)

DataLeptonMvaETBinningSpecification = McLeptonMvaETBinningSpecification.clone()
DataLeptonMvaETBinningSpecification.UnbinnedVariables = cms.vstring("mass")
DataLeptonMvaETBinningSpecification.BinnedVariables = cms.PSet(IDEfficiencyBins)

############################################################################################
############################################################################################
####### GsfElectron->Id / selection efficiency 
############################################################################################
############################################################################################

process.McGsfElectronToVeto = cms.EDAnalyzer(
    "TagProbeFitTreeAnalyzer",
    InputFileNames = cms.vstring("mc.root"),
    InputDirectoryName = cms.string("GsfElectronToID"),
    InputTreeName = cms.string("fitter_tree"), 
    OutputFileName = cms.string("eff_mc_Veto.root"),
    NumCPU = cms.uint32(6),
    SaveWorkspace = cms.bool(False), #VERY TIME CONSUMING FOR MC
    doCutAndCount = cms.bool(True),
    floatShapeParameters = cms.bool(True),
#    fixVars = cms.vstring("meanP","sigmaP","meanF","sigmaF"), # switch off fixed vars
    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(60),
    WeightVariable = cms.string("totWeight"),
    # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
    Variables = cms.PSet(
        mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
        #event_nPV = cms.vstring("Event N_{PV}", "0", "1000000", ""),
        probe_Ele_pt = cms.vstring("Probe p_{T}", "10", "200", "GeV/c"),
        probe_sc_abseta = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
        probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""),
        #tag_Ele_pt = cms.vstring("Tag p_{T}", "35.", "1000000000", "GeV/c"),
        totWeight = cms.vstring("totWeight", "0", "100000000", ""), 
#        Ele_dRTau = cms.vstring("Ele_dRTau", "0.2", "100000", ""),
#        probe_dRTau = cms.vstring("probe_dRTau", "0.2", "100000", ""),
        ),
    # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculation
    Categories = cms.PSet(
        mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
        passingVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]"),
        ),
    PDFs = common.all_pdfs,
    # defines a set of efficiency calculations, what PDF to use for fitting and how to bin the data;
    # there will be a separate output directory for each calculation that includes a
    # simultaneous fit, side band subtraction and counting.
    Efficiencies = getEfficiencies("Veto", False),
#    Efficiencies = cms.PSet(
#        MCtruth_Veto = cms.PSet(
#            getBinningSpecification("Veto", False),
#            EfficiencyCategoryAndState = cms.vstring("passingVeto", "pass"),
#            ),
#        )
    )

def getCategories(wp, isData):
    categories = cms.PSet()
    setattr(categories, "passing" + wp, cms.vstring("passing" + wp, "dummy[pass=1,fail=0]"))
    if not isData: setattr(categories, "mcTrue", cms.vstring("MC true", "dummy[true=1,false=0]"))
    return categories

def getAnalyzer(wp, dir, isData):
    analyzer = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
      InputFileNames           = cms.vstring(dataFile if isData else mcFile),
      InputDirectoryName       = cms.string(dir),
      InputTreeName            = cms.string("fitter_tree"), 
      OutputFileName           = cms.string("eff_" + ("data" if isData else "mc") + "_" + wp + ".root"),
      NumCPU                   = cms.uint32(6),
      SaveWorkspace            = cms.bool(False),       # Time comsuming/could cause crashes if set True
      doCutAndCount            = cms.bool(not isData),  # Only for MC
      floatShapeParameters     = cms.bool(True),
  #   fixVars = cms.vstring("meanP","sigmaP","meanF","sigmaF"), # switch off fixed vars
      binnedFit                = cms.bool(True),
      binsForFit               = cms.uint32(60),
      WeightVariable           = cms.string("totWeight"),

      # defines all the real variables of the probes available in the input tree and intended for use in the efficiencies
      Variables                = cms.PSet(
				    mass             = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
				    #event_nPV       = cms.vstring("Event N_{PV}", "0", "1000000", ""),
				    probe_Ele_pt     = cms.vstring("Probe p_{T}", "10", "200", "GeV/c"),
				    probe_sc_abseta  = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
				    probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""),
				    #tag_Ele_pt      = cms.vstring("Tag p_{T}", "35.", "1000000000", "GeV/c"),
				    totWeight        = cms.vstring("totWeight", "0", "100000000", ""), 
			            #Ele_dRTau       = cms.vstring("Ele_dRTau", "0.2", "100000", ""),
			            #probe_dRTau     = cms.vstring("probe_dRTau", "0.2", "100000", ""),
      ),
      # defines all the discrete variables of the probes available in the input tree and intended for use in the efficiency calculation
      Categories               = getCategories(wp, isData),
      PDFs                     = common.all_pdfs,
      Efficiencies             = getEfficiencies("Veto", False),
    )
    if isData: 
      delattr(analyzer,            "WeightVariable")
      delattr(analyzer.Variables,  "totWeight")
    return analyzer


process.McGsfElectronToVeto = getAnalyzer("Veto", "GsfElectronToID", False)

process.McGsfElectronToLoose = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLoose.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLoose.OutputFileName = cms.string("eff_mc_Loose.root")
process.McGsfElectronToLoose.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLoose.Efficiencies = cms.PSet(
    MCtruth_Loose = cms.PSet(
        McLooseBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose", "pass"),
        ),
    )

process.McGsfElectronToMedium = process.McGsfElectronToVeto.clone()
process.McGsfElectronToMedium.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToMedium.OutputFileName = cms.string("eff_mc_Medium.root")
process.McGsfElectronToMedium.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToMedium.Efficiencies = cms.PSet(
    MCtruth_Medium = cms.PSet(
        McMediumBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
        ),
    )

process.McGsfElectronToTight = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTight.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToTight.OutputFileName = cms.string("eff_mc_Tight.root")
process.McGsfElectronToTight.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTight.Efficiencies = cms.PSet(
    MCtruth_Tight = cms.PSet(
        McTightBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )

process.McGsfElectronToTight2 = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTight2.InputDirectoryName = cms.string("GsfElectronToEleID")
process.McGsfElectronToTight2.OutputFileName = cms.string("eff_mc_Tight2.root")
process.McGsfElectronToTight2.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTight2.Efficiencies = cms.PSet(
    MCtruth_Tight = cms.PSet(
        McTight2BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )



process.McGsfElectronToLeptonMvaVL = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLeptonMvaVL.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLeptonMvaVL.OutputFileName = cms.string("eff_mc_LeptonMvaVL.root")
process.McGsfElectronToLeptonMvaVL.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLeptonMvaVL = cms.vstring("passingLeptonMvaVL", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLeptonMvaVL.Efficiencies = cms.PSet(
    MCtruth_LeptonMvaVL = cms.PSet(
        McLeptonMvaVLBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaVL", "pass"),
        ),
    )


process.McGsfElectronToLeptonMvaL = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLeptonMvaL.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLeptonMvaL.OutputFileName = cms.string("eff_mc_LeptonMvaL.root")
process.McGsfElectronToLeptonMvaL.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLeptonMvaL = cms.vstring("passingLeptonMvaL", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLeptonMvaL.Efficiencies = cms.PSet(
    MCtruth_LeptonMvaL = cms.PSet(
        McLeptonMvaLBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaL", "pass"),
        ),
    )


process.McGsfElectronToLeptonMvaM = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLeptonMvaM.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLeptonMvaM.OutputFileName = cms.string("eff_mc_LeptonMvaM.root")
process.McGsfElectronToLeptonMvaM.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLeptonMvaM = cms.vstring("passingLeptonMvaM", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLeptonMvaM.Efficiencies = cms.PSet(
    MCtruth_LeptonMvaM = cms.PSet(
        McLeptonMvaMBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaM", "pass"),
        ),
    )


process.McGsfElectronToLeptonMvaT = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLeptonMvaT.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLeptonMvaT.OutputFileName = cms.string("eff_mc_LeptonMvaT.root")
process.McGsfElectronToLeptonMvaT.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLeptonMvaT = cms.vstring("passingLeptonMvaT", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLeptonMvaT.Efficiencies = cms.PSet(
    MCtruth_LeptonMvaT = cms.PSet(
        McLeptonMvaTBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaT", "pass"),
        ),
    )


process.McGsfElectronToLeptonMvaVT = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLeptonMvaVT.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLeptonMvaVT.OutputFileName = cms.string("eff_mc_LeptonMvaVT.root")
process.McGsfElectronToLeptonMvaVT.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLeptonMvaVT = cms.vstring("passingLeptonMvaVT", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLeptonMvaVT.Efficiencies = cms.PSet(
    MCtruth_LeptonMvaVT = cms.PSet(
        McLeptonMvaVTBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaVT", "pass"),
        ),
    )


process.McGsfElectronToLeptonMvaET = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLeptonMvaET.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLeptonMvaET.OutputFileName = cms.string("eff_mc_LeptonMvaET.root")
process.McGsfElectronToLeptonMvaET.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLeptonMvaET = cms.vstring("passingLeptonMvaET", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLeptonMvaET.Efficiencies = cms.PSet(
    MCtruth_LeptonMvaET = cms.PSet(
        McLeptonMvaETBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaET", "pass"),
        ),
    )





process.McGsfElectronToLoose2D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToLoose2D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToLoose2D.OutputFileName = cms.string("eff_mc_Loose2D.root")
process.McGsfElectronToLoose2D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingLoose2D = cms.vstring("passingLoose2D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToLoose2D.Efficiencies = cms.PSet(
    MCtruth_Loose2D = cms.PSet(
        McLoose2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose2D", "pass"),
        ),
    )

process.McGsfElectronToFOID2D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToFOID2D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToFOID2D.OutputFileName = cms.string("eff_mc_FOID2D3D.root")
process.McGsfElectronToFOID2D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingFOID2D = cms.vstring("passingFOID2D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToFOID2D.Efficiencies = cms.PSet(
    MCtruth_FOID2D = cms.PSet(
        McFOID2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingFOID2D", "pass"),
        ),
    )

process.McGsfElectronToTight2D3D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTight2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToTight2D3D.OutputFileName = cms.string("eff_mc_Tight2D3D.root")
process.McGsfElectronToTight2D3D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTight2D3D = cms.vstring("passingTight2D3D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTight2D3D.Efficiencies = cms.PSet(
    MCtruth_Tight2D3D = cms.PSet(
        McTight2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight2D3D", "pass"),
        ),
    )

process.McGsfElectronToTightID2D3D = process.McGsfElectronToVeto.clone()
process.McGsfElectronToTightID2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.McGsfElectronToTightID2D3D.OutputFileName = cms.string("eff_mc_TightID2D3D.root")
process.McGsfElectronToTightID2D3D.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingTightID2D3D = cms.vstring("passingTightID2D3D", "dummy[pass=1,fail=0]"),
    )
process.McGsfElectronToTightID2D3D.Efficiencies = cms.PSet(
    MCtruth_TightID2D3D = cms.PSet(
        McTightID2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTightID2D3D", "pass"),
        ),
    )

process.McMVAVLooseElectronToMini = process.McGsfElectronToMedium.clone()
process.McMVAVLooseElectronToMini.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.McMVAVLooseElectronToMini.OutputFileName = cms.string("eff_mc_mvavLoosemini_"+trail+".root")
process.McMVAVLooseElectronToMini.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"),
    )
process.McMVAVLooseElectronToMini.Efficiencies = cms.PSet(
    MCtruth_Mini = cms.PSet(
        McMVAVLooseMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.McMVAVLooseElectronToMini4 = process.McMVAVLooseElectronToMini.clone()
process.McMVAVLooseElectronToMini4.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.McMVAVLooseElectronToMini4.OutputFileName = cms.string("eff_mc_mvavLoosemini4_"+trail+".root")
process.McMVAVLooseElectronToMini4.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"),
    )
process.McMVAVLooseElectronToMini4.Efficiencies = cms.PSet(
    MCtruth_Mini4 = cms.PSet(
        McMVAVLooseMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.McMVAVLooseElectronToConvIHit1 = process.McMVAVLooseElectronToMini.clone()
process.McMVAVLooseElectronToConvIHit1.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.McMVAVLooseElectronToConvIHit1.OutputFileName = cms.string("eff_mc_mvavLooseconvihit1_"+trail+".root")
process.McMVAVLooseElectronToConvIHit1.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingConvIHit1 = cms.vstring("passingConvIHit1", "dummy[pass=1,fail=0]"),
    )
process.McMVAVLooseElectronToConvIHit1.Efficiencies = cms.PSet(
    MCtruth_ConvIHit1 = cms.PSet(
        McMVAVLooseConvIHit1BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit1", "pass"),
        ),
    )

process.McMVATightElectronToConvIHit0Chg = process.McMVAVLooseElectronToMini.clone()
process.McMVATightElectronToConvIHit0Chg.InputDirectoryName = cms.string("MVATightElectronToIso")
process.McMVATightElectronToConvIHit0Chg.OutputFileName = cms.string("eff_mc_mvaTightconvihit0chg_"+trail+".root")
process.McMVATightElectronToConvIHit0Chg.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingConvIHit0Chg = cms.vstring("passingConvIHit0Chg", "dummy[pass=1,fail=0]"),
    )
process.McMVATightElectronToConvIHit0Chg.Efficiencies = cms.PSet(
    MCtruth_ConvIHit0Chg = cms.PSet(
        McMVATightConvIHit0ChgBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit0Chg", "pass"),
        ),
    )

process.McMVATightElectronToMulti = process.McMVAVLooseElectronToMini.clone()
process.McMVATightElectronToMulti.InputDirectoryName = cms.string("MVATightElectronToIso")
process.McMVATightElectronToMulti.OutputFileName = cms.string("eff_mc_mvaTightmulti_"+trail+".root")
process.McMVATightElectronToMulti.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMultiIso = cms.vstring("passingMultiIso", "dummy[pass=1,fail=0]"),
    )
process.McMVATightElectronToMulti.Efficiencies = cms.PSet(
    MCtruth_Multi = cms.PSet(
        McMVATightMultiBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIso", "pass"),
        ),
    )

process.McMVATightElectronToMultiEmu = process.McMVAVLooseElectronToMini.clone()
process.McMVATightElectronToMultiEmu.InputDirectoryName = cms.string("MVATightElectronToIso")
process.McMVATightElectronToMultiEmu.OutputFileName = cms.string("eff_mc_mvaTightmultiemu_"+trail+".root")
process.McMVATightElectronToMultiEmu.Categories = cms.PSet(
    mcTrue = cms.vstring("MC true", "dummy[true=1,false=0]"),
    passingMultiIsoEmu = cms.vstring("passingMultiIsoEmu", "dummy[pass=1,fail=0]"),
    )
process.McMVATightElectronToMultiEmu.Efficiencies = cms.PSet(
    MCtruth_MultiEmu = cms.PSet(
        McMVATightMultiEmuBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIsoEmu", "pass"),
        ),
    )

process.DataGsfElectronToVeto = process.McGsfElectronToVeto.clone()
process.DataGsfElectronToVeto.InputFileNames = cms.vstring("data.root")
process.DataGsfElectronToVeto.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToVeto.OutputFileName = cms.string("eff_data_Veto.root")
process.DataGsfElectronToVeto.doCutAndCount = cms.bool(False)
delattr(process.DataGsfElectronToVeto, "WeightVariable")
process.DataGsfElectronToVeto.Variables = cms.PSet(
    mass = cms.vstring("Tag-Probe Mass", "60.0", "120.0", "GeV/c^{2}"),
    #event_nPV = cms.vstring("Event N_{PV}", "0", "1000000", ""),
    probe_Ele_pt = cms.vstring("Probe p_{T}", "10", "200", "GeV/c"),
    probe_sc_abseta = cms.vstring("Probe |#eta|", "0", "2.5", ""), 
    #tag_Ele_pt = cms.vstring("Tag p_{T}", "35.", "1000000000", "GeV/c"),
    probe_ele_RelAct = cms.vstring("Probe Activity", "0", "100000000", ""), 
    )
process.DataGsfElectronToVeto.Categories = cms.PSet(passingVeto = cms.vstring("passingVeto", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToVeto.Efficiencies = cms.PSet(
    Veto = cms.PSet(
        DataVetoBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingVeto", "pass"),
        ),
    )

process.DataGsfElectronToLoose = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLoose.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLoose.OutputFileName = cms.string("eff_data_Loose.root")
process.DataGsfElectronToLoose.Categories = cms.PSet(passingLoose = cms.vstring("passingLoose", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLoose.Efficiencies = cms.PSet(
    Loose = cms.PSet(
        DataLooseBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose", "pass"),
        ),
    )

process.DataGsfElectronToMedium = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToMedium.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToMedium.OutputFileName = cms.string("eff_data_Medium.root")
process.DataGsfElectronToMedium.Categories = cms.PSet(passingMedium = cms.vstring("passingMedium", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToMedium.Efficiencies = cms.PSet(
    Medium = cms.PSet(
        DataMediumBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMedium", "pass"),
        ),
    )

process.DataGsfElectronToTight = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTight.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToTight.OutputFileName = cms.string("eff_data_Tight.root")
process.DataGsfElectronToTight.Categories = cms.PSet(passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTight.Efficiencies = cms.PSet(
    Tight = cms.PSet(
        DataTightBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )

process.DataGsfElectronToTight2 = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTight2.InputDirectoryName = cms.string("GsfElectronToEleID")
process.DataGsfElectronToTight2.OutputFileName = cms.string("eff_data_Tight2.root")
process.DataGsfElectronToTight2.Categories = cms.PSet(passingTight = cms.vstring("passingTight", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTight2.Efficiencies = cms.PSet(
    Tight = cms.PSet(
        DataTight2BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight", "pass"),
        ),
    )



process.DataGsfElectronToLeptonMvaVL = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLeptonMvaVL.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLeptonMvaVL.OutputFileName = cms.string("eff_data_LeptonMvaVL.root")
process.DataGsfElectronToLeptonMvaVL.Categories = cms.PSet(passingLeptonMvaVL = cms.vstring("passingLeptonMvaVL", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLeptonMvaVL.Efficiencies = cms.PSet(
    LeptonMvaVL = cms.PSet(
        DataLeptonMvaVLBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaVL", "pass"),
        ),
    )


process.DataGsfElectronToLeptonMvaL = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLeptonMvaL.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLeptonMvaL.OutputFileName = cms.string("eff_data_LeptonMvaL.root")
process.DataGsfElectronToLeptonMvaL.Categories = cms.PSet(passingLeptonMvaL = cms.vstring("passingLeptonMvaL", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLeptonMvaL.Efficiencies = cms.PSet(
    LeptonMvaL = cms.PSet(
        DataLeptonMvaLBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaL", "pass"),
        ),
    )


process.DataGsfElectronToLeptonMvaM = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLeptonMvaM.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLeptonMvaM.OutputFileName = cms.string("eff_data_LeptonMvaM.root")
process.DataGsfElectronToLeptonMvaM.Categories = cms.PSet(passingLeptonMvaM = cms.vstring("passingLeptonMvaM", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLeptonMvaM.Efficiencies = cms.PSet(
    LeptonMvaM = cms.PSet(
        DataLeptonMvaMBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaM", "pass"),
        ),
    )


process.DataGsfElectronToLeptonMvaT = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLeptonMvaT.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLeptonMvaT.OutputFileName = cms.string("eff_data_LeptonMvaT.root")
process.DataGsfElectronToLeptonMvaT.Categories = cms.PSet(passingLeptonMvaT = cms.vstring("passingLeptonMvaT", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLeptonMvaT.Efficiencies = cms.PSet(
    LeptonMvaT = cms.PSet(
        DataLeptonMvaTBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaT", "pass"),
        ),
    )


process.DataGsfElectronToLeptonMvaVT = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLeptonMvaVT.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLeptonMvaVT.OutputFileName = cms.string("eff_data_LeptonMvaVT.root")
process.DataGsfElectronToLeptonMvaVT.Categories = cms.PSet(passingLeptonMvaVT = cms.vstring("passingLeptonMvaVT", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLeptonMvaVT.Efficiencies = cms.PSet(
    LeptonMvaVT = cms.PSet(
        DataLeptonMvaVTBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaVT", "pass"),
        ),
    )

process.DataGsfElectronToLeptonMvaET = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLeptonMvaET.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLeptonMvaET.OutputFileName = cms.string("eff_data_LeptonMvaET.root")
process.DataGsfElectronToLeptonMvaET.Categories = cms.PSet(passingLeptonMvaET = cms.vstring("passingLeptonMvaET", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLeptonMvaET.Efficiencies = cms.PSet(
    LeptonMvaET = cms.PSet(
        DataLeptonMvaETBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLeptonMvaET", "pass"),
        ),
    )






process.DataGsfElectronToLoose2D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToLoose2D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToLoose2D.OutputFileName = cms.string("eff_data_Loose2D.root")
process.DataGsfElectronToLoose2D.Categories = cms.PSet(passingLoose2D = cms.vstring("passingLoose2D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToLoose2D.Efficiencies = cms.PSet(
    Loose2D = cms.PSet(
        DataLoose2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingLoose2D", "pass"),
        ),
    )

process.DataGsfElectronToFOID2D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToFOID2D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToFOID2D.OutputFileName = cms.string("eff_data_FOID2D3D.root")
process.DataGsfElectronToFOID2D.Categories = cms.PSet(passingFOID2D = cms.vstring("passingFOID2D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToFOID2D.Efficiencies = cms.PSet(
    FOID2D = cms.PSet(
        DataFOID2DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingFOID2D", "pass"),
        ),
    )

process.DataGsfElectronToTight2D3D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTight2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToTight2D3D.OutputFileName = cms.string("eff_data_Tight2D3D.root")
process.DataGsfElectronToTight2D3D.Categories = cms.PSet(passingTight2D3D = cms.vstring("passingTight2D3D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTight2D3D.Efficiencies = cms.PSet(
    Tight2D3D = cms.PSet(
        DataTight2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTight2D3D", "pass"),
        ),
    )

process.DataGsfElectronToTightID2D3D = process.DataGsfElectronToVeto.clone()
process.DataGsfElectronToTightID2D3D.InputDirectoryName = cms.string("GsfElectronToID")
process.DataGsfElectronToTightID2D3D.OutputFileName = cms.string("eff_data_TightID2D3D.root")
process.DataGsfElectronToTightID2D3D.Categories = cms.PSet(passingTightID2D3D = cms.vstring("passingTightID2D3D", "dummy[pass=1,fail=0]"))
process.DataGsfElectronToTightID2D3D.Efficiencies = cms.PSet(
    TightID2D3D = cms.PSet(
        DataTightID2D3DBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingTightID2D3D", "pass"),
        ),
    )

process.DataMVAVLooseElectronToMini = process.DataGsfElectronToVeto.clone()
process.DataMVAVLooseElectronToMini.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToMini.OutputFileName = cms.string("eff_data_mvavLoosemini_"+trail+".root")
process.DataMVAVLooseElectronToMini.Categories = cms.PSet(passingMini = cms.vstring("passingMini", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToMini.Efficiencies = cms.PSet(
    Mini = cms.PSet(
        DataMVAVLooseMiniBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini", "pass"),
        ),
    )

process.DataMVAVLooseElectronToMini4 = process.DataMVAVLooseElectronToMini.clone()
process.DataMVAVLooseElectronToMini4.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToMini4.OutputFileName = cms.string("eff_data_mvavLoosemini4_"+trail+".root")
process.DataMVAVLooseElectronToMini4.Categories = cms.PSet(passingMini4 = cms.vstring("passingMini4", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToMini4.Efficiencies = cms.PSet(
    Mini4 = cms.PSet(
        DataMVAVLooseMini4BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMini4", "pass"),
        ),
    )

process.DataMVAVLooseElectronToConvIHit1 = process.DataMVAVLooseElectronToMini.clone()
process.DataMVAVLooseElectronToConvIHit1.InputDirectoryName = cms.string("MVAVLooseElectronToIso")
process.DataMVAVLooseElectronToConvIHit1.OutputFileName = cms.string("eff_data_mvavLooseconvihit1_"+trail+".root")
process.DataMVAVLooseElectronToConvIHit1.Categories = cms.PSet(passingConvIHit1 = cms.vstring("passingConvIHit1", "dummy[pass=1,fail=0]"))
process.DataMVAVLooseElectronToConvIHit1.Efficiencies = cms.PSet(
    ConvIHit1 = cms.PSet(
        DataMVAVLooseConvIHit1BinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit1", "pass"),
        ),
    )

process.DataMVATightElectronToConvIHit0Chg = process.DataMVAVLooseElectronToMini.clone()
process.DataMVATightElectronToConvIHit0Chg.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToConvIHit0Chg.OutputFileName = cms.string("eff_data_mvaTightconvihit0chg_"+trail+".root")
process.DataMVATightElectronToConvIHit0Chg.Categories = cms.PSet(passingConvIHit0Chg = cms.vstring("passingConvIHit0Chg", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToConvIHit0Chg.Efficiencies = cms.PSet(
    ConvIHit0Chg = cms.PSet(
        DataMVATightConvIHit0ChgBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingConvIHit0Chg", "pass"),
        ),
    )

process.DataMVATightElectronToMulti = process.DataMVAVLooseElectronToMini.clone()
process.DataMVATightElectronToMulti.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToMulti.OutputFileName = cms.string("eff_data_mvaTightmulti_"+trail+".root")
process.DataMVATightElectronToMulti.Categories = cms.PSet(passingMultiIso = cms.vstring("passingMultiIso", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToMulti.Efficiencies = cms.PSet(
    Multi = cms.PSet(
        DataMVATightMultiBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIso", "pass"),
        ),
    )

process.DataMVATightElectronToMultiEmu = process.DataMVAVLooseElectronToMini.clone()
process.DataMVATightElectronToMultiEmu.InputDirectoryName = cms.string("MVATightElectronToIso")
process.DataMVATightElectronToMultiEmu.OutputFileName = cms.string("eff_data_mvaTightmultiemu_"+trail+".root")
process.DataMVATightElectronToMultiEmu.Categories = cms.PSet(passingMultiIsoEmu = cms.vstring("passingMultiIsoEmu", "dummy[pass=1,fail=0]"))
process.DataMVATightElectronToMultiEmu.Efficiencies = cms.PSet(
    MultiEmu = cms.PSet(
        DataMVATightMultiEmuBinningSpecification,
        EfficiencyCategoryAndState = cms.vstring("passingMultiIsoEmu", "pass"),
        ),
    )

process.seq = cms.Sequence()

if (not options.noMC) and (not options.noID):
    process.seq += process.McGsfElectronToVeto
    process.seq += process.McGsfElectronToLoose
    process.seq += process.McGsfElectronToMedium
    process.seq += process.McGsfElectronToTight
#    process.seq += process.McGsfElectronToTight2 # this was attempt to check passingTight in GsfElectronToEleID but turned out to be the same as in GsfElectronToID
#    process.seq += process.McGsfElectronToLeptonMvaVL
#    process.seq += process.McGsfElectronToLeptonMvaL
    process.seq += process.McGsfElectronToLeptonMvaM
#    process.seq += process.McGsfElectronToLeptonMvaT
    process.seq += process.McGsfElectronToLeptonMvaVT
#    process.seq += process.McGsfElectronToLeptonMvaET
    process.seq += process.McGsfElectronToLoose2D
    process.seq += process.McGsfElectronToFOID2D
    process.seq += process.McGsfElectronToTight2D3D
    process.seq += process.McGsfElectronToTightID2D3D

if (not options.noMC) and (not options.noIso):
    process.seq += process.McMVAVLooseElectronToMini
    process.seq += process.McMVAVLooseElectronToMini4
    process.seq += process.McMVAVLooseElectronToConvIHit1
    process.seq += process.McMVATightElectronToConvIHit0Chg
    process.seq += process.McMVATightElectronToMulti
    process.seq += process.McMVATightElectronToMultiEmu

if (not options.noData) and (not options.noID):
    process.seq += process.DataGsfElectronToVeto
    process.seq += process.DataGsfElectronToLoose
    process.seq += process.DataGsfElectronToMedium
    process.seq += process.DataGsfElectronToTight
#    process.seq += process.DataGsfElectronToTight2
#    process.seq += process.DataGsfElectronToLeptonMvaVL
#    process.seq += process.DataGsfElectronToLeptonMvaL
    process.seq += process.DataGsfElectronToLeptonMvaM
#    process.seq += process.DataGsfElectronToLeptonMvaT
    process.seq += process.DataGsfElectronToLeptonMvaVT
#    process.seq += process.DataGsfElectronToLeptonMvaET
    process.seq += process.DataGsfElectronToLoose2D
    process.seq += process.DataGsfElectronToFOID2D
    process.seq += process.DataGsfElectronToTight2D3D
    process.seq += process.DataGsfElectronToTightID2D3D

if (not options.noData) and (not options.noIso):
    process.seq += process.DataMVAVLooseElectronToMini
    process.seq += process.DataMVAVLooseElectronToMini4
    process.seq += process.DataMVAVLooseElectronToConvIHit1
    process.seq += process.DataMVATightElectronToConvIHit0Chg
    process.seq += process.DataMVATightElectronToMulti
    process.seq += process.DataMVATightElectronToMultiEmu

process.fit = cms.Path(process.seq)
