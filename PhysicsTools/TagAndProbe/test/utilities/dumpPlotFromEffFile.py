#!/usr/bin/env python
import ROOT
from optparse import OptionParser
import sys, os, glob

tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')


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

def getParam(name, params):
    mid = params.at(params.index(name)).getVal()
    err = params.at(params.index(name)).getError()
    min = params.at(params.index(name)).getMin()
    max = params.at(params.index(name)).getMax()
    return (mid, err, min, max) 

def main(options, failedFitsNominal, failedFitsAltTag, failedFitsAltSig):
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

    if False:
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
            try:    obj = ROOT.gDirectory.GetKey(k).ReadObj();
            except: continue
            innername = obj.GetName()
            if (not obj.IsA().InheritsFrom("TDirectory") or not "_bin" in innername):
                continue
            ROOT.gDirectory.cd(innername)
            c = ROOT.gDirectory.Get("fit_canvas")
            try:    c.Draw()
            except: continue
            plotname = os.path.join(options.output, innername.replace(options.wp, '') + ".png")
            plotname = plotname.replace("&", "")
            plotname = plotname.replace("__pdfSignalPlusBackground", "")
            plotname = plotname.replace("_and_mcTrue_true", "")
            plotname = plotname.replace("_mcTrue_true", "")
            plotname = plotname.replace("__", "_")
            plotname = plotname.replace("__", "_")
            c.SaveAs(plotname)

            for (name, list) in [('nominal', failedFitsNominal), ('altSig0', failedFitsAltSig), ('altTag', failedFitsAltTag)]:
              if options.input.count(name):
                fitResults = ROOT.gDirectory.Get("fitresults").floatParsFinal()
                init       = ROOT.gDirectory.Get("fitresults").floatParsInit()
                for param in ['alphaPass','alphaFail','betaPass','betaFail','gammaPass','gammaFail','meanP','meanF']:
                  (mid, err, min, max)  = getParam(param, fitResults)
                  (i, erri, mini, maxi) = getParam(param, init)
                  if err < 0.00001 and (abs(mid-max) < err or abs(mid-min) < err):
                    failedFit = k.split('__')[-1]
                    print failedFit, ' has probably a failed fit, adding to list'
                    list.append(failedFit)
            ROOT.gDirectory.cd("../")


def writeFailedFits(baseName, failedFits):
    failedFits = [f for f in failedFits if failedFits.count(f) > 1]
    outFile = os.path.join(tnpPackage, 'python', baseName + '1.py')
    iteration = 1
    while os.path.isfile(outFile):
      iteration += 1
      outFile = os.path.join(tnpPackage, 'python', baseName + str(iteration) + '.py')
    with open(outFile, 'w') as f:
      f.write(baseName + str(iteration) + ' = [\n') 
      for failedFit in set(failedFits):
        f.write('       "' + failedFit + '",\n')
      f.write('       ]')

if (__name__ == "__main__"):
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--list', action='store_true', default=False, help='List failed fits')
    options = argParser.parse_args()

    failedFitsNominal = []
    failedFitsAltTag = []
    failedFitsAltSig = []
    #for masterdir in ['efficiencies_2016', 'efficiencies_2017', 'efficiencies_jets_2016', 'efficiencies_jets_2017', 'efficiencies_PV_2016', 'efficiencies_PV_2017']:
    for masterdir in ['efficiencies_2017']:
      for directory in os.listdir(os.path.join(tnpPackage, "test", masterdir)):
        for file in glob.glob(os.path.join(tnpPackage, "test", masterdir, directory, "eff*.root")):
          options.input  = file
          options.output = os.path.join('fits'+masterdir.replace('efficiencies',''), directory, file.split('.root')[0].split('/')[-1])
          options.wp     = file.split('.root')[0].split('_')[-1]
          options.cc     = options.output.count("eff_mc") and not directory.count('altSig')
          try:    os.makedirs(options.output)
          except: pass

          ROOT.gROOT.SetBatch(True)
          main(options, failedFitsNominal, failedFitsAltTag, failedFitsAltSig)

    if options.list: 
      writeFailedFits('failedFitsNominal', failedFitsNominal)
      writeFailedFits('failedFitsAltSig',  failedFitsAltSig)
      writeFailedFits('failedFitsAltTag',  failedFitsAltTag)
