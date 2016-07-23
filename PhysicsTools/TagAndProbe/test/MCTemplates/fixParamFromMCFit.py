#! /usr/bin/env python
import ROOT
from optparse import OptionParser
from os import listdir
from os.path import isfile, join
import os
from string import replace


def GetFitName(filename, keyname):
    pos = keyname.rfind("__")
    if pos == -1:
        return None
    elif "RelAct" in keyname:
        return None
    else:
        output = keyname[pos+2:]
        return output

def Fix(name, params):
    return name+"["+str(params.at(params.index(name)).getVal())+"]"
    
def Constrain(name, params):
    mid = params.at(params.index(name)).getVal()
    elo = abs(params.at(params.index(name)).getAsymErrorLo())
    if elo <= 0:
        elo = abs(params.at(params.index(name)).getError())
    ehi = abs(params.at(params.index(name)).getAsymErrorHi())
    if ehi <= 0:
        ehi = abs(params.at(params.index(name)).getError())
    top = params.at(params.index(name)).getMax()
    bot = params.at(params.index(name)).getMin()
    return name+"["+str(mid)+","+str(max(mid-10.*elo,bot))+","+str(min(mid+10.*ehi,top))+"]"

def Constrain2(name, params):
    mid = params.at(params.index(name)).getVal()
    elo = abs(params.at(params.index(name)).getAsymErrorLo())
    if elo <= 0:
        elo = abs(params.at(params.index(name)).getError())
    ehi = abs(params.at(params.index(name)).getAsymErrorHi())
    if ehi <= 0:
        ehi = abs(params.at(params.index(name)).getError())
    top = params.at(params.index(name)).getMax()
    bot = params.at(params.index(name)).getMin()
    return name+"["+str(mid)+","+str(max(mid-0.1*mid,bot))+","+str(min(mid+0.1*mid,top))+"]"
    
def Float(name, params):
    mid = params.at(params.index(name)).getVal()
    elo = params.at(params.index(name)).getMin()
    ehi = params.at(params.index(name)).getMax()
    return name+"["+str(mid)+","+str(elo)+","+str(ehi)+"]"
    
