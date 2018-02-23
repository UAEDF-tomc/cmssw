import FWCore.ParameterSet.Config as cms
### USAGE:
###
###
###
###

#### 
#### For systematics studies: 
#### .1. ID with data and MC: 
####     cmsRun fitMuonID_id.py TEST 3 data_all 
####     cmsRun fitMuonID_id.py TEST 3 mc_all LO 
#### 
#### .2. Iso with data and MC: 
####     cmsRun fitMuonID_id.py TEST 8 data_all 
####     cmsRun fitMuonID_id.py TEST 8 mc_all LO 

import sys, os, shutil
args = sys.argv[1:]
iteration = 'TEST'
if len(args) > 1: iteration = args[1]
print "The iteration is", iteration
id_bins = '1'
if len(args) > 2: id_bins = args[2]
print 'id_bins is', id_bins
scenario = "data_all"
if len(args) > 3: scenario = args[3]
print "Will run scenario", scenario
sample = 'JSON1280'
if len(args) > 4: sample = args[4]
print 'the sample is', sample 

process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

#set different mass range if iso
_mrange = "70"
if (int(id_bins) > 4) and (int(id_bins) < 10): 
    _mrange = "77"
if (int(id_bins) == 10 or int(id_bins) == 20): 
    _mrange = "77" 
