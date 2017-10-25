#!/bin/bash
cd "/user/tomc/tagAndProbe/CMSSW_8_0_20/src/PhysicsTools/TagAndProbe/test"
source $VO_CMS_SW_DIR/cmsset_default.sh
eval `scram runtime -sh`
eval $command
