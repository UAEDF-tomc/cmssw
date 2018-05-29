#!/usr/bin/env python
import glob, ROOT, os

for f in glob.glob('./efficiencies/2016/*/*/*/*.root'):
  try:
    print f
    file = ROOT.TFile(f, "update")
    dir  = file.Get('tpTree')
    key  = dir.GetListOfKeys()[0]
    file.cd('tpTree/' + key.GetName())
    ROOT.gDirectory.Delete('fitter_tree;*')
    file.Close()
    ftemp = f.replace('.root', '_temp.root')
    os.system('mv ' + f + ' ' + ftemp + ';hadd -f ' + f + ' ' + ftemp + ' &> /dev/null;rm ' + ftemp)
  except:
    pass