print '_mrange is', _mrange


Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),

    Variables = cms.PSet(
        #weight = cms.vstring("weight","-100","100",""),
        mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}"),
        ###mass = cms.vstring("Tag-muon Mass", "70", "130", "GeV/c^{2}"),
        pt = cms.vstring("muon p_{T}", "0", "1000", "GeV/c"),
        #eta    = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        abseta = cms.vstring("muon |#eta|", "0", "2.5", ""),
        #phi    = cms.vstring("muon #phi at vertex", "-3.1416", "3.1416", ""),
        #charge = cms.vstring("muon charge", "-2.5", "2.5", ""),
        #combRelIsoPF04dBeta = cms.vstring("dBeta rel iso dR 0.4", "-2", "9999999", ""),
        #combRelIsoPF03dBeta = cms.vstring("dBeta rel iso dR 0.3", "-2", "9999999", ""),
        tag_pt = cms.vstring("Tag p_{T}", "0", "1000", "GeV/c"),
        tag_nVertices   = cms.vstring("Number of vertices", "0", "999", ""),
        #tag_abseta = cms.vstring("|eta| of tag muon", "0", "2.5", ""),
        tag_combRelIsoPF04dBeta = cms.vstring("Tag dBeta rel iso dR 0.4", "-2", "9999999", ""),
        dB = cms.vstring("dB", "-1000", "1000", ""),
        dzPV = cms.vstring("dzPV", "-1000", "1000", ""),
        #dxyBS = cms.vstring("dxyBS", "-1000", "1000", ""),
        SIP = cms.vstring("SIP", "-1000", "1000", ""),
        pair_probeMultiplicity = cms.vstring("pair_probeMultiplicity", "0","30",""),
        miniIsoCharged  = cms.vstring("miniIsoCharged" ,  "-2", "9999999", ""),
        miniIsoNeutrals = cms.vstring("miniIsoNeutrals",  "-2", "9999999", ""),
        #miniIsoPhotons  = cms.vstring("miniIsoPhotons" ,  "-2", "9999999", ""),
        miniCombRelIsoTTH = cms.vstring("miniCombRelIsoTTH" ,  "-2", "9999999", ""), # toggle
        JetBTagCSV      = cms.vstring("JetBTagCSV"     , "-10",       "1", ""),
        mvaIdTTH        = cms.vstring("mvaIdTTH"       ,  "-1",       "1", ""), # toggle
        tkSigmaPtOverPt = cms.vstring("tkSigmaPtOverPt",   "0", "9999999", ""),
        fixedGridRhoFastjetCentralNeutral = cms.vstring("fixedGridRhoFastjetCentralNeutral", "-1", "9999999", ""),
        ),

    Categories = cms.PSet(
        #PF          = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
        Loose       = cms.vstring( "Loose Id. Muon", "dummy[pass=1,fail=0]"),
        Medium      = cms.vstring("Medium Id. Muon", "dummy[pass=1,fail=0]"),
        #Tight2012   = cms.vstring("Tight Id. Muon", "dummy[pass=1,fail=0]"),
        tag_IsoMu24   = cms.vstring("IsoMu24"  , "dummy[pass=1,fail=0]"),
        #tag_IsoTkMu24 = cms.vstring("IsoTkMu24", "dummy[pass=1,fail=0]"),
    ),

    Expressions = cms.PSet(
        #IP
        #IsoTTHVar = cms.vstring("IsoTTHVar", "(miniIsoCharged+max(0,miniIsoNeutrals+miniIsoPhotons))/pt", "miniIsoCharged", "miniIsoNeutrals", "miniIsoPhotons", "fixedGridRhoFastjetCentralNeutral", "pt"),
        #Loose_noIPVar = cms.vstring("Loose_noIPVar", "PF==1", "PF"),
        #Loose_TTHVar = cms.vstring("Loose_TTHVar", "Loose==1 && abs(dB)<0.05 && abs(dzPV)<0.1 && abs(SIP)<8.0 && miniCombRelIsoTTH<0.4", "Loose", "dB", "dzPV", "SIP", "miniCombRelIsoTTH"), # toggle
        #Medium_noIPVar= cms.vstring("Medium_noIPVar", "Medium==1", "Medium"),
        #Medium_SIPVar = cms.vstring("Medium_SIPVar", "Medium==1 && abs(dB)<0.05 && abs(dzPV)<0.1 && abs(SIP)<4.0", "Medium", "dB", "dzPV", "SIP"),
        #Medium_TTHVar = cms.vstring("Medium_TTHVar", "Medium==1 && abs(dB)<0.05 && abs(dzPV)<0.1 && abs(SIP)<8.0 && JetBTagCSV<0.8484 && tkSigmaPtOverPt<0.2 && mvaIdTTH>0.9 && miniCombRelIsoTTH<0.4", "Medium", "dB", "dzPV", "SIP", "JetBTagCSV", "tkSigmaPtOverPt", "mvaIdTTH", "miniCombRelIsoTTH"), # toggle
        #Tight2012_zIPCutVar = cms.vstring("Tight2012_zIPCut", "Tight2012 == 1 && abs(dzPV) < 0.5", "Tight2012", "dzPV"),
        #tag_IsoMuTkMu24 = cms.vstring("tag_IsoMuTkMu24", "tag_IsoMu24==1 || tag_IsoTkMu24==1", "tag_IsoMu24", "tag_IsoTkMu24"),
    ),

    Cuts = cms.PSet(
        #IP
        #Loose_noIP = cms.vstring("Loose_noIP", "Loose_noIPVar", "0.5"),
        #Loose_TTH = cms.vstring("Loose_TTH", "Loose_TTHVar", "0.5"), # toggle
        #Medium_noIP= cms.vstring("Medium_noIP", "Medium_noIPVar", "0.5"),
        #Medium_SIP = cms.vstring("Medium_SIP", "Medium_SIPVar", "0.5"),
        #Medium_TTH = cms.vstring("Medium_TTH", "Medium_TTHVar", "0.5"), # toggle
        #Tight2012_zIPCut = cms.vstring("Tight2012_zIPCut", "Tight2012_zIPCutVar", "0.5"),
        #Isolations
        #LooseIso4 = cms.vstring("LooseIso4" ,"combRelIsoPF04dBeta", "0.25"),
        #TightIso4 = cms.vstring("TightIso4" ,"combRelIsoPF04dBeta", "0.15"),
        #HNLIso3   = cms.vstring("HNLIso3"   ,"combRelIsoPF03dBeta", "0.10"),
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

    Efficiencies = cms.PSet(), # will be filled later
)