def main(alternative):
    tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')
    with open(os.path.join(tnpPackage, 'python', "altSigFit_alternative" + str(alternative) + ".py"), "w") as out:
        out.write("import FWCore.ParameterSet.Config as cms\n")
        out.write("\n")
        out.write("block_0 = cms.PSet(\n")

        entry = 0
        block = 0



        altSigMC = os.path.join(tnpPackage, 'test', 'altSig')
        files = [ filename for filename in listdir(altSigMC) if isfile(join(altSigMC,filename)) and "eff_mc_" in filename ]
        for filename in files:
            f = ROOT.TFile(altSigMC +"/"+filename)
	    topDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
	    f.cd(ROOT.gDirectory.GetListOfKeys()[0].GetName())
	    subDir = ROOT.gDirectory.GetListOfKeys()[0].GetName()
	    directory = f.Get(os.path.join(topDir, subDir))

            keys = directory.GetListOfKeys()
            for key in keys:
                if "__" not in key.GetName(): continue
                subdirectory = directory.Get(key.GetName())
                subdirectory.cd();
                results = subdirectory.Get("fitresults")
                params = results.floatParsFinal()
                if entry == 100:
                    entry = 0
                    block += 1
                    if block != 0:
                        out.write(")\n")
                    out.write("block_"+str(block)+" = cms.PSet(\n")
                else:
                    entry += 1
                if GetFitName(filename, key.GetName()) == None:
                    continue
                out.write(GetFitName(filename, key.GetName())+" = cms.vstring(\n")

                if alternative==2:
		  out.write("\"RooDoubleCBFast::signalResPass(mass,"+Float("meanP",params)+","+Float("sigmaP",params)+","+Constrain2("alphaP1",params)+","+Constrain2("nP1",params)+","+Constrain2("alphaP2",params)+","+Constrain2("nP2",params)+")\",\n")
		  out.write("\"RooDoubleCBFast::signalResFail(mass,"+Float("meanF",params)+","+Float("sigmaF",params)+","+Constrain2("alphaF1",params)+","+Constrain2("nF1",params)+","+Constrain2("alphaF2",params)+","+Constrain2("nF2",params)+")\",\n")
                else:
		  out.write("\"RooDoubleCBFast::signalResPass(mass,"+Float("meanP",params)+","+Float("sigmaP",params)+","+Constrain("alphaP1",params)+","+Constrain("nP1",params)+","+Constrain("alphaP2",params)+","+Constrain("nP2",params)+")\",\n")
		  out.write("\"RooDoubleCBFast::signalResFail(mass,"+Float("meanF",params)+","+Float("sigmaF",params)+","+Constrain("alphaF1",params)+","+Constrain("nF1",params)+","+Constrain("alphaF2",params)+","+Constrain("nF2",params)+")\",\n")

                if alternative==1:
                  out.write("\"RooBreitWigner::signalPassBWZ(mass, "+Constrain("mZpass",params)+","+Constrain("sigmaZpass",params)+")\",\n")
                  out.write("\"RooBreitWigner::signalFailBWZ(mass, "+Constrain("mZfail",params)+","+Constrain("sigmaZfail",params)+")\",\n")
                elif alternative==2:
                  out.write("\"RooBreitWigner::signalPassBWZ(mass, "+Constrain2("mZpass",params)+","+Constrain2("sigmaZpass",params)+")\",\n")
                  out.write("\"RooBreitWigner::signalFailBWZ(mass, "+Constrain2("mZfail",params)+","+Constrain2("sigmaZfail",params)+")\",\n")
                else:
                  out.write("\"RooBreitWigner::signalPassBWZ(mass, "+Float("mZpass",params)+","+Float("sigmaZpass",params)+")\",\n")
                  out.write("\"RooBreitWigner::signalFailBWZ(mass, "+Float("mZfail",params)+","+Float("sigmaZfail",params)+")\",\n")

                if alternative==3:
		  out.write("\"RooBreitWigner::signalPassBWtail(mass, "+Constrain("mtailpass",params)+","+Constrain("sigmatailpass",params)+")\",\n")
		  out.write("\"RooBreitWigner::signalFailBWtail(mass, "+Constrain("mtailfail",params)+","+Constrain("sigmatailfail",params)+")\",\n")
		  out.write("\"RooGaussian::signalPassGaus(mass, "+Constrain("meanVP",params)+","+Constrain("sigmaVP",params)+")\",\n")
		  out.write("\"RooGaussian::signalFailGaus(mass, "+Constrain("meanVF",params)+","+Constrain("sigmaVF",params)+")\",\n")
                else:
		  out.write("\"RooBreitWigner::signalPassBWtail(mass, "+Fix("mtailpass",params)+","+Fix("sigmatailpass",params)+")\",\n")
		  out.write("\"RooBreitWigner::signalFailBWtail(mass, "+Fix("mtailfail",params)+","+Fix("sigmatailfail",params)+")\",\n")
		  out.write("\"RooGaussian::signalPassGaus(mass, "+Fix("meanVP",params)+","+Fix("sigmaVP",params)+")\",\n")
		  out.write("\"RooGaussian::signalFailGaus(mass, "+Fix("meanVF",params)+","+Fix("sigmaVF",params)+")\",\n")

                out.write("\"FCONV::signalZPass(mass, signalPassBWZ, signalResPass)\",\n")
                out.write("\"FCONV::signalZFail(mass, signalFailBWZ, signalResFail)\",\n")
                out.write("\"FCONV::signalVoigtPass(mass, signalPassBWtail, signalPassGaus)\",\n")
                out.write("\"FCONV::signalVoigtFail(mass, signalFailBWtail, signalFailGaus)\",\n")

                if alternative==3:
		  out.write("\"SUM::signalPass("+Constrain("cPass",params)+"*signalZPass,signalVoigtPass)\",\n")
		  out.write("\"SUM::signalFail("+Constrain("cFail",params)+"*signalZFail,signalVoigtFail)\",\n")
                else:
		  out.write("\"SUM::signalPass("+Fix("cPass",params)+"*signalZPass,signalVoigtPass)\",\n")
		  out.write("\"SUM::signalFail("+Fix("cFail",params)+"*signalZFail,signalVoigtFail)\",\n")

                out.write("\"RooCMSShape::backgroundPass(mass, "+Float("alphaPass",params)+", "+Float("betaPass",params)+", "+Float("gammaPass",params)+", peakPass[90.0])\",\n")
                out.write("\"RooCMSShape::backgroundFail(mass, "+Float("alphaFail",params)+", "+Float("betaFail",params)+", "+Float("gammaFail",params)+", peakFail[90.0])\",\n")
                out.write("\"efficiency["+str(params.at(params.index("efficiency")).getVal())+",0.,1.]\",\n")
                out.write("\"signalFractionInPassing[1.0]\"\n")
                out.write("),\n")
                out.write("\n")
        out.write(")\n")

        out.write("all_pdfs = cms.PSet(\n")
        for i in range(0,block+1):
            out.write("block_"+str(i)+",\n")
        out.write(")\n")


# This script extracts the parameters from the altSig fit on the MC
# Because the altSig fits on data sometimes fail, we construct a few alternatives with more or less constrain to ensure we can pick out a working fit
if __name__ == "__main__":  
    main(0)
    main(1)
    main(2)
    main(3)
