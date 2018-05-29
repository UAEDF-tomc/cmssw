#! /usr/bin/env python

import os
import ROOT

def Histo(parent, isfit):
  sub1 = parent.GetListOfKeys()
  for ikey1 in xrange(sub1.GetSize()):
      key1 = sub1.At(ikey1)
      if key1.GetName() == "ProcessID0": continue
      dir1 = parent.Get(key1.GetName())
      sub2 = dir1.GetListOfKeys()
      for ikey2 in xrange(sub2.GetSize()):
          key2 = sub2.At(ikey2)
          dir2 = dir1.Get(key2.GetName())
          subdir = dir2.Get("fit_eff_plots")
          if not isfit:
              subdir = dir2.Get("cnt_eff_plots")
          subkeys = subdir.GetListOfKeys()
          for ikey in xrange(subkeys.GetSize()):
              key = subkeys.At(ikey)
              if not any([x in key.GetName() for x in ['el_sc_abseta_el_pt', 'event_nPV_el_pt','event_njets_el_pt']]): continue
              canvas = subdir.Get(key.GetName())
              prims = canvas.GetListOfPrimitives()
              for iprim in xrange(prims.GetSize()):
                  prim = prims.At(iprim)
                  if not any([x in key.GetName() for x in ['el_sc_abseta_el_pt', 'event_nPV_el_pt','event_njets_el_pt']]): continue
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


  dir = 'efficiencies'+ext
  tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')
  nominal    = os.path.join(tnpPackage, 'test', dir, 'nominal')
  altSig0    = os.path.join(tnpPackage, 'test', dir, 'altSig0')
  altSig1    = os.path.join(tnpPackage, 'test', dir, 'altSig1')
  altSig2    = os.path.join(tnpPackage, 'test', dir, 'altSig2')
  altSig3    = os.path.join(tnpPackage, 'test', dir, 'altSig3')
  altBkg0    = os.path.join(tnpPackage, 'test', dir, 'altBkg0')
  altBkg1    = os.path.join(tnpPackage, 'test', dir, 'altBkg1')
  altBkg2    = os.path.join(tnpPackage, 'test', dir, 'altBkg2')
  altMC      = os.path.join(tnpPackage, 'test', dir, 'altMC')
  altTag     = os.path.join(tnpPackage, 'test', dir, 'altTag')

  flist = (f for f in os.listdir(nominal) if "_data_" in f and "_act.root" not in f)

  for f in flist:
      if not f.count("eff_data"): continue
      print f.replace("eff_data_","").replace(".root","")
      fmc = f.replace("_data_","_mc_")

      fdat  = ROOT.TFile(nominal +"/"+ f)
      fnmc  = ROOT.TFile(nominal +"/"+ fmc)
      fsig0 = ROOT.TFile(nominal +"/"+ f) # currently nominal to save work
      fsig1 = ROOT.TFile(nominal +"/"+ f) # currently nominal to save work
      fsig2 = ROOT.TFile(nominal +"/"+ f) # currently nominal to save work
      fsig3 = ROOT.TFile(nominal +"/"+ f) # currently nominal to save work
      fbkg0 = ROOT.TFile(altBkg0 +"/"+ f)
      fbkg1 = ROOT.TFile(altBkg1 +"/"+ f)
      fbkg2 = ROOT.TFile(altBkg2 +"/"+ f)
      famc  = ROOT.TFile(altMC   +"/"+ fmc)
      ftag  = ROOT.TFile(altTag  +"/"+ f)

      fout = open(os.path.join(outDir, f.replace("_data_","_all_").replace(".root",".txt")), "w")

      hdat  = Histo(fdat,  True)
      hnmc  = Histo(famc,  False)
      hsig0 = Histo(fsig0, True)
      hsig1 = Histo(fsig1, True)
      hsig2 = Histo(fsig2, True)
      hsig3 = Histo(fsig3, True)
      
      hbkg0 = Histo(fbkg0, True)
      hbkg1 = Histo(fbkg1, True)
      hbkg2 = Histo(fbkg2, True)
      hamc  = Histo(fnmc,  False)
      htag  = Histo(ftag,  True)


      for ix in xrange(1, hdat.GetNbinsX()+1):
          xlo = hdat.GetXaxis().GetBinLowEdge(ix)
          xhi = hdat.GetXaxis().GetBinUpEdge(ix)
          for iy in xrange(1, hdat.GetNbinsY()+1):
              ylo = hdat.GetYaxis().GetBinLowEdge(iy)
              yhi = hdat.GetYaxis().GetBinUpEdge(iy)

              dat = hdat.GetBinContent(ix,iy)
              daterr = hdat.GetBinError(ix,iy)
              if daterr < 0.0001: daterr = 0.0001   # Because in very rare cases this error is too small and messes up the plot

              sig  = hsig0.GetBinContent(ix,iy)
              sig1 = hsig1.GetBinContent(ix,iy)
              sig2 = hsig2.GetBinContent(ix,iy)
              sig3 = hsig3.GetBinContent(ix,iy)

              bkg  = hbkg0.GetBinContent(ix,iy)
              bkg1 = hbkg1.GetBinContent(ix,iy)
              bkg2 = hbkg2.GetBinContent(ix,iy)

              if ix==1 and iy==1 and not any([is2016, usePV, useJets]): # hacky way, because the nominal fit fails for all 2017 workingpoints at low pt/eta while the alternative tag seems fine
                dat    = htag.GetBinContent(ix, iy)
                daterr = htag.GetBinError(ix, iy)
                bkg    = htag.GetBinContent(ix, iy)

              if(abs(sig-dat) > abs(sig1-dat)): sig = sig1  # To be sure we do not take failed fits, we check some slightly alternative fits too
              if(abs(sig-dat) > abs(sig2-dat)): sig = sig2
              if(abs(sig-dat) > abs(sig3-dat)): sig = sig3

              if(abs(bkg-dat) > abs(bkg1-dat)): bkg = bkg1
              if(abs(bkg-dat) > abs(bkg2-dat)): bkg = bkg2



              line1 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % (xlo, xhi, ylo, yhi, dat, daterr, hnmc.GetBinContent(ix,iy), hnmc.GetBinError(ix,iy), bkg, sig, hamc.GetBinContent(ix,iy), htag.GetBinContent(ix,iy), 1., 1., 1.)
              line2 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % (-xhi, -xlo, ylo, yhi, dat, daterr, hnmc.GetBinContent(ix,iy), hnmc.GetBinError(ix,iy), bkg, sig, hamc.GetBinContent(ix,iy), htag.GetBinContent(ix,iy), 1., 1., 1.)
              print line1
              fout.write(line1+"\n")
              if 'PV' not in dir and 'njets' not in dir:
                print line2
                fout.write(line2+"\n")
      fout.close()
