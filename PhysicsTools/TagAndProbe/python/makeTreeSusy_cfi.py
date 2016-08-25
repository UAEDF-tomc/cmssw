import FWCore.ParameterSet.Config as cms
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *


def AddMiniIso(process, options, varOptions):
    process.load("JetMETCorrections.Configuration.JetCorrectors_cff")

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
    )

    process.relminiiso =  cms.EDProducer("IsolationSum",
        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
        rho                = cms.InputTag("fixedGridRhoFastjetAll"),
        candidates         = cms.InputTag("packedPFCandidates"),
        probes             = cms.InputTag("slimmedElectrons"),
        minRadius          = cms.double(0.05),
        maxRadius          = cms.double(0.2),
        ktScale            = cms.double(10.),
    )


    MiniIsoProbeVars = cms.PSet(
        process.GsfElectronToEleID.variables,
        probe_ele_Mini               = cms.InputTag("relminiiso:sum"),
        probe_ele_chargedMini        = cms.InputTag("relminiiso:charged"),
        probe_ele_neutralMini        = cms.InputTag("relminiiso:neutral"),
        probe_ele_JetPtRatio         = cms.InputTag("AddLeptonJetRelatedVariables:JetPtRatio"),
        probe_ele_JetPtRel           = cms.InputTag("AddLeptonJetRelatedVariables:JetPtRel"),
        probe_ele_JetNDauCharged     = cms.InputTag("AddLeptonJetRelatedVariables:JetNDauCharged"),
        probe_ele_JetBTagCSV         = cms.InputTag("AddLeptonJetRelatedVariables:JetBTagCSV"),
        probe_ele_sip3d              = cms.InputTag("MyEleVars:sip3d"),
        probe_ele_ecalIso            = cms.InputTag("MyEleVars:ecalIso"),
        probe_ele_hcalIso            = cms.InputTag("MyEleVars:hcalIso"),
        probe_ele_trackIso           = cms.InputTag("MyEleVars:trackIso"),
        probe_ele_missIHits          = cms.InputTag("MyEleVars:missIHits"),
    )


    process.my_ele_sequence = cms.Sequence()

    # All workingpoints we need to probe
    # Note: cut based wp are without isolation
    workingPoints = ['CutBasedVeto', 'CutBasedLoose', 'CutBasedMedium', 'CutBasedTight',
		    'MVAVLooseFO', 'MVAVLoose', 'MVATight', 'MVAWP80', 'MVAWP90',
		    'Mini', 'Mini2', 'Mini4', 'MVAVLooseMini', 'MVAVLooseMini2', 'MVAVLooseMini4',
		    'Loose2D', 'FOID2D', 'Tight2D3D', 'TightID2D3D',
		    'ConvIHit1', 'ConvIHit0', 'TightConvIHit0', 'ConvIHit0Chg',
		    'MultiIsoM', 'MultiIsoT', 'MultiIsoVT', 'MultiIsoEmu',
		    'LeptonMvaM', 'LeptonMvaVT', 
		    'CutBasedTTZ', 'CutBasedIllia', 'CutBasedStopsDilepton',
		    'LeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04', 'LeptonMvaMIDEmuTightIP2DSIP3D8miniIso04']


    # Applies probe cuts and WP (numerators and denominators both need to be listed here)
    def getProbes(name):
      temp = process.goodElectronsPROBECutBasedVeto.clone()
      temp.selection = cms.InputTag('MyEleVars:pass' + wp)
      setattr(process, 'probes' + name, temp)
      process.my_ele_sequence += temp

    for wp in workingPoints: getProbes(wp)

    # Applies trigger matching (denominators need to be listed here)
    def getAllProbes(name):
      temp = process.goodElectronsTagHLT.clone()
      temp.isAND = cms.bool(False)
      temp.selection = cms.InputTag('probes' + name)
      setattr(process, 'goodElectronsProbe' + name, temp)
      process.my_ele_sequence += temp

    for wp in ['Loose2D', 'TightID2D3D', 'Tight2D3D', 'CutBasedVeto', 'CutBasedLoose', 'CutBasedMedium', 'CutBasedTight', 'TightConvIHit0']:
      getAllProbes(wp)

    # Tag and probe pairs
    def getTagProbePairs(name, string):
      temp = process.tagTightEleID.clone()
      temp.decay = cms.string(string)
      setattr(process, name, temp)
      process.allTagsAndProbes *= temp
      return name

    def getProducer(name, allProbes, pairsString):
      producer = process.GsfElectronToEleID.clone()
      producer.jetCollection = cms.InputTag("slimmedJets")
      producer.jet_pt_cut    = cms.double(30.)
      producer.jet_eta_cut   = cms.double(2.5)
      producer.match_delta_r = cms.double(0.3)
      producer.variables     = MiniIsoProbeVars
      producer.tagProbePairs = cms.InputTag(getTagProbePairs(name + 'Pairs', pairsString))
      producer.allProbes     = cms.InputTag(allProbes)
      setattr(process, name, producer)
      process.tree_sequence *= producer

    getProducer('GsfElectronToID', "goodElectronsProbeHLT", "goodElectronsTagHLT@+ goodElectrons@-")
    process.GsfElectronToID.flags = cms.PSet(
        passingVeto                                     = cms.InputTag("probesCutBasedVeto"),
        passingLoose                                    = cms.InputTag("probesCutBasedLoose"),
        passingMedium                                   = cms.InputTag("probesCutBasedMedium"),
        passingTight                                    = cms.InputTag("probesCutBasedTight"),
        passingLoose2D                                  = cms.InputTag("probesLoose2D"),
        passingFOID2D                                   = cms.InputTag("probesFOID2D"),
        passingTight2D3D                                = cms.InputTag("probesTight2D3D"),
        passingTightID2D3D                              = cms.InputTag("probesTightID2D3D"),
        passingLeptonMvaM                               = cms.InputTag("probesLeptonMvaM"),
        passingLeptonMvaVT                              = cms.InputTag("probesLeptonMvaVT"),
        passingCutBasedTTZ                              = cms.InputTag("probesCutBasedTTZ"),
        passingCutBasedIllia                            = cms.InputTag("probesCutBasedIllia"),
        passingCutBasedStopsDilepton                    = cms.InputTag("probesCutBasedStopsDilepton"),
        passingLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04 = cms.InputTag("probesLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04"),
        passingLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04  = cms.InputTag("probesLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04"),
    )

    getProducer('MVAVLooseElectronToIso', "goodElectronsProbeLoose2D", "goodElectronsTagHLT@+ probesLoose2D@-")
    process.MVAVLooseElectronToIso.flags = cms.PSet(
        passingMini      = cms.InputTag("probesMVAVLooseMini"), 
        passingMini2     = cms.InputTag("probesMVAVLooseMini2"),
        passingMini4     = cms.InputTag("probesMVAVLooseMini4"),
        passingConvIHit1 = cms.InputTag("probesConvIHit1"),
    )

    getProducer('MVATightElectronToIso', "goodElectronsProbeTightID2D3D", "goodElectronsTagHLT@+ probesTightID2D3D@-")
    process.MVATightElectronToIso.flags = cms.PSet(
        passingMultiIsoM    = cms.InputTag("probesMultiIsoM"),
        passingMultiIsoT    = cms.InputTag("probesMultiIsoT"),
        passingMultiIsoVT   = cms.InputTag("probesMultiIsoVT"),
        passingMultiIsoEmu  = cms.InputTag("probesMultiIsoEmu"),
        passingConvIHit0    = cms.InputTag("probesConvIHit0"),
        passingConvIHit0Chg = cms.InputTag("probesConvIHit0Chg"),
    )

    getProducer('MVATightNoEMuElectronToIso', 'goodElectronsProbeTight2D3D', "goodElectronsTagHLT@+ probesTight2D3D@-")
    process.MVATightNoEMuElectronToIso.flags = cms.PSet(
        passingConvIHit0 = cms.InputTag("probesConvIHit0"),
    )

    getProducer('MVATightConvIHit0ElectronToIso', "goodElectronsProbeTightConvIHit0","goodElectronsTagHLT@+ probesTightConvIHit0@-")
    process.MVATightConvIHit0ElectronToIso.flags = cms.PSet(
        passingConvIHit0Chg = cms.InputTag("probesConvIHit0Chg"),
    )

    for level in ['Veto', 'Loose', 'Medium', 'Tight']:
      getProducer('CutBased' + level + 'ElectronToIso', "goodElectronsProbeCutBased" + level, "goodElectronsTagHLT@+ probesCutBased" + level + "@-")
      temp = getattr(process, 'CutBased' + level + 'ElectronToIso')
      temp.flags = cms.PSet(
	  passingMini       = cms.InputTag("probesMini"),
	  passingMini2      = cms.InputTag("probesMini2"),
	  passingMini4      = cms.InputTag("probesMini4"),
	  passingConvIHit1  = cms.InputTag("probesConvIHit1"),
	  passingMultiIsoVT = cms.InputTag("probesMultiIsoVT"),
      )


    if varOptions.isMC:
        process.p = cms.Path(
            process.sampleInfo +
            process.hltFilter +
            process.cand_sequence +
            process.eleVarHelper +
            process.relminiiso +
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
            process.cand_sequence +
            process.eleVarHelper +
            process.relminiiso +
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
