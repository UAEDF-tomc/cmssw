#! /bin/bash

eval `scramv1 runtime -sh`
cd $CMSSW_BASE/src/ && scram b -j 15 -k
cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test

mkdir -p log

cmsRun fitterSusy.py onlyData=True onlyId=True &> log/data_id.log &
cmsRun fitterSusy.py onlyMC=True   onlyId=True &> log/mc_id.log &
#cmsRun fitterSusy.py onlyData=True onlyIso=True doAct=True &> log/data_act.log &
#cmsRun fitterSusy.py onlyMC=True   onlyIso=True doAct=True &> log/mc_act.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True &> log/data_eta.log &
cmsRun fitterSusy.py onlyMC=True   onlyIso=True &> log/mc_eta.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True part2=True &> log/data_eta2.log &
cmsRun fitterSusy.py onlyMC=True   onlyIso=True part2=True &> log/mc_eta2.log &
wait

cmsRun fitterSusy.py onlyMC=True onlyId=True altMC=True &> log/mc_id_altMC.log &
cmsRun fitterSusy.py onlyMC=True onlyIso=True altMC=True &> log/mc_eta_altMC.log &
cmsRun fitterSusy.py onlyMC=True onlyIso=True altMC=True part2=True &> log/mc_eta2_altMC.log &

cmsRun fitterSusy.py onlyData=True onlyId=True altTag=True &> log/data_id_altTag.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altTag=True &> log/data_eta_altTag.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altTag=True part2=True &> log/data_eta2_altTag.log &
wait

cmsRun fitterSusy.py onlyData=True onlyId=True altBkg=True &> log/data_id_altBkg.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altBkg=True &> log/data_eta_altBkg.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altBkg=True part2=True &> log/data_eta2_altBkg.log &

cmsRun fitterSusy.py onlyData=True onlyId=True altSig=True &> log/data_id_altSig.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altSig=True &> log/data_eta_altSig.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True altSig=True part2=True &> log/data_eta2_altSig.log &

wait
rm -r temp*
