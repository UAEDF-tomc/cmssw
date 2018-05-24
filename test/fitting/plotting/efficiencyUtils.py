#!/usr/bin/python 

import math
from array import array

class efficiency:
    #    altEff = [-1]*7
    iAltMC       = 0 
    iAltTag1     = 1
    iAltTag2     = 2
    iAltMass1    = 3
    iAltMass2    = 4
    iAltShape    = 5
    
    def __init__(self,ptBin,etaBin,effData,errEffData,effMC,errEffMC, *variations):
        self.ptBin      = ptBin
        self.etaBin     = etaBin
        self.effData    = effData
        self.effMC      = effMC
        self.errEffData = errEffData        
        self.errEffMC   = errEffMC
        self.altEff     = [-1]*6
        self.syst       = [-1]*8

        try:    float(effMC)
        except: self.effMC = variations[0] 

        for i, eff in enumerate(variations):
          try:      float(eff)
          except:   eff = self.effData
          try:      self.altEff[i] = eff
          except:   pass

        print self

    def __str__(self):
        return '%2.3f\t%2.3f\t%2.1f\t%2.1f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%s' % (self.etaBin[0],self.etaBin[1], self.ptBin[0] ,self.ptBin[1] ,
                                                                               self.effData, self.errEffData, self.effMC, self.errEffMC, str(self.altEff))

    @staticmethod
    def getSystematicNames():
        return [ 'statData', 'statMC', 'altMC', 'altTag1', 'altTag2', 'altMass1', 'altMass2', 'altShape' ]



    def combineSyst(self):
        systAltTag1      = self.altEff[self.iAltTag1] - self.effData
        systAltTag2      = self.altEff[self.iAltTag2] - self.effData
        systAltMass1     = self.altEff[self.iAltMass1] - self.effData
        systAltMass2     = self.altEff[self.iAltMass2] - self.effData
        systAltShape     = self.altEff[self.iAltShape] - self.effData
        systAltMC        = self.altEff[self.iAltMC] - self.effMC

        self.syst = [self.errEffData, self.errEffMC, systAltMC, systAltTag1, systAltTag2, systAltMass1, systAltMass2, systAltShape]
        self.systCombined = 0
        for isyst in range(len(self.syst)):
            self.systCombined += self.syst[isyst]*self.syst[isyst];

        self.systCombined = math.sqrt(self.systCombined)

    def __add__(self,eff):
        if self.effData < 0: return eff.deepcopy()
        if eff.effData < 0:  return self.deepcopy()
        
        ptbin         = self.ptBin
        etabin        = self.etaBin
        errData2      = 1.0 / (1.0/(self.errEffData*self.errEffData)+1.0/(eff.errEffData*eff.errEffData)) if eff.errEffData !=0 and self.errEffData != 0 else 0
        wData1        = 1.0 / (self.errEffData * self.errEffData) * errData2 if self.errEffData !=0 else 0
        wData2        = 1.0 / (eff .errEffData * eff .errEffData) * errData2 if eff.errEffData !=0 else 0
        newEffData    = wData1 * self.effData + wData2 * eff.effData;
        newErrEffData = math.sqrt(errData2)
        
        #        errMC2 = 1.0 / (1.0/(self.errEffMC*self.errEffMC)+1.0/(eff.errEffMC*eff.errEffMC))
        #wMC1   = 1.0 / (self.errEffMC * self.errEffMC) * errMC2
        #wMC2   = 1.0 / (eff .errEffMC * eff .errEffMC) * errMC2
        newEffMC      = wData1 * self.effMC + wData2 * eff.effMC;
        newErrEffMC   = 0.00001#math.sqrt(errMC2)

        variations = [(wData1*eff + wData2*eff.altEff[i]) for i, eff in self.altEff]

        return efficiency(ptbin,etabin,newEffData,newErrEffData,newEffMC,newErrEffMC,*variations)


import ROOT as rt
import numpy as np

def makeTGraphFromList(listOfEfficiencies, keyMin, keyMax):
    grOut = rt.TGraphErrors(len(listOfEfficiencies))

    ip = 0
    for point in listOfEfficiencies:
        grOut.SetPoint(     ip, (point[keyMin]+point[keyMax])/2. , point['val'] )
        grOut.SetPointError(ip, (point[keyMax]-point[keyMin])/2. , point['err'] )
        ip = ip + 1

    return grOut



