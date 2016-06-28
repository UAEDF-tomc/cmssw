import FWCore.ParameterSet.Config as cms

def AdjustOptions(options, varOptions):
    options["MAXEVENTS"] = cms.untracked.int32(10000)
    options['DoRECO']    = cms.bool(True)

    # Needs update (or keep using the defaults)
#    if varOptions.isMC:
#        options["TnPPATHS"]            = cms.vstring("HLT_Ele22_eta2p1_WP75_Gsf_v*")
#        options["TnPHLTTagFilters"]    = cms.vstring("hltSingleEle22WP75GsfTrackIsoFilter")
#        options["HLTFILTERTOMEASURE"]  = cms.vstring("hltSingleEle22WP75GsfTrackIsoFilter")
#    else:
#        options["TnPPATHS"]            = cms.vstring("HLT_Ele22_eta2p1_WPLoose_Gsf_v*")
#        options["TnPHLTTagFilters"]    = cms.vstring("hltSingleEle22WPLooseGsfTrackIsoFilter")
#        options["HLTFILTERTOMEASURE"]  = cms.vstring("hltSingleEle22WPLooseGsfTrackIsoFilter")
