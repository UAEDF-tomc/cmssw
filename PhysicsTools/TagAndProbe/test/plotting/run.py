#!/usr/bin/env python
import glob, os

for file in glob.glob("../eff*.txt"):
  os.system("python EGammaID_scaleFactors.py " + file)
