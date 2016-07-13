import FWCore.ParameterSet.Config as cms

alleta = cms.PSet(
Veto_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Medium_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose2D_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
FOID2D_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2D3D_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
TightID2D3D_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini4_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseConvIHit1_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightConvIHit0Chg_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMulti_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMultiEmu_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVL_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaL_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaM_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaT_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVT_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaET_alleta_10p0To20p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_10.0To20.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_alleta_20p0To30p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_20.0To30.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_alleta_30p0To40p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_30.0To40.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_alleta_40p0To50p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_40.0To50.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_alleta_50p0To200p0_0p0To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_alleta.root\", \"hMass_50.0To200.0_0.0To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
)

barrel = cms.PSet(
Veto_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Medium_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose2D_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
FOID2D_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2D3D_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
TightID2D3D_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini4_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseConvIHit1_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightConvIHit0Chg_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMulti_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMultiEmu_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVL_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaL_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaM_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaT_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVT_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaET_barrel_10p0To20p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_10.0To20.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_10p0To20p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_10.0To20.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_20p0To30p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_20.0To30.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_20p0To30p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_20.0To30.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_30p0To40p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_30.0To40.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_30p0To40p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_30.0To40.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_40p0To50p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_40.0To50.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_40p0To50p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_40.0To50.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_50p0To200p0_0p0To0p8 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_50.0To200.0_0.0To0.8_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_barrel_50p0To200p0_0p8To1p442 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_barrel.root\", \"hMass_50.0To200.0_0.8To1.442_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
)

crack = cms.PSet(
Veto_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Medium_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose2D_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
FOID2D_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2D3D_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
TightID2D3D_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini4_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseConvIHit1_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightConvIHit0Chg_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMulti_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMultiEmu_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVL_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaL_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaM_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaT_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVT_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaET_crack_10p0To20p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_10.0To20.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_crack_20p0To30p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_20.0To30.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_crack_30p0To40p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_30.0To40.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_crack_40p0To50p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_40.0To50.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_crack_50p0To200p0_1p442To1p566 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_crack.root\", \"hMass_50.0To200.0_1.442To1.566_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
)

endcap = cms.PSet(
Veto_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Veto_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToVeto_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Medium_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Medium_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToMedium_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Loose2D_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Loose2D_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLoose2D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
FOID2D_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

FOID2D_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToFOID2D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
Tight2D3D_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

Tight2D3D_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTight2D3D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
TightID2D3D_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

TightID2D3D_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToTightID2D3D_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseMini4_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseMini4_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToMini4_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVAVLooseConvIHit1_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVAVLooseConvIHit1_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVAVLooseElectronToConvIHit1_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightConvIHit0Chg_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightConvIHit0Chg_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToConvIHit0Chg_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMulti_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMulti_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMulti_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
MVATightMultiEmu_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

MVATightMultiEmu_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/MVATightElectronToMultiEmu_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVL_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVL_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVL_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaL_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaL_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaL_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaM_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaM_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaM_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaT_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaT_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaT_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaVT_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaVT_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaVT_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
LeptonMvaET_endcap_10p0To20p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_10.0To20.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_endcap_20p0To30p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_20.0To30.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_endcap_30p0To40p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_30.0To40.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_endcap_40p0To50p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_40.0To50.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),

LeptonMvaET_endcap_50p0To200p0_1p566To2p5 = cms.vstring(
"RooGaussian::signalResPass(mass, meanP[0.0,-10.000,10.000],sigmaP[1.0,0.001,10.000])",
"RooGaussian::signalResFail(mass, meanF[0.0,-10.000,10.000],sigmaF[1.0,0.001,10.000])",
"ZGeneratorLineShape::signalPhyPass(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Pass\")",
"ZGeneratorLineShape::signalPhyFail(mass,\"../data/GsfElectronToLeptonMvaET_endcap.root\", \"hMass_50.0To200.0_1.566To2.5_Fail\")",
"RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0, 70, 80])",
"RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0, 70, 80])",
"FCONV::signalPass(mass, signalPhyPass, signalResPass)",
"FCONV::signalFail(mass, signalPhyFail, signalResFail)",
"efficiency[0.5,0,1]",
"signalFractionInPassing[1.0]"
),
)

all_pdfs = cms.PSet(
  alleta,
  barrel,
  crack,
  endcap,
)
