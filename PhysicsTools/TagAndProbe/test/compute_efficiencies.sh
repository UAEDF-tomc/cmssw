#! /bin/bash

eval `scramv1 runtime -sh`
cd $CMSSW_BASE/src/ && scram b -j 15 -k
cd $CMSSW_BASE/src/PhysicsTools/TagAndProbe/test

cmsRun fitterSusy.py noData=True noIso=True &> mc_id.log &
cmsRun fitterSusy.py noMC=True noIso=True &> data_id.log &
#cmsRun fitterSusy.py noData=True noID=True doEta=False &> mc_act.log &
#cmsRun fitterSusy.py noMC=True noID=True doEta=False &> data_act.log &
cmsRun fitterSusy.py noData=True noID=True doEta=True &> mc_eta.log &
cmsRun fitterSusy.py noMC=True noID=True doEta=True &> data_eta.log &

wait
