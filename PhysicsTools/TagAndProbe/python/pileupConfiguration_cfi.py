import FWCore.ParameterSet.Config as cms

#### MC PU DISTRIBUTIONS
from SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi import mix as mix_2016_25ns

pu_distribs = {"80X_mcRun2_asymptotic_v1"  : mix_2016_25ns.input.nbPileupEvents.probValue}

#### DATA PU DISTRIBUTIONS
data_pu_distribs = { "Jamboree_golden_JSON" : [5.12e+04,3.66e+05,5.04e+05,4.99e+05,7.5e+05,1.1e+06,2.53e+06,9.84e+06,4.4e+07,1.14e+08,1.94e+08,2.63e+08,2.96e+08,2.74e+08,2.06e+08,1.26e+08,6.38e+07,2.73e+07,1.1e+07,5.2e+06,3.12e+06,1.87e+06,9.35e+05,3.64e+05,1.1e+05,2.64e+04,5.76e+03,1.53e+03,594,278,131,59.8,26,10.8,4.29,1.62,0.587,0.203,0.0669,0.0211,0.00633,0.00182,0.000498,0.00013,3.26e-05,7.77e-06,1.77e-06,3.85e-07,7.99e-08,1.58e-08,3e-09,5.43e-10],
                     "ICHEP2016_JSON"       : [1.78e+03,2.69e+04,1.78e+05,4.71e+05,7.61e+05,1.02e+06,1.48e+06,7.35e+06,2.3e+07,3.75e+07,6.01e+07,9.32e+07,1.41e+08,2.09e+08,2.88e+08,3.53e+08,3.93e+08,4.09e+08,4e+08,3.69e+08,3.23e+08,2.69e+08,2.12e+08,1.57e+08,1.09e+08,6.96e+07,4.09e+07,2.19e+07,1.07e+07,4.8e+06,1.99e+06,7.76e+05,2.9e+05,1.07e+05,4.22e+04,1.95e+04,1.16e+04,8.73e+03,7.5e+03,6.85e+03,6.44e+03,6.16e+03,5.96e+03,5.81e+03,5.67e+03,5.53e+03,5.38e+03,5.21e+03,5.01e+03,4.78e+03],
                     "MORIOND2017"          : [2.59e+05,1.32e+06,2.56e+06,4.02e+06,5.62e+06,7.18e+06,1.04e+07,3.07e+07,7.64e+07,1.85e+08,4.04e+08,7.01e+08,1.04e+09,1.4e+09,1.77e+09,2.05e+09,2.22e+09,2.3e+09,2.34e+09,2.36e+09,2.34e+09,2.25e+09,2.13e+09,1.98e+09,1.81e+09,1.62e+09,1.43e+09,1.25e+09,1.06e+09,8.85e+08,7.21e+08,5.75e+08,4.48e+08,3.41e+08,2.54e+08,1.83e+08,1.28e+08,8.56e+07,5.49e+07,3.35e+07,1.94e+07,1.07e+07,5.55e+06,2.73e+06,1.27e+06,5.63e+05,2.37e+05,9.71e+04,4.01e+04,1.81e+04,1e+04,7.03e+03,5.85e+03,5.25e+03,4.84e+03,4.47e+03,4.11e+03,3.76e+03,3.41e+03,3.06e+03] }


pileupProducer = cms.EDProducer("PileupWeightProducer",
                                #hardcodedWeights = cms.untracked.bool(True),
                                pileupInfoTag    = cms.InputTag("slimmedAddPileupInfo"),
                                PileupMC = cms.vdouble(pu_distribs["80X_mcRun2_asymptotic_v1"]),
                                PileupData = cms.vdouble(data_pu_distribs["MORIOND2017"]),
                                )
