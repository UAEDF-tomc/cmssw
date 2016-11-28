#!/usr/bin/env python
import ROOT
from optparse import OptionParser
import sys, os, glob

def makeTable(h, tablefilename):
    nX = h.GetNbinsX()
    nY = h.GetNbinsY()
  
    print "Writing...", tablefilename
    f = open(os.path.join(options.output, tablefilename), "w+")

    for i in xrange(1, nX+1):
    
        pT0 = h.GetXaxis().GetBinLowEdge(i)
        pT1 = h.GetXaxis().GetBinLowEdge(i+1)
    
        for j in xrange(1, nY+1):
            x    = h.GetBinContent(i,j)
            dx   = h.GetBinError(i,j)
            eta0 = h.GetYaxis().GetBinLowEdge(j)
            eta1 = h.GetYaxis().GetBinLowEdge(j+1)
      
            f.write("%4.2f  %4.2f   %+6.4f   %+6.4f  %6.4f   %6.4f \n" %(pT0, pT1, eta0, eta1, x, dx))
  
    f.close()


def main(options):
    ROOT.gStyle.SetPaintTextFormat("1.4f")
    print "##################################################   "
    print "Opening file: " + options.input
    f      = ROOT.TFile(options.input)
    topDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
    f.cd(ROOT.gDirectory.GetListOfKeys()[0].GetName())
    subDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
    f.cd(os.path.join(topDir, subDir))
    
    keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]

    # EFFICIENCY PLOTS + TABLE
    dirName = "cnt_eff_plots"
    if not options.cc:
        dirName = "fit_eff_plots"
    ROOT.gDirectory.cd(dirName)

    keyList2 = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
    tableDone = False

    for k in  keyList2:
        obj = ROOT.gDirectory.GetKey(k).ReadObj();
        innername = obj.GetName()
        if (obj.ClassName() == "TCanvas"):
            for p in obj.GetListOfPrimitives():
                if (p.ClassName() == "TH2F" and not tableDone):
                    obj.SetLogx()
                    makeTable(p, subDir +".txt")
                    tableDone = True
            obj.Draw()
            innername = innername.replace("&", "")            
            plotname = os.path.join(options.output, innername + ".png")
            obj.SaveAs(plotname)

    if not options.cc:
        ROOT.gDirectory.cd("../")
        keyList = [key.GetName() for key in ROOT.gDirectory.GetListOfKeys()]
        for k in  keyList:
            obj = ROOT.gDirectory.GetKey(k).ReadObj();
            innername = obj.GetName()
            if (not obj.IsA().InheritsFrom("TDirectory") or not "_bin" in innername):
                continue
            ROOT.gDirectory.cd(innername)
            c = ROOT.gDirectory.Get("fit_canvas")
            c.Draw()
            plotname = os.path.join(options.output, "fit_" + subDir + "_" + innername + ".png")
            #plotname = plotname.replace("probe_sc_", "")
            plotname = plotname.replace("&", "")
            plotname = plotname.replace("__pdfSignalPlusBackground", "")
            c.SaveAs(plotname)
            ROOT.gDirectory.cd("../")

if (__name__ == "__main__"):
    tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')

    parser = OptionParser()
    (options, arg) = parser.parse_args()

    try:    os.makedirs('fits')
    except: pass

    for directory in os.listdir(os.path.join(tnpPackage, "test", "efficiencies")):
      for file in glob.glob(os.path.join(tnpPackage, "test", "efficiencies", directory, "eff*.root")):
	options.input  = file
	options.output = os.path.join('fits', directory, file.split('.root')[0].split('/')[-1])
	options.cc     = options.output.count("eff_mc") and not directory.count('altSig')

	try:    os.makedirs(options.output)
	except: pass

	ROOT.gROOT.SetBatch(True)
	main(options)