class efficiencyList: 
    effList = {}

    def __init__(self):
        self.effList = {}

    
    def __str__(self):
        outStr = ''
        for ptBin in self.effList.keys():
            for etaBin in self.effList[ptBin].keys():
                outStr += str(self.effList[ptBin][etaBin])
                outStr += '\n'
        return outStr

    
    def addEfficiency( self, eff ):
        if not self.effList.has_key(eff.ptBin):
            self.effList[eff.ptBin] = {}
        self.effList[eff.ptBin][eff.etaBin] = eff

    def combineSyst(self):
        for ptBin in self.effList.keys():
          for etaBin in self.effList[ptBin].keys():
            self.effList[ptBin][etaBin].combineSyst()

                                
    def histo2D(self, onlyError = -1, relError = False, switchEtaPt = False):
        ### first define bining
        xbins = []
        ybins = []
        for ptBin in self.effList.keys():
          if ptBin[1] > 200: continue
          if not ptBin[0] in xbins: xbins.append(ptBin[0])
          if not ptBin[1] in xbins: xbins.append(ptBin[1])

          for etaBin in self.effList[ptBin].keys():
            if not etaBin[0] in ybins: ybins.append(etaBin[0])
            if not etaBin[1] in ybins: ybins.append(etaBin[1])

        xbins.sort()
        ybins.sort()

        if switchEtaPt:
          xbins, ybins = ybins, xbins

        ## transform to numpy array for ROOT
        xbinsTab = np.array(xbins)
        ybinsTab = np.array(ybins)
        htitle = 'muon scale factors'
        hname  = 'h2_scaleFactors'

        if onlyError >= 0:
          htitle = 'uncertainties'
          hname  = 'h2_uncertainties'

        h2 = rt.TH2F(hname, htitle, len(xbins)-1, xbinsTab, len(ybins)-1, ybinsTab)

        for ptBin in self.effList.keys():
          if ptBin[1] > 200: continue
          for etaBin in self.effList[ptBin].keys():
            ptCenter  = (ptBin[0]+ptBin[1])/2.
            etaCenter = (etaBin[0]+etaBin[1])/2.
            bin       = h2.FindBin(etaCenter if switchEtaPt else ptCenter, ptCenter if switchEtaPt else etaCenter)

            eff = self.effList[ptBin][etaBin]
            if eff.effMC == 0 or eff.effData == 0: continue

            h2.SetBinContent(bin, eff.effData/eff.effMC)
            h2.SetBinError  (bin, eff.systCombined/eff.effMC)
            if onlyError == 0:  
              h2.SetBinContent(bin, eff.systCombined/eff.effMC)
            elif onlyError >= 1 and onlyError <= 8:
              denominator = eff.systCombined if relError else eff.effMC
              h2.SetBinContent(bin, abs(eff.syst[onlyError-1])/denominator)

        if not switchEtaPt: h2.GetYaxis().SetRangeUser(0,2.5) # Only show abseta
        h2.GetYaxis().SetTitle("p_{T} [GeV]" if switchEtaPt else "|#eta|")
        h2.GetXaxis().SetTitle("#eta" if switchEtaPt else "p_{T} [GeV]")
        return h2
        
                                
    def listOfGraphs(self, doScaleFactor, doEta = False):
        listOfGraphs = {}

        for ptBin in self.effList.keys():
          for etaBin in self.effList[ptBin].keys():
            groupKey = ptBin if doEta else etaBin
            eff = self.effList[ptBin][etaBin]
            if not listOfGraphs.has_key(groupKey): listOfGraphs[groupKey] = []

            value = eff.effData
            error = eff.systCombined 
            if doScaleFactor :
                value = eff.effData      / eff.effMC if eff.effMC != 0 else 0
                error = eff.systCombined / eff.effMC if eff.effMC != 0 else 0
            listOfGraphs[groupKey].append({'min': etaBin[0] if doEta else ptBin[0], 'max': etaBin[1] if doEta else ptBin[1], 'val': value, 'err': error}) 
        return listOfGraphs
