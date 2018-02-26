import FWCore.ParameterSet.Config as cms
### USAGE:
###
###
###
###

#### 
#### For systematics studies: 
#### .1. ID with data and MC: 
####     cmsRun fitMuonID_id.py TEST  data_all 
####     cmsRun fitMuonID_id.py TEST  mc_all LO 

import sys, os, shutil
args = sys.argv[1:]
iteration = 'TEST'
if len(args) > 1: iteration = args[1]
print "The iteration is", iteration
id_bins = '1'
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

#set different mass range if iso
_mrange = "70"
if (int(id_bins) > 4) and (int(id_bins) < 10): _mrange = "77"
if (int(id_bins) == 10 or int(id_bins) == 20): _mrange = "77" 
print '_mrange is', _mrange


Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer", NumCPU = cms.uint32(1), SaveWorkspace = cms.bool(False),
    Variables = cms.PSet(
        #weight                           = cms.vstring("weight","-100","100",""),
        mass                              = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}"),
        ###mass                           = cms.vstring("Tag-muon Mass", "70", "130", "GeV/c^{2}"),
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
        miniIsoCharged                    = cms.vstring("miniIsoCharged" ,  "-2", "9999999", ""),
        miniIsoNeutrals                   = cms.vstring("miniIsoNeutrals",  "-2", "9999999", ""),
        miniIsoPhotons                    = cms.vstring("miniIsoPhotons" ,  "-2", "9999999", ""),
        miniCombRelIsoTTH                 = cms.vstring("miniCombRelIsoTTH" ,  "-2", "9999999", ""), # toggle
        JetBTagCSV                        = cms.vstring("JetBTagCSV"     , "-10",       "1", ""),
        mvaIdTTH                          = cms.vstring("mvaIdTTH"       ,  "-1",       "1", ""), # toggle
        tkSigmaPtOverPt                   = cms.vstring("tkSigmaPtOverPt",   "0", "9999999", ""),
        fixedGridRhoFastjetCentralNeutral = cms.vstring("fixedGridRhoFastjetCentralNeutral", "-1", "9999999", ""),
        ),

    Categories = cms.PSet(
       #PF            = cms.vstring("PF Muon", "dummy[pass=1,fail=0]"),
        Loose         = cms.vstring("Loose Id. Muon",  "dummy[pass=1,fail=0]"),
        Medium        = cms.vstring("Medium Id. Muon", "dummy[pass=1,fail=0]"),
       #Tight2012     = cms.vstring("Tight Id. Muon", "dummy[pass=1,fail=0]"),
        tag_IsoMu24   = cms.vstring("IsoMu24"  , "dummy[pass=1,fail=0]"),
       #tag_IsoTkMu24 = cms.vstring("IsoTkMu24", "dummy[pass=1,fail=0]"),
    ),

    Expressions = cms.PSet(
      Feb2018LooseVar      = cms.vstring("Feb2018LooseVar",    "Medium==1 && abs(dB)<0.05 && abs(dzPV)<0.1 && abs(SIP)<8.0 && miniCombRelIsoTTH<0.4", "Loose", "dB", "dzPV", "SIP", "miniCombRelIsoTTH"),
      Feb2018LeptonMvaLVar = cms.vstring("Feb2018LeptonMvaL",  "Feb2018LooseVar==1 && mvaIdTTH > 0.8"),
      Feb2018LeptonMvaMVar = cms.vstring("Feb2018LeptonMvaM",  "Feb2018LooseVar==1 && mvaIdTTH > 0.85"),
      Feb2018LeptonMvaTVar = cms.vstring("Feb2018LeptonMvaT",  "Feb2018LooseVar==1 && mvaIdTTH > 0.9"),
      tkSigmaPtOverPtVar   = cms.vstring("tkSigmaPtOverPtVar", "tkSigmaPtOverPt<0.2"
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

ID_BINS = [
    #(("Medium_TTH"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_pt_abseta_vtx", LOWPT_ETA_BINS_VTX_OVER_LOOSE  )), # toggle
    #(("Medium_TTH"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_coarsevtx"    , VTX_COARSEBINS_ETA24_OVER_LOOSE)) # toggle
    (("Feb2018Loose"),      ("NUM_TTHMedium_DEN_TTHLoose_PAR_pt_abseta_vtx", LOWPT_ETA_BINS_VTX_OVER_LOOSE  )), # toggle
    (("Feb2018LeptonMvaL"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_coarsevtx"    , VTX_COARSEBINS_ETA24_OVER_LOOSE)) # toggle
    (("Feb2018LeptonMvaM"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_coarsevtx"    , VTX_COARSEBINS_ETA24_OVER_LOOSE)) # toggle
    (("Feb2018LeptonMvaT"), ("NUM_TTHMedium_DEN_TTHLoose_PAR_coarsevtx"    , VTX_COARSEBINS_ETA24_OVER_LOOSE)) # toggle
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
    module = process.TnP_MuonID.clone(OutputFileName = cms.string(_output + "/TnP_%s_%s.root" % (scenario,X)))
    print "Output: " + (_output + "/TnP_%s_%s.root" % (scenario,X))
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
    if scenario == 'data':
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
    elif scenario == 'mc':
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

#from customizeTnPforSysts import customizeTnPforSysts
#customizeTnPforSysts(process)
