#!/usr/bin/env python

import sys,os,time
from math import sqrt
import ROOT as rt
import CMS_lumi, tdrstyle
import numpy

from efficiencyUtils import efficiency
from efficiencyUtils import efficiencyList
import efficiencyUtils as effUtil


import argparse
argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument("--file",   action='store',      default=None,  help="which file?")
argParser.add_argument("--plot",   action='store',      default=0,     help="which plot?")
args = argParser.parse_args()

ext = args.file.split('/')[-2].strip('tables')

doAct   = ext.count('PV')
useJets = ext.count('jets') 

outputDirectory = 'output'+ext

try:    os.makedirs(outputDirectory)
except: pass

tdrstyle.setTDRStyle()

rt.gROOT.SetBatch(True)

CMS_lumi.lumi_13TeV = ("35.9 fb^{-1}" if ext.count('2016') else "41.4 fb^{-1}")
CMS_lumi.writeExtraText = 1
CMS_lumi.lumi_sqrtS = "13 TeV " + ("(2016)" if ext.count('2016') else "(2017)")


effiMin = 0.48
effiMax = 1.07

sfMin = 0.58
sfMax = 1.28

graphColors = [rt.kGray+3, rt.kRed +1, rt.kAzure+2, rt.kSpring-1, rt.kYellow -2 , rt.kOrange, rt.kViolet, rt.kCyan, rt.kBlack, rt.kBlue] 


def findMinMax(effis):
    mini = +999
    maxi = -999

    for key in effis.keys():
      for eff in effis[key]:
        mini = min(eff['val'] - eff['err'], mini)
        maxi = max(eff['val'] + eff['err'], maxi)

    if mini > 0.18 and mini < 0.28: mini = 0.18 # This is to avoid the label cutoff at the bottom of the y-axis
    if mini > 0.28 and mini < 0.38: mini = 0.28
    if mini > 0.38 and mini < 0.48: mini = 0.38
    if mini > 0.48 and mini < 0.58: mini = 0.48
    if mini > 0.58 and mini < 0.68: mini = 0.58
    if mini > 0.68 and mini < 0.78: mini = 0.68
    if mini > 0.78 and mini < 1.0:  mini = 0.78
        
    if   maxi > 0.95: maxi = 1.17        
    elif maxi < 0.87: maxi = 0.87
    else:             maxi = 1.07

    if maxi-mini > 0.5: maxi = maxi + 0.2
    if maxi-mini > 0.8: maxi = maxi + 0.2
        
    return (mini,maxi)

    
