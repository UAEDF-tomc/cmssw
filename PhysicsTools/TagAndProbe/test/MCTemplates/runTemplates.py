#! /usr/bin/env python
import getTemplatesFromMC
import makeConfigForTemplates
import os, glob

tnpPackage = os.path.join(os.environ['CMSSW_BASE'], 'src', 'PhysicsTools', 'TagAndProbe')

configs = [(False, False, False), (False, False, True), (False, True, False), (False, True, True), (True, False, False), (True, False, True)]
for config in configs:
  usePV, useJets, is2016 = config

  if usePV:     ext  = '_PV'
  elif useJets: ext  = '_jets'
  else:         ext  = ''
  if is2016:    ext += '_2016'
  else:         ext += '_2017'

  templateProduction = 'templatesTTV' + ext

  try:
    os.makedirs(os.path.join(tnpPackage, 'data', templateProduction))
  except:
    pass

  if usePV:     varName = 'event_nPV'
  elif useJets: varName = 'event_njets'
  else:         varName = 'el_sc_abseta'

  if usePV:     bins = "0,5,10,15,20,25,30,35,40,45,9999"
  elif useJets: bins = "-0.5,0.5,1.5,2.5,3.5,4.5,6.5"
  else:         bins = "0.0,0.8,1.4442,1.566,2.0,2.5"

  def getIdLabel(args):
      idProbe, directory, region = args
      return directory.split('To')[0] + 'To' + idProbe + "_" + region


  class options:
      input           = '/user/tomc/tagAndProbe/electrons/tuples/Moriond18_v3/' + ('2016' if is2016 else '2017') + '/DY_amcatnlo.root'
      output          = "mc_templates.root"
      directory       = "GsfElectronToID"
      idprobe         = "passingMedium"
      var1Bins        = "10,20,30,40,50,100,200"
      var2Bins        = bins
      var1Name        = "el_pt"
      var2Name        = varName
      addProbeCut     = ""
      weightVarName   = "totWeight"
      tagTauVarName   = "" # "tag_Ele_dRTau"
      probeTauVarName = "" # "probe_dRTau
      idLabel         = ""
      failBkgPdf      = "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0,70.0,80.0])"
      passBkgPdf      = "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0,70.0,80.0])"
      altSig          = False



  import importlib
  # Manual fix to avoid failed fits, we take a slightly different parameter
  def getBkgPdf(line, type, iteration):
    label = line.split('BKGPDF')[-1].split('"')[0]
    if iteration==0 or iteration==4 or iteration==5 or iteration==6: # First iteration: default
      if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.05, 0, 1], peakFail[90.0,70.0,80.0])"
      if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.05, 0, 1], peakPass[90.0,70.0,80.0])"
    else:
      listOfFailedFits = 'failedFits' + type + str(iteration)
      failedFits = getattr(importlib.import_module('PhysicsTools.TagAndProbe.'+listOfFailedFits), listOfFailedFits)
      if label in failedFits:
        if iteration==1:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.02, 0, 1], peakFail[90.0,70.0,80.0])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.02, 0, 1], peakPass[90.0,70.0,80.0])"
        elif iteration==2:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[50.,30.,100.], betaFail[0.05, 0.001,0.8], gammaFail[0.1, -2, 2], peakFail[90.0, 70, 100])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[50.,30.,100.], betaPass[0.05, 0.001,0.8], gammaPass[0.1, -2, 2], peakPass[90.0, 70, 100])"
        elif iteration==3:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[55.,50.,70.], betaFail[0.001, 0.,0.1], gammaFail[0.02, 0, 1], peakFail[90.0,70.0,80.0])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[55.,50.,70.], betaPass[0.001, 0.,0.1], gammaPass[0.02, 0, 1], peakPass[90.0,70.0,80.0])"
        elif iteration==7 or iteration==8:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,80.], betaFail[0.05, 0.01,0.08], gammaFail[0.1, -2, 2], peakFail[90.0,70.0,80.0])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,80.], betaPass[0.05, 0.01,0.08], gammaPass[0.1, -2, 2], peakPass[90.0,70.0,80.0])"
        elif iteration==9:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[50.,30.,100.], betaFail[0.05, 0.001,0.8], gammaFail[0.1, -2, 2], peakFail[90.0, 70, 100])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[50.,30.,100.], betaPass[0.05, 0.001,0.8], gammaPass[0.1, -2, 2], peakPass[90.0, 70, 100])"
        elif iteration==10 or iteration==11:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[60.,50.,70.], betaFail[0.05, 0.,0.1], gammaFail[0.02, 0, 1], peakFail[90.0,70.0,80.0])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[60.,50.,70.], betaPass[0.05, 0.,0.1], gammaPass[0.02, 0, 1], peakPass[90.0,70.0,80.0])"
        elif iteration==12:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[60.,40.,80.], betaFail[0.001, 0.001,0.8], gammaFail[0.05, -2, 2], peakFail[90.0])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[60.,40.,80.], betaPass[0.001, 0.001,0.8], gammaPass[0.05, -2, 2], peakPass[90.0])"
        elif iteration==13:
          if line.count('FAIL'): return "RooCMSShape::backgroundFail(mass, alphaFail[55.,40.,80.], betaFail[0.001, 0.001,0.8], gammaFail[0.02, -2, 2], peakFail[90.0])"
          if line.count('PASS'): return "RooCMSShape::backgroundPass(mass, alphaPass[55.,40.,80.], betaPass[0.001, 0.001,0.8], gammaPass[0.02, -2, 2], peakPass[90.0])"
        else:
          return getBkgPdf(line, type, iteration - 1)

  def getSigPdf(line, type, iteration):
      label = line.split('SIGPDF')[-1].split('"')[0]
      if iteration==0 or iteration==4 or iteration==7:
        if type == "AltSig":
          if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[0.0,-10.000,10.000],sigmaP[0.956,0.00,10.000],alphaP1[0.999, 0.0,50.0],nP1[1.405,0.000,50.000],alphaP2[0.999,0.0,50.0],nP2[1.405,0.000,50.000])"
          if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[0.0,-10.000,10.000],sigmaF[3.331,0.00,10.000],alphaF1[1.586, 0.0,50.0],nF1[0.464,0.000,20.00],alphaF2[1.586,0.0,50.0],nF2[0.464,0.000,20.00])"
        else:
          if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[0.1,0.100,10.000],sigmaP[1.0,0.001,10.000])" 
          if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[0.1,0.100,10.000],sigmaF[1.0,0.001,10.000])"
      else:
        listOfFailedFits = 'failedFits' + type + str(iteration)
        failedFits = getattr(importlib.import_module('PhysicsTools.TagAndProbe.'+listOfFailedFits), listOfFailedFits)
        if label in failedFits:
          if type == "AltSig":
            if iteration==1:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[2.0,-10.000,10.000],sigmaP[5,0.00,10.000],alphaP1[4, 0.0,50.0],nP1[3,0.000,50.000],alphaP2[1.999,0.0,50.0],nP2[2.405,0.000,50.000])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[2.0,-10.000,10.000],sigmaF[5,0.00,10.000],alphaF1[4, 0.0,50.0],nF1[3,0.000,20.000],alphaF2[2.586,0.0,50.0],nF2[3.464,0.000,20.000])"
            elif iteration==5 or iteration==2:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[0.7,-5.000,5.000],sigmaP[0.4,0.00,10.000],alphaP1[0.8, 0.0,50.0],nP1[1.1,0.000,50.000],alphaP2[0.7,0.0,50.0],nP2[1.2,0.000,50.000])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[0.7,-5.000,5.000],sigmaF[0.4,0.00,10.000],alphaF1[1.3, 0.0,50.0],nF1[0.8,0.000,20.000],alphaF2[1.3,0.0,50.0],nF2[0.64,0.000,20.000])"
            elif iteration==6 or iteration==8:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[0.,-5.000,5.000],sigmaP[1,0.7,6.000],alphaP1[2., 1.2,3.5],nP1[3.,0.05,5.0],alphaP2[1.5,0.5,6.0],nP2[1.,0.5,5.])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[0.,-5.000,5.000],sigmaF[2,0.7,15.00],alphaF1[2., 1.2,3.5],nF1[3.,0.05,5.0],alphaF2[2.0,0.5,6.0],nF2[1.,0.5,5.])"
            elif iteration==9:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[0.2,-5.000,5.000],sigmaP[1,0.7,6.000],alphaP1[2., 0.2,5.5],nP1[3.,0.05,5.0],alphaP2[1.5,0.5,6.0],nP2[1.,0.5,5.])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[0.2,-5.000,5.000],sigmaF[2,0.7,15.00],alphaF1[2., 0.2,5.5],nF1[3.,0.05,5.0],alphaF2[2.0,0.5,6.0],nF2[1.,0.5,5.])"
            elif iteration==10 or iteration==11:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[-0.02,-10.000,10.000],sigmaP[1,0.7,6.000],alphaP1[2., 0.2,5.5],nP1[3.,0.05,5.0],alphaP2[1.5,0.5,6.0],nP2[1.,0.5,5.])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[-0.02,-10.000,10.000],sigmaF[2,0.7,15.00],alphaF1[2., 0.2,5.5],nF1[3.,0.05,5.0],alphaF2[2.0,0.5,6.0],nF2[1.,0.5,5.])"
            elif iteration==12 or iteration==3:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[-0.02,-5.000,5.000],sigmaP[1,0.7,6.000],alphaP1[3., 0.2,5.5],nP1[1.,0.05,5.0],alphaP2[4.5,0.5,6.0],nP2[3.,0.5,5.])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[-0.02,-5.000,5.000],sigmaF[2,0.7,15.00],alphaF1[3., 0.2,5.5],nF1[1.,0.05,5.0],alphaF2[4.0,0.5,6.0],nF2[3.,0.5,5.])"
            elif iteration==13:
              if line.count('FAIL'): return "RooDoubleCBFast::signalResPass(mass,meanP[0.06,-10.000,10.000],sigmaP[1.9,0.01,25.000],alphaP1[3., 0.01,15.5],nP1[1.,0.05,15.0],alphaP2[4.5,0.5,16.0],nP2[3.,0.5,15.])"
              if line.count('PASS'): return "RooDoubleCBFast::signalResFail(mass,meanF[0.06,-10.000,10.000],sigmaF[2.9,0.01,25.00],alphaF1[3., 0.01,15.5],nF1[1.,0.05,15.0],alphaF2[4.0,0.5,16.0],nF2[3.,0.5,15.])"
          else:
            if iteration==1:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[-0.5,-10.000,10.000],sigmaP[2.0,0.001,10.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[-0.5,-10.000,10.000],sigmaF[2.0,0.001,10.000])"
            elif iteration==5 or iteration==2:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[0.7,-5.000,5.000],sigmaP[0.5,0.001,10.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[0.7,-5.000,5.000],sigmaF[0.5,0.001,10.000])"
            elif iteration==6 or iteration==8:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[0.,-5.000,5.000],sigmaP[0.9,0.5,5.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[0.,-5.000,5.000],sigmaF[0.9,0.5,5.000])"
            elif iteration==9 or iteration==3:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[0.2,-5.000,5.000],sigmaP[0.9,0.5,5.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[0.2,-5.000,5.000],sigmaF[0.9,0.5,5.000])"
            elif iteration==10 or iteration==11:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[-0.02,-10.000,10.000],sigmaP[0.7,0.5,5.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[-0.02,-10.000,10.000],sigmaF[0.7,0.5,5.000])"
            elif iteration==12:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[-0.06,-10.000,10.000],sigmaP[1.7,0.5,5.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[-0.06,-10.000,10.000],sigmaF[1.7,0.5,5.000])"
            elif iteration==13:
              if line.count('FAIL'): return "RooGaussian::signalResPass(mass, meanP[0.06,-10.000,10.000],sigmaP[0.3,0.001,10.000])" 
              if line.count('PASS'): return "RooGaussian::signalResFail(mass, meanF[0.06,-10.000,10.000],sigmaF[0.3,0.001,10.000])"
        else:
          return getSigPdf(line, type, iteration - 1)



  def runGetTemplatesFromMC(args):
      idProbe, directory, region = args

      myOptions = options()

      if region == "alleta":     options.var2Bins = "0,2.5"
      if region == "barrel":     options.var2Bins = "0,0.8,1.442"
      if region == "crack":      options.var2Bins = "1.442,1.566"
      if region == "endcap":     options.var2Bins = "1.566,2.0,2.5"

      myOptions.idLabel      = getIdLabel(args)
      myOptions.output       = os.path.join(tnpPackage, 'data', templateProduction, myOptions.idLabel + ".root")
      myOptions.directory    = directory
      myOptions.idprobe      = "passing" + idProbe
      getTemplatesFromMC.main(myOptions)

      myOptions.outputFile   = os.path.join(tnpPackage, 'python', "nominalFit" + ext + "_" + myOptions.idLabel + ".py")
      myOptions.templateFile = myOptions.output
      makeConfigForTemplates.main(myOptions)

      myOptions.outputFile   = os.path.join(tnpPackage, 'python', "altTagFit" + ext + "_" + myOptions.idLabel + ".py")
      makeConfigForTemplates.main(myOptions)

      myOptions.altSig       = True  # Also make templates for MC to be used for the altSig systematic
      myOptions.outputFile   = os.path.join(tnpPackage, 'python', "altSigFit" + ext + "_" + myOptions.idLabel + ".py")
      makeConfigForTemplates.main(myOptions)

  jobs = []
  for region in ["PV"] if usePV else (["njets"] if useJets else ["alleta","barrel","crack","endcap"]):
    jobs.append(("TTVLoose",                    "EleToId",                       region))
    jobs.append(("TTVLeptonMvaL",               "TTVLooseToLeptonMva",           region))
    jobs.append(("TTVLeptonMvaM",               "TTVLooseToLeptonMva",           region))
    jobs.append(("TTVLeptonMvaT",               "TTVLooseToLeptonMva",           region))
    jobs.append(("TightCharge",                 "TTVLeptonMvaLToTightCharge",    region))
    jobs.append(("TightCharge",                 "TTVLeptonMvaMToTightCharge",    region))
    jobs.append(("TightCharge",                 "TTVLeptonMvaTToTightCharge",    region))

  from multiprocessing import Pool
  pool = Pool(processes=16)
  pool.map(runGetTemplatesFromMC, jobs)
  pool.close()
  pool.join()

  iteration=0
  # Adding everything to all_pdfs, a bit complex as CMSSW doesn't accept more than 255 arguments to a PSet
  for fit in ['nominalFit', 'altSigFit', 'altTagFit']:
    if fit.count('nominal'): type = 'Nominal'
    if fit.count('altSig'):  type = 'AltSig'
    if fit.count('altTag'):  type = 'AltTag'
    with open(os.path.join(tnpPackage, 'python', fit + ext + '.py'), 'w') as f:
      f.write('import FWCore.ParameterSet.Config as cms\n\n')

      for args in jobs:
        f.write('pdfs_' + getIdLabel(args) + ' = cms.PSet(\n')
        with open(os.path.join(tnpPackage, 'python', fit + ext + "_" + getIdLabel(args) + ".py"), "r") as r:
          for line in r.readlines()[3:-2]:
            if   line.count('BKGPDF'): f.write('"' + getBkgPdf(line, type, iteration) + '",\n')
            elif line.count('SIGPDF'): f.write('"' + getSigPdf(line, type, iteration) + '",\n')
            else:                      f.write(line)
        f.write(')\n\n')

      f.write('all_pdfs = cms.PSet(\n')
      for args in jobs:
        f.write('  pdfs_' + getIdLabel(args) + ',\n')
      f.write(')')

    import glob, os
    map(os.remove, glob.glob(os.path.join(tnpPackage, 'python', fit + ext + '_*.p*')))


  # For background shape systematic, replace RooCMSShape with RooExponetial (take three alternatives for initial parameters to be sure at least one fit succeeds)
  with open(os.path.join(tnpPackage, 'python', 'altBkgFit' + ext + '_alternative0.py'), 'w') as f:
    with open(os.path.join(tnpPackage, 'python', 'nominalFit' + ext + '.py'), 'r') as r:
      for line in r:
        if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[-0.001, -.1, .1])",\n')
        elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[-0.001, -.1, .1])",\n')
        else:                                           f.write(line)

  with open(os.path.join(tnpPackage, 'python', 'altBkgFit' + ext + '_alternative1.py'), 'w') as f:
    with open(os.path.join(tnpPackage, 'python', 'nominalFit' + ext + '.py'), 'r') as r:
      for line in r:
        if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[0.02, -.1, .1])",\n')
        elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[0.02, -.1, .1])",\n')
        else:                                           f.write(line)

  with open(os.path.join(tnpPackage, 'python', 'altBkgFit' + ext + '_alternative2.py'), 'w') as f:
    with open(os.path.join(tnpPackage, 'python', 'nominalFit' + ext + '.py'), 'r') as r:
      for line in r:
        if   line.count('RooCMSShape::backgroundPass'): f.write('"RooExponential::backgroundPass(mass, aExpP[-0.02, -.1, .1])",\n')
        elif line.count('RooCMSShape::backgroundFail'): f.write('"RooExponential::backgroundFail(mass, aExpF[-0.02, -.1, .1])",\n')
        else:                                           f.write(line)
