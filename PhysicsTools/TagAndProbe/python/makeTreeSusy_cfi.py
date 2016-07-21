import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *


def AddMiniIso(process, options, varOptions):
    #Adds clones of objects managed by Matteo so that upstream changes propagate to mini iso objects
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

    process.jetConverter = cms.EDProducer(
        "JetConverter",
        jets=cms.InputTag("slimmedJets")
    )

    process.jetAwareCleaner = cms.EDProducer(
        "JetAwareCleaner",
        RawJetCollection= cms.InputTag("jetConverter"),
        LeptonCollection= cms.InputTag(options['ELECTRON_COLL']),
        L1Corrector = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
        L1L2L3ResCorrector= cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
        dRmax = cms.double(0.4),
        dRCandProbeVeto = cms.double(0.0001)
    )
    
    process.AddLeptonJetRelatedVariables = cms.EDProducer("AddLeptonJetRelatedVariables",
	JetCollection= cms.InputTag("jetAwareCleaner"),
	JetCollectionWithCSV= cms.InputTag("slimmedJets"),
	pfCandidates = cms.InputTag("packedPFCandidates"),
	LeptonCollection = cms.InputTag(options['ELECTRON_COLL']),
	dRmax = cms.double(0.4),
	subLepFromJetForPtRel = cms.bool(True)
    )


    process.MyEleVars = cms.EDProducer(
        "MyElectronVariableHelper",
        probes = cms.InputTag(options['ELECTRON_COLL']),
        mvas = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        dxy = cms.InputTag("eleVarHelper:dxy"),
        dz = cms.InputTag("eleVarHelper:dz"),
        miniIso = cms.InputTag("relminiiso:sum"),
        chargedMiniIso = cms.InputTag("relminiiso:charged"),
        neutralMiniIso = cms.InputTag("relminiiso:neutral"),
        jetPtRatio     = cms.InputTag("AddLeptonJetRelatedVariables","JetPtRatio"),
        jetPtRel       = cms.InputTag("AddLeptonJetRelatedVariables","JetPtRel"),
        jetNDauCharged = cms.InputTag("AddLeptonJetRelatedVariables","JetNDauCharged"),
        jetBTagCSV     = cms.InputTag("AddLeptonJetRelatedVariables","JetBTagCSV"),
        eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium"),
    )

    MiniIsoProbeVars = cms.PSet(
        process.GsfElectronToEleID.variables,
        probe_ele_chMini = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
        probe_ele_neuMini = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
        probe_ele_phoMini = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
        probe_ele_chAct = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
        probe_ele_neuAct = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
        probe_ele_phoAct = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
        probe_ele_Act = cms.InputTag("absactivity:sum"),
        probe_ele_Mini = cms.InputTag("relminiiso:sum"),
        probe_ele_chargedMini = cms.InputTag("relminiiso:charged"),
        probe_ele_neutralMini = cms.InputTag("relminiiso:neutral"),
        probe_ele_RelAct = cms.InputTag("relactivity:sum"),
        probe_ele_AbsMini = cms.InputTag("absminiiso:sum"),
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

    activity_pset = cms.PSet()
    for eleid in process.egmGsfElectronIDs.physicsObjectIDs:
        if eleid.idDefinition.idName == "cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-tight":
            for cut in eleid.idDefinition.cutFlow:
                if cut.cutName == "GsfEleEffAreaMiniIsoCut":
                    activity_pset = cut
                    
    process.absactivity = cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        actRadius = cms.double(0.4),
        isRelativeIso = cms.bool(False),
    )
    process.relactivity = cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005-Act040"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005-Act040"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005-Act040"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        actRadius = cms.double(0.4),
        isRelativeIso = cms.bool(True),
    )
    process.absminiiso =  cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        isRelativeIso = cms.bool(False),
    )                                      
    process.relminiiso =  cms.EDProducer(
        "IsolationSum",
        effAreasConfigFile = activity_pset.effAreasConfigFile,
        probes = cms.InputTag("slimmedElectrons"),
        rho = activity_pset.rho,
        chadIso = cms.InputTag("ElectronIsolation:h+-DR020-BarVeto000-EndVeto001-kt1000-Min005"),
        nhadIso = cms.InputTag("ElectronIsolation:h0-DR020-BarVeto000-EndVeto000-kt1000-Min005"),
        phoIso = cms.InputTag("ElectronIsolation:gamma-DR020-BarVeto000-EndVeto008-kt1000-Min005"),
        minRadius = cms.double(0.05),
        maxRadius = cms.double(0.2),
        ktScale = cms.double(10.),
        isRelativeIso = cms.bool(True),
    )

    process.iso_sums = cms.Sequence(
        process.absactivity +
        process.relactivity +
        process.absminiiso +
        process.relminiiso
    )                                   

    #Applies probe cuts and WP (numerators and denominators both need to be listed here)
    process.goodElectronsPROBECutBasedNoIsoVeto = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoVeto.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-veto")
    process.goodElectronsPROBECutBasedNoIsoLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoLoose.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-loose")
    process.goodElectronsPROBECutBasedNoIsoMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-medium")
    process.goodElectronsPROBECutBasedNoIsoTight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedNoIsoTight.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-noiso-tight")
    process.goodElectronsPROBECutBasedMiniMedium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMiniMedium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini-V1-standalone-medium")
    process.goodElectronsPROBECutBasedMini4Medium = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedMini4Medium.selection = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Spring15-25ns-Mini4-V1-standalone-medium")
    process.goodElectronsPROBEMVAVLooseFO = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAVLooseFO.selection = cms.InputTag("MyEleVars:passMVAVLooseFO")
    process.goodElectronsPROBEMVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLoose")
    process.goodElectronsPROBEMVATight = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVATight.selection = cms.InputTag("MyEleVars:passMVATight")
    process.goodElectronsPROBEMVAWP80 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAWP80.selection = cms.InputTag("MyEleVars:passMVAWP80")
    process.goodElectronsPROBEMVAWP90 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMVAWP90.selection = cms.InputTag("MyEleVars:passMVAWP90")
    process.goodElectronsPROBEMiniMVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMiniMVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLooseMini")
    process.goodElectronsPROBEMini2MVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMini2MVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLooseMini2")
    process.goodElectronsPROBEMini4MVAVLoose = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMini4MVAVLoose.selection = cms.InputTag("MyEleVars:passMVAVLooseMini4")
    process.goodElectronsPROBELoose2D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBELoose2D.selection = cms.InputTag("MyEleVars:passLoose2D")
    process.goodElectronsPROBEFOID2D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEFOID2D.selection = cms.InputTag("MyEleVars:passFOID2D")
    process.goodElectronsPROBETight2D3D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBETight2D3D.selection = cms.InputTag("MyEleVars:passTight2D3D")
    process.goodElectronsPROBETightID2D3D = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBETightID2D3D.selection = cms.InputTag("MyEleVars:passTightID2D3D")
    process.goodElectronsPROBEConvIHit1 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEConvIHit1.selection = cms.InputTag("MyEleVars:passConvIHit1")
    process.goodElectronsPROBEConvIHit0 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEConvIHit0.selection = cms.InputTag("MyEleVars:passConvIHit0")
    process.goodElectronsPROBETightConvIHit0 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBETightConvIHit0.selection = cms.InputTag("MyEleVars:passTightConvIHit0")
    process.goodElectronsPROBEConvIHit0Chg = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEConvIHit0Chg.selection = cms.InputTag("MyEleVars:passConvIHit0Chg")
    process.goodElectronsPROBEMultiIsoM = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMultiIsoM.selection = cms.InputTag("MyEleVars:passMultiIsoM")
    process.goodElectronsPROBEMultiIsoT = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMultiIsoT.selection = cms.InputTag("MyEleVars:passMultiIsoT")
    process.goodElectronsPROBEMultiIsoVT = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMultiIsoVT.selection = cms.InputTag("MyEleVars:passMultiIsoVT")
    process.goodElectronsPROBEMultiIsoEmu = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBEMultiIsoEmu.selection = cms.InputTag("MyEleVars:passMultiIsoEmu")
    process.goodElectronsPROBELeptonMvaM = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBELeptonMvaM.selection = cms.InputTag("MyEleVars:passLeptonMvaM")
    process.goodElectronsPROBELeptonMvaVT = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBELeptonMvaVT.selection = cms.InputTag("MyEleVars:passLeptonMvaVT")
    process.goodElectronsPROBECutBasedTTZ = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedTTZ.selection = cms.InputTag("MyEleVars:passCutBasedTTZ")
    process.goodElectronsPROBECutBasedIllia = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBECutBasedIllia.selection = cms.InputTag("MyEleVars:passCutBasedIllia")
    process.goodElectronsPROBELeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBELeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04.selection = cms.InputTag("MyEleVars:passLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04")
    process.goodElectronsPROBELeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 = process.goodElectronsPROBECutBasedVeto.clone()
    process.goodElectronsPROBELeptonMvaMIDEmuTightIP2DSIP3D8miniIso04.selection = cms.InputTag("MyEleVars:passLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04")

    #Applies trigger matching (denominators need to be listed here)
    process.goodElectronsProbeMediumNoIso = process.goodElectronsTagHLT.clone()
    process.goodElectronsProbeMediumNoIso.isAND = cms.bool(False)
    process.goodElectronsProbeMediumNoIso.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoMedium")
    process.goodElectronsProbeLoose2D = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeLoose2D.inputs = cms.InputTag("goodElectronsPROBELoose2D")
    process.goodElectronsProbeMVATightID2D3D = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeMVATightID2D3D.inputs = cms.InputTag("goodElectronsPROBETightID2D3D")
    process.goodElectronsProbeMVATight2D3D = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeMVATight2D3D.inputs = cms.InputTag("goodElectronsPROBETight2D3D")
    process.goodElectronsProbeCutBasedNoIsoTight = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeCutBasedNoIsoTight.inputs = cms.InputTag("goodElectronsPROBECutBasedNoIsoTight")
    process.goodElectronsProbeTightConvIHit0 = process.goodElectronsProbeMediumNoIso.clone()
    process.goodElectronsProbeTightConvIHit0.inputs = cms.InputTag("goodElectronsPROBETightConvIHit0")

    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoVeto
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoLoose
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoMedium
    process.ele_sequence += process.goodElectronsPROBECutBasedNoIsoTight
    process.ele_sequence += process.goodElectronsPROBECutBasedMiniMedium
    process.ele_sequence += process.goodElectronsPROBECutBasedMini4Medium
    process.ele_sequence += process.goodElectronsProbeMediumNoIso

    process.my_ele_sequence = cms.Sequence()
    process.my_ele_sequence += process.goodElectronsPROBEMVAVLooseFO
    process.my_ele_sequence += process.goodElectronsPROBEMVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBEMVATight
    process.my_ele_sequence += process.goodElectronsPROBEMVAWP80
    process.my_ele_sequence += process.goodElectronsPROBEMVAWP90
    process.my_ele_sequence += process.goodElectronsPROBEMiniMVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBEMini2MVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBEMini4MVAVLoose
    process.my_ele_sequence += process.goodElectronsPROBELoose2D
    process.my_ele_sequence += process.goodElectronsPROBEFOID2D
    process.my_ele_sequence += process.goodElectronsPROBETight2D3D
    process.my_ele_sequence += process.goodElectronsPROBETightID2D3D
    process.my_ele_sequence += process.goodElectronsPROBEConvIHit1
    process.my_ele_sequence += process.goodElectronsPROBEConvIHit0
    process.my_ele_sequence += process.goodElectronsPROBEConvIHit0Chg
    process.my_ele_sequence += process.goodElectronsPROBETightConvIHit0
    process.my_ele_sequence += process.goodElectronsProbeLoose2D
    process.my_ele_sequence += process.goodElectronsProbeMVATightID2D3D
    process.my_ele_sequence += process.goodElectronsProbeMVATight2D3D
    process.my_ele_sequence += process.goodElectronsProbeCutBasedNoIsoTight
    process.my_ele_sequence += process.goodElectronsProbeTightConvIHit0
    process.my_ele_sequence += process.goodElectronsPROBEMultiIsoM
    process.my_ele_sequence += process.goodElectronsPROBEMultiIsoT
    process.my_ele_sequence += process.goodElectronsPROBEMultiIsoVT
    process.my_ele_sequence += process.goodElectronsPROBEMultiIsoEmu
    process.my_ele_sequence += process.goodElectronsPROBELeptonMvaM
    process.my_ele_sequence += process.goodElectronsPROBELeptonMvaVT
    process.my_ele_sequence += process.goodElectronsPROBECutBasedTTZ
    process.my_ele_sequence += process.goodElectronsPROBECutBasedIllia
    process.my_ele_sequence += process.goodElectronsPROBELeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04
    process.my_ele_sequence += process.goodElectronsPROBELeptonMvaMIDEmuTightIP2DSIP3D8miniIso04

    process.tagTightID = process.tagTightEleID.clone()
    process.tagTightID.decay = cms.string("goodElectronsTagHLT@+ goodElectrons@-")
    process.tagTightMiniMVAVLoose = process.tagTightEleID.clone()
    process.tagTightMiniMVAVLoose.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBELoose2D@-")
    process.tagTightMiniMVATight = process.tagTightEleID.clone()
    process.tagTightMiniMVATight.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBETightID2D3D@-")
    process.tagTightMiniMVATightNoEMu = process.tagTightEleID.clone()
    process.tagTightMiniMVATightNoEMu.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBETight2D3D@-")
    process.tagTightMiniCutBasedTight = process.tagTightEleID.clone()
    process.tagTightMiniCutBasedTight.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBECutBasedNoIsoTight@-")
    process.tagTightMiniTightConvIHit0 = process.tagTightEleID.clone()
    process.tagTightMiniTightConvIHit0.decay = cms.string("goodElectronsTagHLT@+ goodElectronsPROBETightConvIHit0@-")

    process.allTagsAndProbes *= process.tagTightID
    process.allTagsAndProbes *= process.tagTightMiniMVAVLoose
    process.allTagsAndProbes *= process.tagTightMiniMVATight
    process.allTagsAndProbes *= process.tagTightMiniMVATightNoEMu
    process.allTagsAndProbes *= process.tagTightMiniCutBasedTight
    process.allTagsAndProbes *= process.tagTightMiniTightConvIHit0

    process.GsfElectronToEleID.jetCollection = cms.InputTag("slimmedJets")
    process.GsfElectronToEleID.jet_pt_cut = cms.double(30.)
    process.GsfElectronToEleID.jet_eta_cut = cms.double(2.5)
    process.GsfElectronToEleID.match_delta_r = cms.double(0.3)

    process.GsfElectronToID = process.GsfElectronToEleID.clone()
    process.GsfElectronToID.variables = MiniIsoProbeVars
    process.GsfElectronToID.tagProbePairs = cms.InputTag("tagTightID")
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
        passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("goodElectronsPROBELeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04"),
        passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("goodElectronsPROBELeptonMvaMIDEmuTightIP2DSIP3D8miniIso04"),
    )
    process.GsfElectronToID.allProbes = cms.InputTag("goodElectronsProbeHLT")
    process.MVAVLooseElectronToIso = process.GsfElectronToEleID.clone()
    process.MVAVLooseElectronToIso.variables = MiniIsoProbeVars
    process.MVAVLooseElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMVAVLoose")
    process.MVAVLooseElectronToIso.flags = cms.PSet(
        passingMini = cms.InputTag("goodElectronsPROBEMiniMVAVLoose"), 
        passingMini2 = cms.InputTag("goodElectronsPROBEMini2MVAVLoose"),
        passingMini4 = cms.InputTag("goodElectronsPROBEMini4MVAVLoose"),
        passingConvIHit1 = cms.InputTag("goodElectronsPROBEConvIHit1"),
    )
    process.MVAVLooseElectronToIso.allProbes = cms.InputTag("goodElectronsProbeLoose2D")

    process.MVATightElectronToIso = process.GsfElectronToEleID.clone()
    process.MVATightElectronToIso.variables = MiniIsoProbeVars
    process.MVATightElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMVATight")
    process.MVATightElectronToIso.flags = cms.PSet(
        passingMultiIsoT = cms.InputTag("goodElectronsPROBEMultiIsoM"),
        passingMultiIsoT = cms.InputTag("goodElectronsPROBEMultiIsoT"),
        passingMultiIsoVT = cms.InputTag("goodElectronsPROBEMultiIsoVT"),
        passingMultiIsoEmu = cms.InputTag("goodElectronsPROBEMultiIsoEmu"),
        passingConvIHit0 = cms.InputTag("goodElectronsPROBEConvIHit0"),
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
    )
    process.MVATightElectronToIso.allProbes = cms.InputTag("goodElectronsProbeMVATightID2D3D")

    process.MVATightNoEMuElectronToIso = process.GsfElectronToEleID.clone()
    process.MVATightNoEMuElectronToIso.variables = MiniIsoProbeVars
    process.MVATightNoEMuElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniMVATightNoEMu")
    process.MVATightNoEMuElectronToIso.flags = cms.PSet(
        passingConvIHit0 = cms.InputTag("goodElectronsPROBEConvIHit0"),
    )
    process.MVATightNoEMuElectronToIso.allProbes = cms.InputTag("goodElectronsProbeMVATight2D3D")

    process.MVATightConvIHit0ElectronToIso = process.GsfElectronToEleID.clone()
    process.MVATightConvIHit0ElectronToIso.variables = MiniIsoProbeVars
    process.MVATightConvIHit0ElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniTightConvIHit0")
    process.MVATightConvIHit0ElectronToIso.flags = cms.PSet(
        passingConvIHit0Chg = cms.InputTag("goodElectronsPROBEConvIHit0Chg"),
    )
    process.MVATightConvIHit0ElectronToIso.allProbes = cms.InputTag("goodElectronsProbeTightConvIHit0")


    process.CutBasedTightElectronToIso = process.GsfElectronToEleID.clone()
    process.CutBasedTightElectronToIso.variables = MiniIsoProbeVars
    process.CutBasedTightElectronToIso.tagProbePairs = cms.InputTag("tagTightMiniCutBasedTight")
    process.CutBasedTightElectronToIso.flags = cms.PSet(
        passingMultiIsoVT = cms.InputTag("goodElectronsPROBEMultiIsoVT"),
    )
    process.CutBasedTightElectronToIso.allProbes = cms.InputTag("goodElectronsProbeCutBasedNoIsoTight")


# The McMatchRECO disappeared since 76X, should investigate what it does
#    if varOptions.isMC:
#        process.GsfElectronToID.probeMatches = cms.InputTag("McMatchRECO")
#        process.MVAVLooseElectronToIso.probeMatches = cms.InputTag("McMatchRECO")
#        process.MVATightElectronToIso.probeMatches = cms.InputTag("McMatchRECO")

    process.tree_sequence *= process.GsfElectronToID
    process.tree_sequence *= process.MVAVLooseElectronToIso
    process.tree_sequence *= process.MVATightElectronToIso
    process.tree_sequence *= process.MVATightNoEMuElectronToIso
    process.tree_sequence *= process.CutBasedTightElectronToIso
    process.tree_sequence *= process.MVATightConvIHit0ElectronToIso


    #Probably a better way to do this, but just copy for now to refresh paths and insert ElectronIsolation

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
