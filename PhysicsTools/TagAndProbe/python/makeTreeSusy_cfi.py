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
        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
       #effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
        probes             = cms.InputTag(options['ELECTRON_COLL']),
        tight              = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight"),
        triggerEmu         = cms.InputTag("egmGsfElectronIDs:cutBasedElectronHLTPreselection-Summer16-V1"),
        mvasHZZ            = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        mvas               = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        mvaWP80            = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
        mvaWP90            = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
        dxy                = cms.InputTag("eleVarHelper:dxy"),
        dz                 = cms.InputTag("eleVarHelper:dz"),
        miniIso            = cms.InputTag("relminiiso:sum"),
        chargedMiniIso     = cms.InputTag("relminiiso:charged"),
        neutralMiniIso     = cms.InputTag("relminiiso:neutral"),
        jetPtRatio         = cms.InputTag("AddLeptonJetRelatedVariables","JetPtRatio"),
        jetPtRel           = cms.InputTag("AddLeptonJetRelatedVariables","JetPtRel"),
        jetNDauCharged     = cms.InputTag("AddLeptonJetRelatedVariables","JetNDauCharged"),
        jetBTagCSV         = cms.InputTag("AddLeptonJetRelatedVariables","JetBTagCSV"),
        rho                = cms.InputTag("fixedGridRhoFastjetAll"),
    )

    process.relminiiso =  cms.EDProducer("IsolationSum",
        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
       #effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
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
    workingPoints = ["CutBasedV", "CutBasedVPOGIP2D", "CutBasedSpring15V",
                     "CutBasedL", "CutBasedLPOGIP2D", "CutBasedSpring15L",
                     "CutBasedM", "CutBasedMPOGIP2D", "CutBasedSpring15M",
                     "CutBasedT", "CutBasedTPOGIP2D", "CutBasedSpring15T",
                     "CutBasedStopsDilepton","TTZ", "TTG", "MVAWP90IDEMuTTZRelIsoCBL", "MVAWP90IDEMuTTZ", "MVAWP90", "TTZ2017", "TTZ2017TightCharge",
                     "MVAVLooseTightIP2D", "MVAVLooseFOIDEmuTightIP2D", 
                     "MVATightTightIP2DSIP3D4", "MVATightIDEmuTightIP2DSIP3D4", "MVATightIDEmuTightIP2DSIP3D4ConvVetoIHit0",
                     "Mini", "Mini2", "Mini4","RelIso010","RelIso012",
                     "MultiIsoM", "MultiIsoT", "MultiIsoT", "MultiIsoTISOEmu",
                     "ConvVetoIHit1", "ConvVetoIHit0", "Charge",
                     "Feb2018Loose", "Feb2018LeptonMvaL", "Feb2018LeptonMvaM", "Feb2018LeptonMvaT", "TightCharge",
                     "triggerEmu"];


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

    referenceWp = ['MVAVLooseTightIP2D', 'MVATightIDEmuTightIP2DSIP3D4', 'MVATightIDEmuTightIP2DSIP3D4ConvVetoIHit0','CutBasedStopsDilepton','Feb2018Loose','RFeb2018LeptonMvaL','RFeb2018LeptonMvaM','RFeb2018LeptonMvaT']
    for wp in referenceWp:
      getAllProbes(wp)

    # Tag and probe pairs
    def getTagProbePairs(name, string):
      temp = process.tagTightEleID.clone()
      temp.decay = cms.string(string)
      setattr(process, name, temp)
      process.allTagsAndProbes *= temp
      return name

    def getProducer(name, allProbes, ref, workingPoints):
      if ref not in referenceWp + ['goodElectrons']:
        print 'Unknown reference point: ' + ref
        exit(1)
      producer = process.GsfElectronToEleID.clone()
      producer.jetCollection = cms.InputTag("slimmedJets")
      producer.jet_pt_cut    = cms.double(30.)
      producer.jet_eta_cut   = cms.double(2.5)
      producer.match_delta_r = cms.double(0.3)
      producer.variables     = MiniIsoProbeVars
      producer.tagProbePairs = cms.InputTag(getTagProbePairs(name + 'Pairs', 'goodElectronsTagHLT@+ ' + (ref if ref == 'goodElectrons' else ('probes' + ref)) + '@-'))
      producer.allProbes     = cms.InputTag(allProbes)
      producer.flags         = cms.PSet()
      for wp in workingPoints: setattr(producer.flags, 'passing' + wp, cms.InputTag('probes' + wp))

      setattr(process, name, producer)
      process.tree_sequence *= producer

    getProducer('GsfElectronToID', "goodElectronsProbeHLT", "goodElectrons",
                ['CutBasedV','CutBasedL','CutBasedM','CutBasedT','CutBasedSpring15V', 'CutBasedSpring15L', 'CutBasedSpring15M', 'CutBasedSpring15T',
                 'CutBasedStopsDilepton','TTZ', 'TTG', "MVAWP90IDEMuTTZRelIsoCBL", "MVAWP90IDEMuTTZ", "MVAWP90", "TTZ2017", "TTZ2017TightCharge",
                 'MVAVLooseTightIP2D','MVAVLooseFOIDEmuTightIP2D', 'MVATightTightIP2DSIP3D4','MVATightIDEmuTightIP2DSIP3D4',
                 'Feb2018Loose'])


    getProducer('MVAVLooseElectronToIso', "goodElectronsProbeMVAVLooseTightIP2D", "MVAVLooseTightIP2D",
                ['Mini','Mini2','Mini4','ConvVetoIHit1'])

    getProducer('MVATightElectronToIso', "goodElectronsProbeMVATightIDEmuTightIP2DSIP3D4", "MVATightIDEmuTightIP2DSIP3D4",
                ['RelIso010','MultiIsoM','MultiIsoT','MultiIsoTISOEmu','ConvVetoIHit0'])

    getProducer('MVATightConvIHit0ElectronToIso', "goodElectronsProbeMVATightIDEmuTightIP2DSIP3D4ConvVetoIHit0","MVATightIDEmuTightIP2DSIP3D4ConvVetoIHit0",
                ['Charge'])

    getProducer('CutBasedStopsDileptonToIso', 'goodElectronsProbeCutBasedStopsDilepton', 'CutBasedStopsDilepton', ['RelIso012'])

    getProducer('Feb2018LooseToLeptonMva', 'goodElectronsProbeFeb2018Loose', 'Feb2018Loose', ['Feb2018LeptonMvaL','Feb2018LeptonMvaM','Feb2018LeptonMvaT'])
    getProducer('Feb2018LeptonMvaLToTightCharge', 'goodElectronsProbeRFeb2018LeptonMvaL', 'RFeb2018LeptonMvaL', ['TightCharge'])
    getProducer('Feb2018LeptonMvaMToTightCharge', 'goodElectronsProbeRFeb2018LeptonMvaM', 'RFeb2018LeptonMvaM', ['TightCharge'])
    getProducer('Feb2018LeptonMvaTToTightCharge', 'goodElectronsProbeRFeb2018LeptonMvaT', 'RFeb2018LeptonMvaT', ['TightCharge'])

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
