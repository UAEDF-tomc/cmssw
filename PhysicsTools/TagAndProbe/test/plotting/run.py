#!/usr/bin/env python
import glob, os

for file in glob.glob("../tables_*/*TTV*.txt"):
  print file
  os.system("python EGammaID_scaleFactors.py --plot=1 --file=" + file)
  os.system("python EGammaID_scaleFactors.py --plot=2 --file=" + file)
