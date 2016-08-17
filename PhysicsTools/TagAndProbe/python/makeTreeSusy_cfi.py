import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *


def AddMiniIso(process, options, varOptions):
    process.load("JetMETCorrections.Configuration.JetCorrectors_cff")


    process.ElectronIsolation =  cms.EDProducer(
        "CITKPFIsolationSumProducer",
        srcToIsolate = cms.InputTag("slimmedElectrons"),
        srcForIsolationCone = cms.InputTag('packedPFCandidates'),
        isolationConeDefinitions = cms.VPSet(
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                VetoConeSizeEndcaps = cms.double(0.015),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h+'),
                miniAODVertexCodes = cms.vuint32(2,3),
            ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                VetoConeSizeEndcaps = cms.double(0.0),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h0'),
                miniAODVertexCodes = cms.vuint32(2,3),
            ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                VetoConeSizeEndcaps = cms.double(0.08),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('gamma'),
                miniAODVertexCodes = cms.vuint32(2,3),
            ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                ActivityConeSize = cms.double(0.4),
                VetoConeSizeEndcaps = cms.double(0.015),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h+'),
                miniAODVertexCodes = cms.vuint32(2,3),
            ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                ActivityConeSize = cms.double(0.4),
                VetoConeSizeEndcaps = cms.double(0.0),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('h0'),
                miniAODVertexCodes = cms.vuint32(2,3),
            ),
            cms.PSet(
                isolationAlgo = cms.string('ElectronMiniIsolationWithConeVeto'),
                coneSize = cms.double(0.2),
                MinConeSize = cms.double(0.05),
                ktScale = cms.double(10.),
                ActivityConeSize = cms.double(0.4),
                VetoConeSizeEndcaps = cms.double(0.08),
                VetoConeSizeBarrel = cms.double(0.0),
                isolateAgainst = cms.string('gamma'),
                miniAODVertexCodes = cms.vuint32(2,3),
            ),
        ),
    )

    process.jetConverter = cms.EDProducer("JetConverter",
        jets = cms.InputTag("slimmedJets")
    )

    process.jetAwareCleaner = cms.EDProducer("JetAwareCleaner",
        RawJetCollection   = cms.InputTag("jetConverter"),
        LeptonCollection   = cms.InputTag(options['ELECTRON_COLL']),
        L1Corrector        = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
        L1L2L3ResCorrector = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
        dRmax              = cms.double(0.4),
        dRCandProbeVeto    = cms.double(0.0001)
    )
    
    process.AddLeptonJetRelatedVariables = cms.EDProducer("AddLeptonJetRelatedVariables",
	JetCollection         = cms.InputTag("jetAwareCleaner"),
	JetCollectionWithCSV  = cms.InputTag("slimmedJets"),
	pfCandidates          = cms.InputTag("packedPFCandidates"),
	LeptonCollection      = cms.InputTag(options['ELECTRON_COLL']),
	dRmax                 = cms.double(0.4),
	subLepFromJetForPtRel = cms.bool(True)
    )


    process.MyEleVars = cms.EDProducer(
        "MyElectronVariableHelper",
        probes         = cms.InputTag(options['ELECTRON_COLL']),
        mvas           = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        dxy            = cms.InputTag("eleVarHelper:dxy"),
        dz             = cms.InputTag("eleVarHelper:dz"),
        miniIso        = cms.InputTag("relminiiso:sum"),
        chargedMiniIso = cms.InputTag("relminiiso:charged"),
        neutralMiniIso = cms.InputTag("relminiiso:neutral"),
        jetPtRatio     = cms.InputTag("AddLeptonJetRelatedVariables","JetPtRatio"),
        jetPtRel       = cms.InputTag("AddLeptonJetRelatedVariables","JetPtRel"),
        jetNDauCharged = cms.InputTag("AddLeptonJetRelatedVariables","JetNDauCharged"),
        jetBTagCSV     = cms.InputTag("AddLeptonJetRelatedVariables","JetBTagCSV"),
        eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium"),
        eleTightIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-tight"),
    )

    MiniIsoProbeVars = cms.PSet(
        process.GsfElectronToEleID.variables,
        probe_ele_Mini = cms.InputTag("relminiiso:sum"),
        probe_ele_chargedMini = cms.InputTag("relminiiso:charged"),
        probe_ele_neutralMini = cms.InputTag("relminiiso:neutral"),
        probe_ele_JetPtRatio     = cms.InputTag("AddLeptonJetRelatedVariables:JetPtRatio"),
        probe_ele_JetPtRel       = cms.InputTag("AddLeptonJetRelatedVariables:JetPtRel"),
        probe_ele_JetNDauCharged = cms.InputTag("AddLeptonJetRelatedVariables:JetNDauCharged"),
        probe_ele_JetBTagCSV     = cms.InputTag("AddLeptonJetRelatedVariables:JetBTagCSV"),
        probe_ele_sip3d = cms.InputTag("MyEleVars:sip3d"),
        probe_ele_ecalIso = cms.InputTag("MyEleVars:ecalIso"),
        probe_ele_hcalIso = cms.InputTag("MyEleVars:hcalIso"),
        probe_ele_trackIso = cms.InputTag("MyEleVars:trackIso"),
        probe_ele_missIHits = cms.InputTag("MyEleVars:missIHits"),
        probe_ele_passConvVeto = cms.InputTag("MyEleVars:passConvVeto"),
        probe_ele_passMVAVLooseFO = cms.InputTag("MyEleVars:passMVAVLooseFO"),
        probe_ele_passMVAVLoose = cms.InputTag("MyEleVars:passMVAVLoose"),
        probe_ele_passMVATight = cms.InputTag("MyEleVars:passMVATight"),
        probe_ele_passMVAWP80 = cms.InputTag("MyEleVars:passMVAWP80"),
        probe_ele_passMVAWP90 = cms.InputTag("MyEleVars:passMVAWP90"),
        probe_ele_passTightIP2D = cms.InputTag("MyEleVars:passTightIP2D"),
        probe_ele_passTightIP3D = cms.InputTag("MyEleVars:passTightIP3D"),
        probe_ele_passIDEmu = cms.InputTag("MyEleVars:passIDEmu"),
        probe_ele_passISOEmu = cms.InputTag("MyEleVars:passISOEmu"),
        probe_ele_passCharge = cms.InputTag("MyEleVars:passCharge"),
        probe_ele_passIHit0 = cms.InputTag("MyEleVars:passIHit0"),
        probe_ele_passIHit1 = cms.InputTag("MyEleVars:passIHit1"),
        probe_ele_passLoose2D = cms.InputTag("MyEleVars:passLoose2D"),
        probe_ele_passFOID2D = cms.InputTag("MyEleVars:passFOID2D"),
        probe_ele_passTight2D3D = cms.InputTag("MyEleVars:passTight2D3D"),
        probe_ele_passTightID2D3D = cms.InputTag("MyEleVars:passTightID2D3D"),
        probe_ele_passConvIHit1 = cms.InputTag("MyEleVars:passConvIHit1"),
        probe_ele_passConvIHit0 = cms.InputTag("MyEleVars:passConvIHit0"),
        probe_ele_passTightConvIHit0 = cms.InputTag("MyEleVars:passTightConvIHit0"),
        probe_ele_passMultiIsoM = cms.InputTag("MyEleVars:passMultiIsoM"),
        probe_ele_passMultiIsoT = cms.InputTag("MyEleVars:passMultiIsoT"),
        probe_ele_passMultiIsoVT = cms.InputTag("MyEleVars:passMultiIsoVT"),
        probe_ele_passMultiIsoEmu = cms.InputTag("MyEleVars:passMultiIsoEmu"),
        probe_ele_passLeptonMvaVL = cms.InputTag("MyEleVars:passLeptonMvaVL"),
        probe_ele_passLeptonMvaL = cms.InputTag("MyEleVars:passLeptonMvaL"),
        probe_ele_passLeptonMvaM = cms.InputTag("MyEleVars:passLeptonMvaM"),
        probe_ele_passLeptonMvaT = cms.InputTag("MyEleVars:passLeptonMvaT"),
        probe_ele_passLeptonMvaVT = cms.InputTag("MyEleVars:passLeptonMvaVT"),
        probe_ele_passLeptonMvaET = cms.InputTag("MyEleVars:passLeptonMvaET"),
        probe_ele_passCutBasedTTZ = cms.InputTag("MyEleVars:passCutBasedTTZ"),
        probe_ele_passCutBasedIllia = cms.InputTag("MyEleVars:passCutBasedIllia"),
        probe_ele_passLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("MyEleVars:passLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04"),
        probe_ele_passLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("MyEleVars:passLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04"),
    )

    setupAllVIDIdsInModule(process,
                           'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_Mini_V1_cff',
                           setupVIDElectronSelection)

    process.relminiiso =  cms.EDProducer("IsolationSum",
        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
        rho                = cms.InputTag("fixedGridRhoFastjetAll"),
        candidates         = cms.InputTag("packedPFCandidates"),
        probes             = cms.InputTag("slimmedElectrons"),
        minRadius          = cms.double(0.05),
        maxRadius          = cms.double(0.2),
        ktScale            = cms.double(10.),
    )

    process.iso_sums = cms.Sequence(
        process.relminiiso
    )                                   

    process.my_ele_sequence = cms.Sequence()

    def getGoodElectronsPROBE(name, inputTag):
      temp = process.goodElectronsPROBECutBasedVeto.clone()
      temp.selection = cms.InputTag(inputTag)
      setattr(process, 'goodElectronsPROBE' + name, temp)
      process.my_ele_sequence += temp

    #Applies probe cuts and WP (numerators and denominators both need to be listed here)
    getGoodElectronsPROBE('CutBasedNoIsoVeto', "egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-veto")
    getGoodElectronsPROBE('CutBasedNoIsoLoose', "egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-loose")
    getGoodElectronsPROBE('CutBasedNoIsoMedium', "egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-medium")
    getGoodElectronsPROBE('CutBasedNoIsoTight', "egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-tight")
    getGoodElectronsPROBE('CutBasedMiniMedium', "egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium")
    getGoodElectronsPROBE('CutBasedMini4Medium', "egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-medium")
    getGoodElectronsPROBE('MVAVLooseFO', "MyEleVars:passMVAVLooseFO")
    getGoodElectronsPROBE('MVAVLoose', "MyEleVars:passMVAVLoose")
    getGoodElectronsPROBE('MVATight', "MyEleVars:passMVATight")
    getGoodElectronsPROBE('MVAWP80', "MyEleVars:passMVAWP80")
    getGoodElectronsPROBE('MVAWP90', "MyEleVars:passMVAWP90")
    getGoodElectronsPROBE('Mini', "MyEleVars:passMini")
    getGoodElectronsPROBE('Mini2', "MyEleVars:passMini2")
    getGoodElectronsPROBE('Mini4', "MyEleVars:passMini4")
    getGoodElectronsPROBE('MiniMVAVLoose', "MyEleVars:passMVAVLooseMini")
    getGoodElectronsPROBE('Mini2MVAVLoose', "MyEleVars:passMVAVLooseMini2")
    getGoodElectronsPROBE('Mini4MVAVLoose', "MyEleVars:passMVAVLooseMini4")
    getGoodElectronsPROBE('Loose2D', "MyEleVars:passLoose2D")
    getGoodElectronsPROBE('FOID2D', "MyEleVars:passFOID2D")
    getGoodElectronsPROBE('Tight2D3D', "MyEleVars:passTight2D3D")
    getGoodElectronsPROBE('TightID2D3D', "MyEleVars:passTightID2D3D")
    getGoodElectronsPROBE('ConvIHit1', "MyEleVars:passConvIHit1")
    getGoodElectronsPROBE('ConvIHit0', "MyEleVars:passConvIHit0")
    getGoodElectronsPROBE('TightConvIHit0', "MyEleVars:passTightConvIHit0")
    getGoodElectronsPROBE('ConvIHit0Chg', "MyEleVars:passConvIHit0Chg")
    getGoodElectronsPROBE('MultiIsoM', "MyEleVars:passMultiIsoM")
    getGoodElectronsPROBE('MultiIsoT', "MyEleVars:passMultiIsoT")
    getGoodElectronsPROBE('MultiIsoVT', "MyEleVars:passMultiIsoVT")
    getGoodElectronsPROBE('MultiIsoEmu', "MyEleVars:passMultiIsoEmu")
    getGoodElectronsPROBE('LeptonMvaM', "MyEleVars:passLeptonMvaM")
    getGoodElectronsPROBE('LeptonMvaVT', "MyEleVars:passLeptonMvaVT")
    getGoodElectronsPROBE('CutBasedTTZ', "MyEleVars:passCutBasedTTZ")
    getGoodElectronsPROBE('CutBasedIllia', "MyEleVars:passCutBasedIllia")
    getGoodElectronsPROBE('CutBasedStopsDilepton', "MyEleVars:passCutBasedStopsDilepton")
    getGoodElectronsPROBE('LeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04', "MyEleVars:passLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04")
    getGoodElectronsPROBE('LeptonMvaMIDEmuTightIP2DSIP3D8miniIso04', "MyEleVars:passLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04")

    def getAllProbes(name, inputTag):
      temp = process.goodElectronsTagHLT.clone()
      temp.isAND = cms.bool(False)
      temp.selection = cms.InputTag(inputTag)
      setattr(process, 'goodElectronsProbe' + name, temp)
      process.my_ele_sequence += temp

    #Applies trigger matching (denominators need to be listed here)
    getAllProbes('MediumNoIso', "goodElectronsPROBECutBasedNoIsoMedium")
    getAllProbes('Loose2D', "goodElectronsPROBELoose2D")
    getAllProbes('MVATightID2D3D', "goodElectronsPROBETightID2D3D")
    getAllProbes('MVATight2D3D', "goodElectronsPROBETight2D3D")
    getAllProbes('CutBasedNoIsoVeto', "goodElectronsPROBECutBasedNoIsoVeto")
    getAllProbes('CutBasedNoIsoLoose', "goodElectronsPROBECutBasedNoIsoLoose")
    getAllProbes('CutBasedNoIsoMedium', "goodElectronsPROBECutBasedNoIsoMedium")
    getAllProbes('CutBasedNoIsoTight', "goodElectronsPROBECutBasedNoIsoTight")
    getAllProbes('TightConvIHit0', "goodElectronsPROBETightConvIHit0")

    def getTagProbePairs(name, string):
      temp = process.tagTightEleID.clone()
      temp.decay = cms.string(string)
      setattr(process, name, temp)
      process.allTagsAndProbes *= temp
      return name

    def getProducer(name, allProbes, pairsString):
      producer = process.GsfElectronToEleID.clone()
      producer.jetCollection = cms.InputTag("slimmedJets")
      producer.jet_pt_cut = cms.double(30.)
      producer.jet_eta_cut = cms.double(2.5)
      producer.match_delta_r = cms.double(0.3)
      producer.variables = MiniIsoProbeVars
      producer.tagProbePairs = cms.InputTag(getTagProbePairs(name + 'Pairs', pairsString))
      producer.allProbes = cms.InputTag(allProbes)
      setattr(process, name, producer)
      process.tree_sequence *= producer

    getProducer('GsfElectronToID', "goodElectronsProbeHLT", "goodElectronsTagHLT@+ goodElectrons@-")
    process.GsfElectronToID.flags = cms.PSet(
        passingVeto = cms.InputTag("goodElectronsPROBECutBasedNoIsoVeto"),
        passingLoose = cms.InputTag("goodElectronsPROBECutBasedNoIsoLoose"),
        passingMedium = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium"),
        passingTight = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight"),
        passingLoose2D = cms.InputTag("goodElectronsPROBELoose2D"),
        passingFOID2D = cms.InputTag("goodElectronsPROBEFOID2D"),
        passingTight2D3D = cms.InputTag("goodElectronsPROBETight2D3D"),
        passingTightID2D3D = cms.InputTag("goodElectronsPROBETightID2D3D"),
        passingLeptonMvaM = cms.InputTag("goodElectronsPROBELeptonMvaM"),
        passingLeptonMvaVT = cms.InputTag("goodElectronsPROBELeptonMvaVT"),
        passingCutBasedTTZ = cms.InputTag("goodElectronsPROBECutBasedTTZ"),
        passingCutBasedIllia = cms.InputTag("goodElectronsPROBECutBasedIllia"),
        passingCutBasedStopsDilepton = cms.InputTag("goodElectronsPROBECutBasedStopsDilepton"),
        passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("goodElectronsPROBELeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04"),
        passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("goodElectronsPROBELeptonMvaMIDEmuTightIP2DSIP3D8miniIso04"),
    )

    getProducer('MVAVLooseElectronToIso', "goodElectronsProbeLoose2D", "goodElectronsTagHLT@+ goodElectronsPROBELoose2D@-")
    process.MVAVLooseElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBEMiniMVAVLoose"), 
        passingMini2 = cms.InputTag("goodElectronsPROBEMini2MVAVLoose"),
        passingMini4 = cms.InputTag("goodElectronsPROBEMini4MVAVLoose"),
        passingConvIHit1 = cms.InputTag("goodElectronsPROBEConvIHit1"),
    )

    getProducer('MVATightElectronToIso', "goodElectronsProbeMVATightID2D3D", "goodElectronsTagHLT@+ goodElectronsPROBETightID2D3D@-")
    process.MVATightElectronToIso.flags = cms.PSet(
        passingMultiIsoM = cms.InputTag("goodElectronsPROBEMultiIsoM"),
        passingMultiIsoT = cms.InputTag("goodElectronsPROBEMultiIsoT"),
        passingMultiIsoVT = cms.InputTag("goodElectronsPROBEMultiIsoVT"),
        passingMultiIsoEmu = cms.InputTag("goodElectronsPROBEMultiIsoEmu"),
        passingConvIHit0 = cms.InputTag("goodElectronsPROBEConvIHit0"),
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
    )

    getProducer('MVATightNoEMuElectronToIso', 'goodElectronsProbeMVATight2D3D', "goodElectronsTagHLT@+ goodElectronsPROBETight2D3D@-")
    process.MVATightNoEMuElectronToIso.flags = cms.PSet(
        passingConvIHit0 = cms.InputTag("goodElectronsPROBEConvIHit0"),
    )

    getProducer('MVATightConvIHit0ElectronToIso', "goodElectronsProbeTightConvIHit0","goodElectronsTagHLT@+ goodElectronsPROBETightConvIHit0@-")
    process.MVATightConvIHit0ElectronToIso.flags = cms.PSet(
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
    )

    getProducer('CutBasedTightElectronToIso', "goodElectronsProbeCutBasedNoIsoTight","goodElectronsTagHLT@+ goodElectronsPROBETightConvIHit0@-")
    process.CutBasedTightElectronToIso.flags = cms.PSet(
        passingMini  = cms.InputTag("goodElectronsPROBEMini"),
        passingMini2 = cms.InputTag("goodElectronsPROBEMini2"),
        passingMini4 = cms.InputTag("goodElectronsPROBEMini4"),
        passingConvIHit1 = cms.InputTag("goodElectronsPROBEConvIHit1"),
        passingMultiIsoVT = cms.InputTag("goodElectronsPROBEMultiIsoVT"),
    )


    if varOptions.isMC:
        process.p = cms.Path(
            process.sampleInfo +
            process.hltFilter +
            process.ElectronIsolation +
            process.cand_sequence +
            process.eleVarHelper +
            process.iso_sums +
            process.ak4PFCHSL1FastL2L3CorrectorChain +
            process.jetConverter + 
            process.jetAwareCleaner +
            process.AddLeptonJetRelatedVariables  + 
            process.MyEleVars +
            process.my_ele_sequence + 
            process.sc_sequence +
            process.allTagsAndProbes +
            process.pileupReweightingProducer +
            process.mc_sequence +
            process.GsfDRToNearestTauProbe + 
            process.GsfDRToNearestTauTag + 
            process.GsfDRToNearestTauSC + 
            process.tree_sequence
        )
    else:
        process.p = cms.Path(
            process.sampleInfo +
            process.hltFilter +
            process.ElectronIsolation +
            process.cand_sequence +
            process.eleVarHelper +
            process.iso_sums +
            process.ak4PFCHSL1FastL2L3CorrectorChain +
            process.jetConverter + 
            process.jetAwareCleaner +
            process.AddLeptonJetRelatedVariables +
            process.MyEleVars +
            process.my_ele_sequence + 
            process.sc_sequence +
            process.allTagsAndProbes +
            process.mc_sequence +
            process.tree_sequence
        )