# This function makes the 1D efficiency plots
def EffiGraph1D(effDataList, sfList, etaPlot, nameout):
    W       = 800
    H       = 800
    yUp     = 0.45
    canName = ('totoNjets' if useJets else ('totoPV' if doAct else 'totoEta')) if etaPlot else 'totoPt'
    c       = rt.TCanvas(canName,canName,50,50,H,W)
    c.SetTopMargin(0.055)
    c.SetBottomMargin(0.10)
    c.SetLeftMargin(0.12)
    
    p1 = rt.TPad( canName + '_up', canName + '_up', 0, yUp, 1,   1, 0,0,0)
    p2 = rt.TPad( canName + '_do', canName + '_do', 0,   0, 1, yUp, 0,0,0)
    p1.SetBottomMargin(0.0075)
    p1.SetTopMargin(   c.GetTopMargin()*1/(1-yUp))
    p2.SetTopMargin(   0.0075)
    p2.SetBottomMargin(c.GetBottomMargin()*1/yUp)
    p1.SetLeftMargin(  c.GetLeftMargin() )
    p2.SetLeftMargin(  c.GetLeftMargin() )
    firstGraph = True
    leg = rt.TLegend(0.5,0.80,0.95 ,0.92)
    leg.SetFillColor(0)
    leg.SetBorderSize(0)

    listOfTGraph1 = []
    listOfTGraph2 = []
    if etaPlot:
      xMin = 0  if doAct else (-.5 if useJets else -2.50)
      xMax = 50 if doAct else (6.5 if useJets else +2.50)
      zMin = 10
      zMax = 200 #500
    else:
      xMin = 10
      xMax = 200 #500
      zMin = 0
      zMax = 50 if doAct else (6.5 if useJets else 2.6)
      p1.SetLogx()
      p2.SetLogx()

    # Clean up entries we don't need
    for list in [effDataList, sfList]:
      for key in list.keys():
        if zMax <= key[0] or zMin >= key[1]: del list[key] 
        else:                                list[key] = [x for x in list[key] if x['min'] < xMax and x['max'] > xMin]

    (effiMin, effiMax) = findMinMax(effDataList)

    for key in sorted(effDataList.keys()):
        grBinsEffData = effUtil.makeTGraphFromList(effDataList[key], 'min', 'max')
        grBinsSF      = effUtil.makeTGraphFromList(sfList[key]     , 'min', 'max')

        grBinsSF     .SetLineWidth(2)
        grBinsEffData.SetLineWidth(2) 

        grBinsSF.SetTitle("")
        grBinsEffData.SetTitle("")

        grBinsEffData.GetHistogram().GetXaxis().SetLimits(xMin,xMax)
        grBinsSF.GetHistogram()     .GetXaxis().SetLimits(xMin,xMax)

        grBinsSF.GetHistogram().GetXaxis().SetTitleOffset(1)
        grBinsSF.GetHistogram().GetXaxis().SetTitle(("nPV" if doAct else ("N_{jets}" if useJets else "SuperCluster #eta")) if etaPlot else "p_{T}  [GeV]")
            
        grBinsSF.GetHistogram().GetYaxis().SetTitle("Data / MC")
        grBinsSF.GetHistogram().GetYaxis().SetTitleOffset(1)
            
        grBinsEffData.GetHistogram().GetYaxis().SetTitleOffset(1)
        grBinsEffData.GetHistogram().GetYaxis().SetTitle("Data efficiency" )

        ### to avoid loosing the TGraph keep it in memory by adding it to a list
        listOfTGraph1.append( grBinsEffData )
        listOfTGraph2.append( grBinsSF ) 

        if etaPlot:   leg.AddEntry( grBinsEffData, '%3.0f #leq p_{T} #leq  %3.0f GeV'   % (key[0], key[1]), "PL")        
        elif doAct:   leg.AddEntry( grBinsEffData, '%3.0f #leq nPV #leq  %3.0f' % (key[0], key[1]), "PL")        
        elif useJets: leg.AddEntry( grBinsEffData, 'N_{jets} =  ' + ('%d' % (int(key[1])) if key[1] < 5  else '5,6'), "PL")        
        else:         leg.AddEntry( grBinsEffData, '%1.3f #leq | #eta | #leq  %1.3f' % (key[0], key[1]), "PL")        

        
    for i in range(len(listOfTGraph1)):
        listOfTGraph1[i].SetLineColor(graphColors[i])
        listOfTGraph1[i].SetMarkerColor(graphColors[i])

        listOfTGraph1[i].GetHistogram().SetMinimum(effiMin)
        listOfTGraph1[i].GetHistogram().SetMaximum(effiMax)
        p1.cd()
        listOfTGraph1[i].Draw("AP" if i==0 else "P")

        listOfTGraph2[i].SetLineColor(graphColors[i])
        listOfTGraph2[i].SetMarkerColor(graphColors[i])
        listOfTGraph2[i].GetHistogram().SetMinimum(sfMin)
        listOfTGraph2[i].GetHistogram().SetMaximum(sfMax)
        if not etaPlot: listOfTGraph2[i].GetHistogram().GetXaxis().SetMoreLogLabels()
        listOfTGraph2[i].GetHistogram().GetXaxis().SetNoExponent()
        p2.cd()        
        listOfTGraph2[i].Draw("AP" if i == 0 else "P")
        

    lineAtOne = rt.TLine(xMin,1,xMax,1)
    lineAtOne.SetLineStyle(rt.kDashed)
    lineAtOne.SetLineWidth(2)
    
    p2.cd()
    lineAtOne.Draw()

    c.cd()
    p2.Draw()
    p1.Draw()

    leg.Draw()    
    CMS_lumi.CMS_lumi(c, 4, 10)

    c.Print(nameout)




def diagnosticErrorPlot( effgr, ierror, nameout ):
    errorNames = efficiency.getSystematicNames()
    c2D_Err = rt.TCanvas('canScaleFactor_%s' % errorNames[ierror] ,'canScaleFactor: %s' % errorNames[ierror],1000,600)    
    c2D_Err.Divide(2,1)
    c2D_Err.GetPad(1).SetLogy()
    c2D_Err.GetPad(2).SetLogy()
    c2D_Err.GetPad(1).SetRightMargin(0.15)
    c2D_Err.GetPad(1).SetLeftMargin( 0.15)
    c2D_Err.GetPad(1).SetTopMargin(  0.10)
    c2D_Err.GetPad(2).SetRightMargin(0.15)
    c2D_Err.GetPad(2).SetLeftMargin( 0.15)
    c2D_Err.GetPad(2).SetTopMargin(  0.10)

    h2_sfErrorAbs = effgr.histo2D(ierror+1, False, switchEtaPt=True)
    h2_sfErrorRel = effgr.histo2D(ierror+1, True,  switchEtaPt=True)
    h2_sfErrorAbs.SetMinimum(0)
    h2_sfErrorAbs.SetMaximum(min(h2_sfErrorAbs.GetMaximum(),0.2))
    h2_sfErrorRel.SetMinimum(0)
    h2_sfErrorRel.SetMaximum(1)
    h2_sfErrorAbs.SetTitle('e/#gamma absolute SF syst: %s ' % errorNames[ierror])
    h2_sfErrorRel.SetTitle('e/#gamma relative SF syst: %s ' % errorNames[ierror])
    c2D_Err.cd(1)
    h2_sfErrorAbs.DrawCopy("colz TEXT45")
    c2D_Err.cd(2)
    h2_sfErrorRel.DrawCopy("colz TEXT45")
    
    c2D_Err.Print(nameout)


