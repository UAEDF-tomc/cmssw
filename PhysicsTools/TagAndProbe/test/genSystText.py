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
                if "probe_sc_abseta_probe_Ele_pt_PLOT" not in key.GetName(): continue
                canvas = subdir.Get(key.GetName())
                prims = canvas.GetListOfPrimitives()
                for iprim in xrange(prims.GetSize()):
                    prim = prims.At(iprim)
                    if "probe_sc_abseta_probe_Ele_pt_PLOT" not in prim.GetName(): continue
                    return prim
    return None


outDir = 'tables'
try:
  os.makedirs(outDir)
except:
  pass


tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')
nominal    = os.path.join(tnpPackage, 'test', 'efficiencies', 'nominal')
altSig0    = os.path.join(tnpPackage, 'test', 'efficiencies', 'altSig0')
altSig1    = os.path.join(tnpPackage, 'test', 'efficiencies', 'altSig1')
altSig2    = os.path.join(tnpPackage, 'test', 'efficiencies', 'altSig2')
altSig3    = os.path.join(tnpPackage, 'test', 'efficiencies', 'altSig3')
altBkg     = os.path.join(tnpPackage, 'test', 'efficiencies', 'altBkg')
altMC      = os.path.join(tnpPackage, 'test', 'efficiencies', 'altMC')
altTag     = os.path.join(tnpPackage, 'test', 'efficiencies', 'altTag')

flist = (f for f in os.listdir(nominal) if "_data_" in f and "_act.root" not in f)

for f in flist:
    if not f.count("eff_data"): continue
    print f.replace("eff_data_","").replace(".root","")
    fmc = f.replace("_data_","_mc_")

    fdat = ROOT.TFile(nominal+"/"+ f)
    fnmc = ROOT.TFile(nominal+"/"+ fmc)
    fsig = ROOT.TFile(altSig +"/"+ f)
    fsig2 = ROOT.TFile(altSig2 +"/"+ f)
    fsig3 = ROOT.TFile(altSig3 +"/"+ f)
    fsig4 = ROOT.TFile(altSig4 +"/"+ f)
    fbkg = ROOT.TFile(altBkg +"/"+ f)
    famc = ROOT.TFile(altMC  +"/"+ fmc)
    ftag = ROOT.TFile(altTag +"/"+ f)

    fout = open(os.path.join(outDir, f.replace("_data_","_all_").replace(".root",".txt")), "w")

    hdat  = Histo(fdat,  True)
    hnmc  = Histo(fnmc,  False)
    hsig0 = Histo(fsig0, True)
    hsig1 = Histo(fsig1, True)
    hsig2 = Histo(fsig2, True)
    hsig3 = Histo(fsig3, True)
    hbkg  = Histo(fbkg,  True)
    hamc  = Histo(famc,  False)
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

            if(abs(sig-dat) > abs(sig1-dat)): sig = sig1  # To be sure we do not take failed fits, we check some slightly alternative fits too
            if(abs(sig-dat) > abs(sig2-dat)): sig = sig2
            if(abs(sig-dat) > abs(sig3-dat)): sig = sig3

            line1 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % (xlo, xhi, ylo, yhi, hdat.GetBinContent(ix,iy), daterr, hnmc.GetBinContent(ix,iy), hnmc.GetBinError(ix,iy), hbkg.GetBinContent(ix,iy), sig, hamc.GetBinContent(ix,iy), htag.GetBinContent(ix,iy), 1., 1., 1.)
            line2 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % (-xhi, -xlo, ylo, yhi, hdat.GetBinContent(ix,iy), daterr, hnmc.GetBinContent(ix,iy), hnmc.GetBinError(ix,iy), hbkg.GetBinContent(ix,iy), sig, hamc.GetBinContent(ix,iy), htag.GetBinContent(ix,iy), 1., 1., 1.)
            print line1
            print line2
            fout.write(line1+"\n")
            fout.write(line2+"\n")
    fout.close()
