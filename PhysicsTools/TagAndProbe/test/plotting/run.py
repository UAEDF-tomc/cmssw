#!/usr/bin/env python
import glob, os, time

for file in glob.glob("../tables/eff*.txt"):
  os.system("python EGammaID_scaleFactors.py " + file)
  time.sleep(3)