filein = args.file
if not os.path.exists( filein ) :
  print 'file %s does not exist' % filein
  sys.exit(1)
else: print " Opening file: ", filein

nameOutBase = "./"+ outputDirectory + "/" + filein.split('/')[-1] 
fileWithEff = open(filein, 'r')

effGraph = efficiencyList()

for line in fileWithEff:
    modifiedLine = line.lstrip(' ').rstrip(' ').rstrip('\n')
    numbers = [float(i) for i in modifiedLine.split('\t')]

    if len(numbers) > 0:
      etaKey = (numbers[0], numbers[1])
      ptKey  = (numbers[2], numbers[3])
      myeff = efficiency(ptKey,etaKey,numbers[4],numbers[5],numbers[6],numbers[7],numbers[8],numbers[9],numbers[10],numbers[11])
      effGraph.addEfficiency(myeff)


fileWithEff.close()

### massage the numbers a bit
effGraph.combineSyst()


print " ------------------------------- "

pdfout = nameOutBase + '_egammaPlots.pdf'
pdfout2 = nameOutBase + '_eff_vs_pt.pdf'
pdfout3 = nameOutBase + ('_eff_vs_pv.pdf' if doAct else ('_eff_vs_njets.pdf' if useJets else '_eff_vs_eta.pdf'))
cDummy = rt.TCanvas()
cDummy.Print( pdfout + "[" )

h2SF    = effGraph.histo2D(-1, switchEtaPt = False)
h2Error = effGraph.histo2D(0, switchEtaPt = False)  ## only error bars
rt.gStyle.SetPalette(1)
rt.gStyle.SetPaintTextFormat('1.3f');
rt.gStyle.SetOptTitle(1)

c2D = rt.TCanvas('canScaleFactor','canScaleFactor',900,600)
c2D.Divide(2,1)
c2D.GetPad(1).SetRightMargin(0.15)
c2D.GetPad(1).SetLeftMargin( 0.15)
c2D.GetPad(1).SetTopMargin(  0.10)
c2D.GetPad(2).SetRightMargin(0.15)
c2D.GetPad(2).SetLeftMargin( 0.15)
c2D.GetPad(2).SetTopMargin(  0.10)
c2D.GetPad(1).SetLogx()
c2D.GetPad(2).SetLogx()

c2D.cd(1)
dmin = 1.0 - h2SF.GetMinimum()
dmax = h2SF.GetMaximum() - 1.0
dall = max(dmin,dmax)
h2SF.SetMinimum(1-dall)
h2SF.SetMaximum(1+dall)
h2SF.DrawCopy("colz TEXT45")

c2D.cd(2)
h2Error.SetMinimum(0)
h2Error.SetMaximum(min(h2Error.GetMaximum(),0.2))

h2Error.DrawCopy("colz TEXT45")

c2D.Print( pdfout )

rootout = rt.TFile(os.path.join(outputDirectory, "scaleFactors.root"),"UPDATE") # adding it to the same file
h2SF.SetOption("colz TEXT45")
h2SF.SetStats(0)
h2SF.Write(nameOutBase.split('eff_all_')[-1].split('.txt')[0].split('_eta')[0] ,rt.TObject.kOverwrite)
rootout.Close()

canvas = rt.TCanvas('2DSF','2DSF', 1000, 700)
canvas.SetRightMargin(.1)
canvas.SetLogx()
h2SF.GetXaxis().SetMoreLogLabels()
h2SF.GetXaxis().SetNoExponent()
h2SF.SetTitle("")
h2SF.DrawCopy("colz TEXTE")
canvas.SaveAs(os.path.join(outputDirectory, nameOutBase.split('eff_all_')[-1].split('.txt')[0].split('_eta')[0] + ".pdf"))

for isyst in range(len(efficiency.getSystematicNames())):
    diagnosticErrorPlot( effGraph, isyst, pdfout )

if int(args.plot)==1: EffiGraph1D(effGraph.listOfGraphs(False, False) , effGraph.listOfGraphs(True, False) , False, pdfout2)
if int(args.plot)==2: EffiGraph1D(effGraph.listOfGraphs(False, True),   effGraph.listOfGraphs(True, True),   True,  pdfout3)

cDummy.Print( pdfout + "]" )
