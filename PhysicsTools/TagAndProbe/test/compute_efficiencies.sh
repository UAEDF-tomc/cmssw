#! /bin/bash

eval `scramv1 runtime -sh`
cd $CMSSW_BASE/src/ && scram b -j 15 -k
cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test

#cmsRun fitterSusy.py onlyData=True onlyId=True &> data_id.log &
#cmsRun fitterSusy.py onlyMC=True   onlyId=True &> mc_id.log &
#cmsRun fitterSusy.py onlyData=True onlyIso=True doAct=True &> data_act.log &
#cmsRun fitterSusy.py onlyMC=True   onlyIso=True doAct=True &> mc_act.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True &> data_eta.log &
cmsRun fitterSusy.py onlyMC=True   onlyIso=True &> mc_eta.log &

wait
# Remove all those temporary directories which get created by the TagProbeFitter
rm -r *probe_Ele*

