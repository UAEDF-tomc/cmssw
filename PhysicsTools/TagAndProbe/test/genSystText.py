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


tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')
nominal    = os.path.join(tnpPackage, 'test', 'nominal')
altSig     = os.path.join(tnpPackage, 'test', 'alternativeSignalShape')
altBkg     = os.path.join(tnpPackage, 'test', 'alternativeBackShape')
altMC      = os.path.join(tnpPackage, 'test', 'alternativeMC')
altTag     = os.path.join(tnpPackage, 'test', 'alternativeTag')

flist = (f for f in os.listdir(nominal) if f in os.listdir(altSig) and f in os.listdir(altBkg) and f.replace("_data_", "_mc_") in os.listdir(altMC) and f in os.listdir(altTag) and "_data_" in f and "_act.root" not in f)

for f in flist:
    if not f.count("eff_data"): continue
    print f.replace("eff_data_","").replace(".root","")
    fmc = f.replace("_data_","_mc_")

    fdat = ROOT.TFile(nominal+"/"+ f)
    fnmc = ROOT.TFile(nominal+"/"+ fmc)
    fsig = ROOT.TFile(altSig +"/"+ f)
    fbkg = ROOT.TFile(altBkg +"/"+ f)
    famc = ROOT.TFile(altMC  +"/"+ fmc)
    ftag = ROOT.TFile(altTag +"/"+ f)

    fout = open(f.replace("_data_","_all_").replace(".root",".txt"), "w")

    hdat = Histo(fdat, True)
    hnmc = Histo(fnmc, False)
    hsig = Histo(fsig, True)
    hbkg = Histo(fbkg, True)
    hamc = Histo(famc, False)
    htag = Histo(ftag, True)

    for ix in xrange(1, hdat.GetNbinsX()+1):
        xlo = hdat.GetXaxis().GetBinLowEdge(ix)
        xhi = hdat.GetXaxis().GetBinUpEdge(ix)
        for iy in xrange(1, hdat.GetNbinsY()+1):
            ylo = hdat.GetYaxis().GetBinLowEdge(iy)
            yhi = hdat.GetYaxis().GetBinUpEdge(iy)
            line1 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % (xlo, xhi, ylo, yhi, hdat.GetBinContent(ix,iy), hdat.GetBinError(ix,iy), hnmc.GetBinContent(ix,iy), hnmc.GetBinError(ix,iy), hbkg.GetBinContent(ix,iy), hsig.GetBinContent(ix,iy), hamc.GetBinContent(ix,iy), htag.GetBinContent(ix,iy), 1., 1., 1.)
            line2 = "%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f\t%8.4f" % (-xhi, -xlo, ylo, yhi, hdat.GetBinContent(ix,iy), hdat.GetBinError(ix,iy), hnmc.GetBinContent(ix,iy), hnmc.GetBinError(ix,iy), hbkg.GetBinContent(ix,iy), hsig.GetBinContent(ix,iy), hamc.GetBinContent(ix,iy), htag.GetBinContent(ix,iy), 1., 1., 1.)
            print line1
            print line2
            fout.write(line1+"\n")
            fout.write(line2+"\n")
    fout.close()
