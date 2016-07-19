#!/usr/bin/env python
import ROOT, os, glob
import math, numpy
from optparse import OptionParser

def makeTable(hnum, hden, tablefilename):
    nX = hnum.GetNbinsX()
    nY = hnum.GetNbinsY()
  
    f = open(tablefilename, "w+")
  
    for i in xrange(1, nX+1):
        pT0 = hnum.GetXaxis().GetBinLowEdge(i)
        pT1 = hnum.GetXaxis().GetBinLowEdge(i+1)
    
        for j in xrange(1, nY+1):
            x = hnum.GetBinContent(i,j)/hden.GetBinContent(i,j)
            dx1 = hnum.GetBinError(i,j)/hnum.GetBinContent(i,j)
            dx2 = hden.GetBinError(i,j)/hden.GetBinContent(i,j)
            dx = math.sqrt(dx1*dx1+dx2*dx2)*x
            print hnum.GetBinError(i,j), hnum.GetBinContent(i,j)
            print dx1, dx2, dx
            eta0 = hnum.GetYaxis().GetBinLowEdge(j)
            eta1 = hnum.GetYaxis().GetBinLowEdge(j+1)
            
            f.write("%4.1f  %4.1f   %+6.4f   %+6.4f  %6.4f   %6.4f \n"%(pT0, pT1, eta0, eta1, x, dx))
            
    f.close()

def main(options, outRootFile, outDir):
    hData = ""
    hMC = ""

    print "##################################################   "
    print "Opening files: " + options.data + " and " + options.mc
    fData  = ROOT.TFile(options.data)
    topDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
    fData.cd(ROOT.gDirectory.GetListOfKeys()[0].GetName())
    subDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
    fData.cd(os.path.join(topDir, subDir, "fit_eff_plots"))
    name = subDir

    outFile = os.path.join(outDir, "ScaleFactor_%s_%s.txt"%(topDir, subDir))

    theCanvas = None
    keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
    for k in  keyList:
        obj = ROOT.gDirectory.GetKey(k).ReadObj();
        innername = obj.GetName()
        if (obj.ClassName() == "TCanvas"):
            for p in obj.GetListOfPrimitives():
                if (p.ClassName() == "TH2F" and p.GetName().count("probe_Ele_pt_probe_sc_abseta_PLOT")):
                    theCanvas = obj
                    hData = p

    fMC    = ROOT.TFile(options.mc)
    topDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
    fMC.cd(ROOT.gDirectory.GetListOfKeys()[0].GetName())
    subDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
    fMC.cd(os.path.join(topDir, subDir, "cnt_eff_plots"))

    keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
    for k in  keyList:
        obj = ROOT.gDirectory.GetKey(k).ReadObj();
        innername = obj.GetName()
        if (obj.ClassName() == "TCanvas"):
            for p in obj.GetListOfPrimitives():
                if (p.ClassName() == "TH2F" and p.GetName().count("probe_Ele_pt_probe_sc_abseta_PLOT")):
                    hMC = p

    makeTable(hData, hMC, outFile)
    
    hData.Divide(hMC)
    hData.SetContour(13, numpy.array([0,0.5,0.75,0.85,0.9,0.95,1,1.05,1.10,1.15,1.25,1.50,2]))
    hData.GetZaxis().SetRangeUser(0,2)
    theCanvas.SetLogx()
    theCanvas.Draw()
    theCanvas.SaveAs(outFile.replace(".txt",".png"))     

    fData.Close()
    fMC.Close()

    if name == "Tight":         name = "CutBasedTight"
    if name == "Medium":        name = "CutBasedMedium"
    if name == "Loose":         name = "CutBasedLoose"
    if name == "Veto":          name = "CutBasedVeto"
    if name == "LeptonMvaVT":   name = "LeptonMvaVeryTight"
    if name == "LeptonMvaM":    name = "LeptonMvaMedium"


    outRootFile.cd()
    hData.GetZaxis().SetTitle("")
    hData.Write(name)

if (__name__ == "__main__"):
    tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')

    parser = OptionParser()
    parser.add_option("-d", "--directory", default="nominal", help="Directory with eff*.root files")
    (options, arg) = parser.parse_args()

    outDir = os.path.join(tnpPackage, 'test', 'utilities', options.directory)
    try:
      os.makedirs(outDir)
    except:
      pass
    outRootFile  = ROOT.TFile(os.path.join(outDir, "scaleFactors.root"),"RECREATE")

    for file in glob.glob(os.path.join(tnpPackage, "test", options.directory, "eff_data*.root"):
      options.data   = file
      options.mc     = file.replace('data','mc')

      ROOT.gROOT.SetBatch(True)
      main(options, outRootFile, outDir)
    outRootFile.Close()
