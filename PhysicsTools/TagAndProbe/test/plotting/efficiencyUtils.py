#!/usr/bin/python 

import math
from array import array

class efficiency:
    #    altEff = [-1]*7
    iAltBkgModel = 0
    iAltSigModel = 1
    iAltMCSignal = 2
    iAltTagSelec = 3
    iPUup        = 4
    iPUdown      = 5
    iAltFitRange = 6
    
    def __init__(self,ptBin,etaBin,effData,errEffData,effMC,errEffMC,effAltBkgModel,effAltSigModel,effAltMCSignal,effAltTagSel):
        self.ptBin      = ptBin
        self.etaBin     = etaBin
        self.effData    = effData
        self.effMC      = effMC
        self.errEffData = errEffData        
        self.errEffMC   = errEffMC
        self.altEff = [-1]*7
        self.syst   = [-1]*9
        self.altEff[self.iAltBkgModel] = effAltBkgModel
        self.altEff[self.iAltSigModel] = effAltSigModel
        self.altEff[self.iAltMCSignal] = effAltMCSignal
        self.altEff[self.iAltTagSelec] = effAltTagSel

    def __str__(self):
        return '%2.3f\t%2.3f\t%2.1f\t%2.1f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f' % (self.etaBin[0],self.etaBin[1],
                                                                                                       self.ptBin[0] ,self.ptBin[1] ,
                                                                                                       self.effData, self.errEffData, self.effMC, self.errEffMC,
                                                                                                       self.altEff[0],self.altEff[1], self.altEff[2], self.altEff[3] )

    @staticmethod
    def getSystematicNames():
        return [ 'statData', 'statMC', 'altBkgModel', 'altSignalModel', 'altMCEff', 'altTagSelection' ]



    def combineSyst(self):
        systAltBkg      = self.altEff[self.iAltBkgModel] - self.effData
        systAltSig      = self.altEff[self.iAltSigModel] - self.effData
        systAltMC       = self.altEff[self.iAltMCSignal] - self.effMC
        systAltTagSelec = self.altEff[self.iAltTagSelec] - self.effData

        if self.altEff[self.iAltBkgModel] < 0: systAltBkg      = 0
        if self.altEff[self.iAltSigModel] < 0: systAltSig      = 0
        if self.altEff[self.iAltMCSignal] < 0: systAltMC       = 0
        if self.altEff[self.iAltTagSelec] < 0: systAltTagSelec = 0

        self.syst[ 0                 ] = self.errEffData
        self.syst[ 1                 ] = self.errEffMC
        self.syst[self.iAltBkgModel+2] = systAltBkg
        self.syst[self.iAltSigModel+2] = systAltSig
        self.syst[self.iAltMCSignal+2] = systAltMC
        self.syst[self.iAltTagSelec+2] = systAltTagSelec
        
        self.systCombined = 0
        for isyst in range(6):
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

        newEffAltBkgModel = wData1 * self.altEff[self.iAltBkgModel] + wData2 * eff.altEff[self.iAltBkgModel]
        newEffAltSigModel = wData1 * self.altEff[self.iAltSigModel] + wData2 * eff.altEff[self.iAltSigModel]
        newEffAltMCSignal = wData1 * self.altEff[self.iAltMCSignal] + wData2 * eff.altEff[self.iAltMCSignal]
        newEffAltTagSelec = wData1 * self.altEff[self.iAltTagSelec] + wData2 * eff.altEff[self.iAltTagSelec]

        return efficiency(ptbin,etabin,newEffData,newErrEffData,newEffMC,newErrEffMC,newEffAltBkgModel,newEffAltSigModel,newEffAltMCSignal,newEffAltTagSelec)


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
          temp  = xbins
          xbins = ybins
          ybins = temp

        ## transform to numpy array for ROOT
        xbinsTab = np.array(xbins)
        ybinsTab = np.array(ybins)
        htitle = 'e/#gamma scale factors'
        hname  = 'h2_scaleFactorsEGamma'

        if onlyError >= 0:
          htitle = 'e/#gamma uncertainties'
          hname  = 'h2_uncertaintiesEGamma'

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
            elif onlyError >= 1 and onlyError <= 6:
              denominator = eff.systCombined if relError else eff.effMC
              h2.SetBinContent(bin, abs(eff.syst[onlyError-1])/denominator)

        if not switchEtaPt: h2.GetYaxis().SetRangeUser(0,2.5) # Only show abseta
        h2.GetYaxis().SetTitle("p_{T} [GeV]" if switchEtaPt else "SuperCluster |#eta|")
        h2.GetXaxis().SetTitle("SuperCluster #eta" if switchEtaPt else "p_{T} [GeV]")
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
