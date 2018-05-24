#!/usr/bin/env python
import glob, os

for file in glob.glob("../tables*PV*2016/*TTV*.txt"):
  print file
  os.system("python muon_scaleFactors.py --plot=1 --file=" + file)
  os.system("python muon_scaleFactors.py --plot=2 --file=" + file)
