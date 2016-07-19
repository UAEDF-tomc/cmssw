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

# TODO: due to bad design of this horrible TnP package you can only run those below after cleaning up the temp files from above, otherwise you end up with segFaults
#cmsRun fitterSusy.py onlyMC=True onlyId=True sysMC=True &> mc_id_sysMC.log &
#cmsRun fitterSusy.py onlyMC=True onlyIso=True doAct=True sysMC=True &> mc_act.log &
#cmsRun fitterSusy.py onlyMC=True onlyIso=True sysMC=True &> mc_eta_sysMC.log &

wait
