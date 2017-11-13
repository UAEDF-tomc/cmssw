#!/usr/bin/env python
import glob, os

#for file in glob.glob("../tables/eff*.txt"):
for file in glob.glob("../tables/eff_all_GsfElectronToTTG.txt"):
  os.system("python EGammaID_scaleFactors.py " + file)
