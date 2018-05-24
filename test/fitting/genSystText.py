#! /usr/bin/env python

import os
import ROOT

def Histo(fileName, bin):
  parent = ROOT.TFile(fileName)
  sub1   = parent.Get('tpTree').GetListOfKeys()
  for ikey1 in xrange(sub1.GetSize()):
    key1 = sub1.At(ikey1)
    dir1 = parent.Get('tpTree/' + key1.GetName())
    sub2 = dir1.GetListOfKeys()
    subdir = dir1.Get("fit_eff_plots")
    subkeys = subdir.GetListOfKeys()
    for ikey in xrange(subkeys.GetSize()):
      key = subkeys.At(ikey)
      if not ('PLOT_pt_bin'+str(bin)) in key.GetName(): continue
      hist = subdir.Get(key.GetName())
      canvas = subdir.Get(key.GetName())
      prims = canvas.GetListOfPrimitives()
      for iprim in xrange(prims.GetSize()):
        prim = prims.At(iprim)
        if not 'fit_eff' in prim.GetName(): continue
        return prim
  return None

combinations = [(False, False, False),
                (False, False, True),
                (True, False, False),
                (True, False, True),
                (False, True, False),
                (False, True, True),
    ]

for usePV, useJets, is2016 in combinations:
  if usePV:     ext  = '_PV'
  elif useJets: ext  = '_jets'
  else:         ext  = ''
  if is2016:    ext += '_2016'
  else:         ext += '_2017'

  outDir = 'tables' + ext
  try:    os.makedirs(outDir)
  except: pass

  year       = '2016' if is2016 else '2017'
  type       = 'pt_jets' if useJets else ('pt_vtx' if usePV else 'pt_eta')
  dir        = os.path.join(os.environ['CMSSW_BASE'], 'src', 'MuonAnalysis', 'TagAndProbe', 'test', 'fitting', 'efficiencies', year, type)

  data       = os.path.join(dir, 'data', 'nominal')
  altTag1    = os.path.join(dir, 'data', 'altTag1')
  altTag2    = os.path.join(dir, 'data', 'altTag2')
  altMass1   = os.path.join(dir, 'data', 'altMass1')
  altMass2   = os.path.join(dir, 'data', 'altMass2')
  altShape   = os.path.join(dir, 'data', 'altShape')
  mc         = os.path.join(dir, 'mc',   'nominal')
  altMC      = os.path.join(dir, 'mc',   'altMC')

  ptBins = [(10,20), (20,30), (30,40), (40,50), (50,100), (100,200), (200,500)]

  def fix(a, default):
    if a>10000:  return default
    if a<0.0001: return 0.0001
    try:         return float(a)
    except:      return default

  for f in os.listdir(data):
    fout = open(os.path.join(outDir, f.replace(".root",".txt").replace('None','Muon').replace('TnP_','')), "w")

    for ix, ptBin in enumerate(ptBins):
      hDat      = Histo(data     + '/' + f, ix)
      hAltTag1  = Histo(altTag1  + '/' + f, ix)
      hAltTag2  = Histo(altTag1  + '/' + f, ix)
      hAltMass1 = Histo(altMass1 + '/' + f, ix)
      hAltMass2 = Histo(altMass2 + '/' + f, ix)
      hAltShape = Histo(altShape + '/' + f, ix)
      hMC       = Histo(mc       + '/' + f, ix)
      hAltMC    = Histo(altMC    + '/' + f, ix)

      xlo, xhi = ptBin
      for iy in range(hDat.GetN()):
        ylo = hDat.GetX()[iy] - hDat.GetEXlow()[iy] 
        yhi = hDat.GetX()[iy] + hDat.GetEXhigh()[iy]

        dat    = fix(hDat.GetY()[iy], 0.)
        daterr = fix(max(hDat.GetEYlow()[iy],hDat.GetEYhigh()[iy]), 0.0001)
        mcval  = fix(hMC.GetY()[iy], 0.)
        mcerr  = fix(max(hMC.GetEYlow()[iy],hMC.GetEYhigh()[iy]), 0.0001)

        dat_altShape = hAltShape.GetY()[iy]
        if abs(dat-dat_altShape) > 0.1: dat_altShape = dat # For sure it is a failed fit when the difference is more than 0.1

        variations = (hAltMC.GetY()[iy], hAltTag1.GetY()[iy], hAltTag2.GetY()[iy], hAltMass1.GetY()[iy], hAltMass2.GetY()[iy], hAltShape.GetY()[iy], 1.)
        variations = tuple(fix(v, dat) for v in variations)

        line1 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % ((xlo, xhi, ylo,   yhi, dat, daterr, mcval, mcerr)+variations)
        line2 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % ((xlo, xhi, -yhi, -ylo, dat, daterr, mcval, mcerr)+variations)
        fout.write(line1+"\n")
        if 'jets' not in dir and 'vtx' not in dir:
          fout.write(line2+"\n")
    fout.close()
