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

cmsRun fitterSusy.py onlyMC=True onlyId=True sysMC=True &> mc_id_sysMC.log &
cmsRun fitterSusy.py onlyMC=True onlyIso=True sysMC=True &> mc_eta_sysMC.log &

cmsRun fitterSusy.py onlyData=True onlyId=True sysTag=True &> data_id_sysTag.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True sysTag=True &> data_eta_sysTag.log &

cmsRun fitterSusy.py onlyData=True onlyId=True sysBackShape=True &> data_id_sysBackShape.log &
cmsRun fitterSusy.py onlyData=True onlyIso=True sysBackShape=True &> data_eta_sysBackShape.log &

wait
rm -r temp*
