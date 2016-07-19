#! /bin/bash

eval `scramv1 runtime -sh`
cd $CMSSW_BASE/src/ && scram b -j 15 -k
cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test

cmsRun fitterSusy.py onlyData=True onlyId=True &> data_id.log &
cmsRun fitterSusy.py onlyMC=True   onlyId=True &> mc_id.log &
#cmsRun fitterSusy.py onlyData=True onlyIso=True doAct=True &> data_act.log &
#cmsRun fitterSusy.py onlyMC=True   onlyIso=True doAct=True &> mc_act.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True &> data_eta.log &
cmsRun fitterSusy.py onlyMC=True   onlyIso=True &> mc_eta.log &

cmsRun fitterSusy.py onlyMC=True onlyId=True altMC=True &> mc_id_altMC.log &
cmsRun fitterSusy.py onlyMC=True onlyIso=True altMC=True &> mc_eta_altMC.log &

cmsRun fitterSusy.py onlyData=True onlyId=True altTag=True &> data_id_altTag.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altTag=True &> data_eta_altTag.log &

cmsRun fitterSusy.py onlyData=True onlyId=True altBkg=True &> data_id_altBkg.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altBkg=True &> data_eta_altBkg.log &

cmsRun fitterSusy.py onlyData=True onlyId=True altSig=True &> data_id_altSig.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altSig=True &> data_eta_altSig.log &

wait
rm -r temp*
