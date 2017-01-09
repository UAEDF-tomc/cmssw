#!/usr/bin/env python
import glob, os

for file in glob.glob("../tables/eff*.txt"):
  os.system("python EGammaID_scaleFactors.py " + file)
os.system("rsync -rutv output tomc@lxplus.cern.ch:~/www/tagAndProbe/december2016/")