#_*_*_*_*_*_*_*_*_*_*_*_*
#Denominators and Binning
#_*_*_*_*_*_*_*_*_*_*_*_*
#For ID

ETA_BINS = cms.PSet(
    pt  = cms.vdouble(20, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
COARSE_ETA_BINS = cms.PSet(
    #Main
    pt     = cms.vdouble(20, 500),
    abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
VTX_BINS_ETA24  = cms.PSet(
    pt     = cms.vdouble( 20, 500 ),
    abseta = cms.vdouble(  0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
PT_ALLETA_BINS = cms.PSet(
    #Main
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    #For testing bkg function
    #pt     = cms.vdouble(60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
PT_ETA_BINS = cms.PSet(
    #Main
    #pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    #pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 120),
    #For testing bkg function
    #pt     = cms.vdouble(60, 80, 120, 200),
    abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
    
)
LOWPT_ETA_BINS = cms.PSet(
    #Main
    pt     = cms.vdouble(15, 20, 25, 30, 40, 50, 60, 80, 120, 200),
    #pt     = cms.vdouble(5, 10, 15, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
    )
LOWPT_ETA_BINS_VTX_OVER_LOOSE = cms.PSet(
    #Main
    pt     = cms.vdouble(15, 20, 25, 30, 40, 50, 60, 80, 120, 200),
    #pt     = cms.vdouble(5, 10, 15, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
    tag_nVertices = cms.vdouble(0.5, 20.5, 30.5, 60.5),
    #Loose_TTH = cms.vstring("above"),
    Loose = cms.vstring("pass"),
    dB   = cms.vdouble(-0.05, 0.05),
    dzPV = cms.vdouble(-0.1 , 0.1 ),
    SIP  = cms.vdouble(-8.0 , 8.0 ),
    #miniCombRelIsoTTH = cms.vdouble(-2.0 , 0.4 ), # toggle
    )
VTX_COARSEBINS_ETA24  = cms.PSet(
    pt     = cms.vdouble( 15  , 200  ),
    abseta = cms.vdouble(  0.0,   2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    tag_nVertices = cms.vdouble(0.5, 5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5, 40.5, 45.5, 50.5, 55.5, 60.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
VTX_COARSEBINS_ETA24_OVER_LOOSE  = cms.PSet(
    pt     = cms.vdouble( 15  , 200  ),
    abseta = cms.vdouble(  0.0,   2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    tag_nVertices = cms.vdouble(0.5, 5.5, 10.5, 15.5, 20.5, 25.5, 30.5, 35.5, 40.5, 45.5, 50.5, 55.5, 60.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
    #Loose_TTH = cms.vstring("above"),
    Loose = cms.vstring("pass"),
    dB   = cms.vdouble(-0.05, 0.05),
    dzPV = cms.vdouble(-0.1 , 0.1 ),
    SIP  = cms.vdouble(-8.0 , 8.0 ),
    #miniCombRelIsoTTH = cms.vdouble(-2.0 , 0.4 ), # toggle
)

#Additional study for Medium ID (in selected eta region)
PHI_LOWETA = cms.PSet(
    pt     = cms.vdouble(20, 500),
    eta = cms.vdouble(-2.4, -2.1),
    phi =  cms.vdouble(-3.1416, -2.618, -2.0944, -1.5708, -1.0472, -0.5236, 0, 0.5236, 1.0472, 1.5708, 2.0944, 2.618, 3.1416),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
PHI_HIGHETA = cms.PSet(
    pt     = cms.vdouble(20, 500),
    eta = cms.vdouble(2.1, 2.4),
    phi =  cms.vdouble(-3.1416, -2.618, -2.0944, -1.5708, -1.0472, -0.5236, 0, 0.5236, 1.0472, 1.5708, 2.0944, 2.618, 3.1416),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
PT_HIGHABSETA = cms.PSet(
    pt     = cms.vdouble(20, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
VTX_HIGHABSETA  = cms.PSet(
    pt     = cms.vdouble( 20, 500 ),
    abseta = cms.vdouble(2.1, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)

#For IP on ID
LOOSE_ETA_BINS = cms.PSet(
    pt  = cms.vdouble(20, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_COARSE_ETA_BINS = cms.PSet(
    #Main
    pt     = cms.vdouble(20, 500),
    abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_VTX_BINS_ETA24  = cms.PSet(
    pt     = cms.vdouble( 20, 500 ),
    abseta = cms.vdouble(  0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_PT_ALLETA_BINS = cms.PSet(
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
LOOSE_PT_ETA_BINS = cms.PSet(
    #pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    PF = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
    
)
#MEDIUM
MEDIUM_ETA_BINS = cms.PSet(
    pt  = cms.vdouble(20, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_COARSE_ETA_BINS = cms.PSet(
    #Main
    pt     = cms.vdouble(20, 500),
    abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_VTX_BINS_ETA24  = cms.PSet(
    pt     = cms.vdouble( 20, 500 ),
    abseta = cms.vdouble(  0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_PT_ALLETA_BINS = cms.PSet(
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUM_PT_ETA_BINS = cms.PSet(
    #pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium = cms.vstring("pass"), 
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
MEDIUMSIP_LOWPT_ETA_BINS = cms.PSet(
    pt     = cms.vdouble(5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 120, 200),
    #pt     = cms.vdouble(5, 10, 15, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble(0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Medium = cms.vstring("pass"), 
    dB   = cms.vdouble(-0.05, 0.05),
    dzPV = cms.vdouble(-0.10, 0.10),
    SIP  = cms.vdouble(-4.00, 4.00),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
#TIGHT
TIGHT_ETA_BINS = cms.PSet(
    pt  = cms.vdouble(20, 500),
    eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Tight2012 = cms.vstring("pass"), 
    dzPV = cms.vdouble(-0.5, 0.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
TIGHT_COARSE_ETA_BINS = cms.PSet(
    #Main
    pt     = cms.vdouble(20, 500),
    abseta = cms.vdouble(0.0, 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Tight2012 = cms.vstring("pass"), 
    dzPV = cms.vdouble(-0.5, 0.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
TIGHT_VTX_BINS_ETA24  = cms.PSet(
    pt     = cms.vdouble( 20, 500 ),
    abseta = cms.vdouble(  0.0, 2.4),
    tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Tight2012 = cms.vstring("pass"), 
    dzPV = cms.vdouble(-0.5, 0.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
TIGHT_PT_ALLETA_BINS = cms.PSet(
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    abseta = cms.vdouble(  0.0, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Tight2012 = cms.vstring("pass"), 
    dzPV = cms.vdouble(-0.5, 0.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
)
TIGHT_PT_ETA_BINS = cms.PSet(
    #pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 120, 200),
    pt     = cms.vdouble(20, 25, 30, 40, 50, 60, 120),
    #pt     = cms.vdouble(10, 20, 25, 30, 40, 50, 60, 120),
    abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4),
    pair_probeMultiplicity = cms.vdouble(0.5, 1.5),
    Tight2012 = cms.vstring("pass"), 
    dzPV = cms.vdouble(-0.5, 0.5),
    #tag selections
    tag_pt = cms.vdouble(25, 500),
    tag_IsoMu24 = cms.vstring("pass"), 
    tag_combRelIsoPF04dBeta = cms.vdouble(-0.5, 0.2),
    
)


tuplesDir = '/user/tomc/public/tagAndProbe/merged/'
if scenario == 'data':
  if sample == 'all': sample = ['B','C','D','E','F','G','H-v2','H-v3']
  else:               sample = [sample]
  samples = [(tuplesDir + 'run' + r + '.root') for r in sample]
  process.TnP_MuonID = Template.clone(
      InputFileNames = cms.vstring(*samples),
      InputTreeName = cms.string("fitter_tree"),
      InputDirectoryName = cms.string("tpTree"),
      OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
      Efficiencies = cms.PSet(),
  )

elif scenario == 'mc':
   process.TnP_MuonID = Template.clone(
     InputFileNames = cms.vstring(tuplesDir + 'DY.root'),
     InputTreeName = cms.string("fitter_tree"),
     InputDirectoryName = cms.string("tpTree"),
     OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
     Efficiencies = cms.PSet(),
     )
     process.TnP_MuonID.WeightVariable = cms.string("weight")
     process.TnP_MuonID.Variables.weight = cms.vstring("weight","-10","10","")

ID_BINS = []

#_*_*_*_*_*_*_*_*_*_*
#IDs
#_*_*_*_*_*_*_*_*_*_*
#Loose ID
if id_bins == '1':
    ID_BINS = [
    #(("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_eta", ETA_BINS)),
    #(("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_coarse_eta", COARSE_ETA_BINS)),
    #(("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_vtx_bin1_24", VTX_BINS_ETA24 )),
    #(("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_pt_alleta_bin1", PT_ALLETA_BINS)),
    (("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_pt_spliteta_bin1", PT_ETA_BINS)),
    ]
#Medium ID
if id_bins == '2':
    ID_BINS = [
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_eta", ETA_BINS)),
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_coarse_eta", COARSE_ETA_BINS)),
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_vtx_bin1_24", VTX_BINS_ETA24 )),
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_pt_alleta_bin1", PT_ALLETA_BINS)),
    (("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_pt_spliteta_bin1", PT_ETA_BINS)),
    ]
#Tight ID
if id_bins == '3':
    ID_BINS = [
    #(("Tight2012_zIPCut"), ("NUM_TightIDandIPCut_DEN_genTracks_PAR_eta", ETA_BINS)),
    #(("Tight2012_zIPCut"), ("NUM_TightID_DEN_genTracks_PAR_coarse_eta", COARSE_ETA_BINS)),
    #(("Tight2012_zIPCut"), ("NUM_TightIDandIPCut_DEN_genTracks_PAR_vtx_bin1_24", VTX_BINS_ETA24 )),
    #(("Tight2012_zIPCut"), ("NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_alleta_bin1", PT_ALLETA_BINS)),
    (("Tight2012_zIPCut"), ("NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1", PT_ETA_BINS)),
    ]
#Additional studies on Medium ID (in selected eta region)
#Medium ID
if id_bins == '4':
    ID_BINS = [
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_phi_loweta", PHI_LOWETA)),
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_phi_higheta", PHI_HIGHETA )),
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_pt_highabseta", PT_HIGHABSETA)),
    #(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_vtx_highabseta", VTX_HIGHABSETA)),
    ]
#_*_*_*_*_*_*_*_*_*_*
#ISOs
#_*_*_*_*_*_*_*_*_*_*
#Loose Iso
if id_bins == '5':
    ID_BINS = [
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_LooseID_PAR_eta", LOOSE_ETA_BINS)),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_LooseID_PAR_coarse_eta", LOOSE_COARSE_ETA_BINS)),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_LooseID_PAR_vtx_bin1_24", LOOSE_VTX_BINS_ETA24 )),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_LooseID_PAR_pt_alleta_bin1", LOOSE_PT_ALLETA_BINS)),
    (("LooseIso4"), ("NUM_LooseRelIso_DEN_LooseID_PAR_pt_spliteta_bin1", LOOSE_PT_ETA_BINS)),
    ]
if id_bins == '6':
    ID_BINS = [
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_MediumID_PAR_eta", MEDIUM_ETA_BINS)),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_MediumID_PAR_coarse_eta", MEDIUM_COARSE_ETA_BINS)),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_MediumID_PAR_vtx_bin1_24", MEDIUM_VTX_BINS_ETA24 )),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_MediumID_PAR_pt_alleta_bin1", MEDIUM_PT_ALLETA_BINS)),
    (("LooseIso4"), ("NUM_LooseRelIso_DEN_MediumID_PAR_pt_spliteta_bin1", MEDIUM_PT_ETA_BINS)),
    ]
if id_bins == '7':
    ID_BINS = [
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_TightID_PAR_eta", TIGHT_ETA_BINS)),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_TightID_PAR_coarse_eta", TIGHT_COARSE_ETA_BINS)),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_TightID_PAR_vtx_bin1_24", TIGHT_VTX_BINS_ETA24 )),
    #(("LooseIso4"), ("NUM_LooseRelIso_DEN_TightID_PAR_pt_alleta_bin1", TIGHT_PT_ALLETA_BINS)),
    (("LooseIso4"), ("NUM_LooseRelIso_DEN_TightID_PAR_pt_spliteta_bin1", TIGHT_PT_ETA_BINS)),
    ]
#Tight Iso
if id_bins == '8':
    ID_BINS = [
    #(("TightIso4"), ("NUM_TightRelIso_DEN_TightID_PAR_eta", TIGHT_ETA_BINS)),
    #(("TightIso4"), ("NUM_TightRelIso_DEN_TightID_PAR_coarse_eta", TIGHT_COARSE_ETA_BINS)),
    #(("TightIso4"), ("NUM_TightRelIso_DEN_TightID_PAR_vtx_bin1_24", TIGHT_VTX_BINS_ETA24 )),
    #(("TightIso4"), ("NUM_TightRelIso_DEN_TightID_PAR_pt_alleta_bin1", TIGHT_PT_ALLETA_BINS)),
    (("TightIso4"), ("NUM_TightRelIso_DEN_TightID_PAR_pt_spliteta_bin1", TIGHT_PT_ETA_BINS)),
    ]
if id_bins == '9':
    ID_BINS = [
    #(("TightIso4"), ("NUM_TightRelIso_DEN_MediumID_PAR_eta", MEDIUM_ETA_BINS)),
    #(("TightIso4"), ("NUM_TightRelIso_DEN_MediumID_PAR_coarse_eta", MEDIUM_COARSE_ETA_BINS)),
    #(("TightIso4"), ("NUM_TightRelIso_DEN_MediumID_PAR_vtx_bin1_24", MEDIUM_VTX_BINS_ETA24 )),
    #(("TightIso4"), ("NUM_TightRelIso_DEN_MediumID_PAR_pt_alleta_bin1", MEDIUM_PT_ALLETA_BINS)),
    (("TightIso4"), ("NUM_TightRelIso_DEN_MediumID_PAR_pt_spliteta_bin1", MEDIUM_PT_ETA_BINS)),
    ]
#Jobs to studie the bkg fit funciton on TightID
#if id_bins == '10': ID_BINS = [(("Tight2012_zIPCut"), ("NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_alleta_bin1", PT_ALLETA_BINS))]
#if id_bins == '11': ID_BINS = [(("Tight2012_zIPCut"), ("NUM_TightIDandIPCut_DEN_genTracks_PAR_pt_spliteta_bin1", PT_ETA_BINS))]
#if id_bins == '12': ID_BINS = [(("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_pt_alleta_bin1", PT_ALLETA_BINS))]
#if id_bins == '13': ID_BINS = [(("Loose_noIP"), ("NUM_LooseID_DEN_genTracks_PAR_pt_spliteta_bin1", PT_ETA_BINS))]
#if id_bins == '14': ID_BINS = [(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_pt_alleta_bin1", PT_ALLETA_BINS))]
#if id_bins == '15': ID_BINS = [(("Medium_noIP"), ("NUM_MediumID_DEN_genTracks_PAR_pt_spliteta_bin1", PT_ETA_BINS))]

# For AN-17-014 (HNL) 
#  - ID cuts: (Medium ID + SIP) / (General track) 
if id_bins == '10':
    ID_BINS = [
        (("Medium_SIP"), ("NUM_HNLMediumID_DEN_genTracks_PAR_pt_spliteta_bin1", LOWPT_ETA_BINS))
        ]

#  - Isolation cut: (relIsoDBeta < 0.1) / (Medium ID + SIP) 
if id_bins == '20':
    ID_BINS = [
        (("HNLIso3"), ("NUM_HNLRelIso_DEN_MediumIDSIP_PAR_pt_spliteta_bin1", MEDIUMSIP_LOWPT_ETA_BINS))
        ]

#  - ID for TTH: 
if id_bins == '30':
    ID_BINS = [
        #(("Medium_TTH"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_pt_abseta_vtx", LOWPT_ETA_BINS_VTX_OVER_LOOSE  )), # toggle
        #(("Medium_TTH"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_coarsevtx"    , VTX_COARSEBINS_ETA24_OVER_LOOSE)) # toggle
        (("Medium"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_pt_abseta_vtx", LOWPT_ETA_BINS_VTX_OVER_LOOSE  )), # toggle
        (("Medium"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_coarsevtx"    , VTX_COARSEBINS_ETA24_OVER_LOOSE)) # toggle
        ]


for ID, ALLBINS in ID_BINS:
    X = ALLBINS[0]
    B = ALLBINS[1]
    _output = os.getcwd() 
    # _output = os.getcwd() + '/Efficiency_' + iteration
    # if not os.path.exists(_output):
    #     print 'Creating', '/Efficiency_' + iteration,'directory where the fits are stored'  
    #     os.makedirs(_output)
    # if scenario == 'data_all':
    #     _output += '/DATA' + '_' + sample
    # elif scenario == 'mc_all':
    #     _output += '/MC' + '_' + sample
    # if not os.path.exists(_output):
    #     os.makedirs(_output)
    module = process.TnP_MuonID.clone(OutputFileName = cms.string(_output + "/TnP_%s_%s_%s.root" % (scenario,sample,X)))
    #save the fitconfig in the plot directory
    #shutil.copyfile(os.getcwd()+'/fitMuonID.py',_output+'/fitMuonID.py')
    shape = cms.vstring("vpvPlusExpo")
    #shape = "vpvPlusCheb"
    if not "Iso" in ID:  #customize only for ID
        shape = cms.vstring("vpvPlusExpo","*pt_bin6*","vpvPlusCheb") #for pT>50 GeV (low-pt bins, from pt=15)
        #shape = cms.vstring("vpvPlusExpo","*pt_bin8*","vpvPlusCheb") #for pT>50 GeV (low-pt bins, from pt=5)
        # if (len(B.pt)==7):  #customize only when the pT have the high pt bins
        #     shape = cms.vstring("vpvPlusExpo","*pt_bin5*","vpvPlusCheb")
    DEN = B.clone(); num = ID;
    

    #compute isolation efficiency 
    if scenario == 'data_all':
        if num.find("Iso3") != -1 or num.find("Iso4") != -1: 
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num,"below"),
                UnbinnedVariables = cms.vstring("mass"),
                BinnedVariables = DEN,
                #BinToPDFmap = cms.vstring(shape)
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num,"above"),
                UnbinnedVariables = cms.vstring("mass"),
                BinnedVariables = DEN,
                #BinToPDFmap = cms.vstring(shape)
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)        
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
    elif scenario == 'mc_all':
        if num.find("Iso3") != -1 or num.find("Iso4") != -1: 
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num,"below"),
                #UnbinnedVariables = cms.vstring("mass","weight"),
                UnbinnedVariables = cms.vstring("mass"),
                BinnedVariables = DEN,
                #BinToPDFmap = cms.vstring(shape)
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num,"above"),
                #UnbinnedVariables = cms.vstring("mass","weight"),
                UnbinnedVariables = cms.vstring("mass"),
                BinnedVariables = DEN,
                #BinToPDFmap = cms.vstring(shape)
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)        
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))

# from customizeTnPforSysts import customizeTnPforSysts
# customizeTnPforSysts(process)
