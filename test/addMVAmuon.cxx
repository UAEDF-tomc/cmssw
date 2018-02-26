#include "TTree.h"
#include "TFile.h"
#include "TStopwatch.h"
#include "TMVA/Reader.h"
#include <algorithm>

void addMVAmuon(TString fileName) {
  TFile *f = TFile::Open(fileName + ".root");
  TTree *tIn = (TTree *) f->Get("tpTree/fitter_tree");
  //// Variables for MVA 
  bool medium;
  float pt, eta, sip3d, dB, dzPV, segmComp, trackMult, miniIsoCharged, miniIsoNeutral, relIso0p3;
  float ptrel, JetPtRatio, JetBTagCSV, fixedGridRhoFastjetCentralNeutral;
  //// Other variables to save 
  tIn->SetBranchAddress("Medium"                           , &medium                           );
  tIn->SetBranchAddress("pt"                               , &pt                               );
  tIn->SetBranchAddress("eta"                              , &eta                              );
  tIn->SetBranchAddress("SIP"                              , &sip3d                            );
  tIn->SetBranchAddress("dB"                               , &dB                               );
  tIn->SetBranchAddress("dzPV"                             , &dzPV                             );
  tIn->SetBranchAddress("segmentCompatibility"             , &segmComp                         );
  tIn->SetBranchAddress("JetNDauCharged"                   , &trackMult                        );
  tIn->SetBranchAddress("miniIsoCharged"                   , &miniIsoCharged                   );
  tIn->SetBranchAddress("miniIsoNeutrals"                  , &miniIsoNeutral                   );
  tIn->SetBranchAddress("JetPtRel"                         , &ptrel                            );
  tIn->SetBranchAddress("JetPtRatio"                       , &JetPtRatio                       );
  tIn->SetBranchAddress("JetBTagCSV"                       , &JetBTagCSV                       );
  tIn->SetBranchAddress("combRelIsoPF03"                   , &relIso0p3                        );
  tIn->SetBranchAddress("fixedGridRhoFastjetCentralNeutral", &fixedGridRhoFastjetCentralNeutral);

  TFile *fOut = new TFile(fileName + "_withIsoAndMva.root", "RECREATE");
  fOut->mkdir("tpTree")->cd();
  TTree *tOut = tIn->CloneTree(0);
  float miniCombRelIsoTTH = -999999., mvaIdTTH = -999999.;
  bool Feb2018Loose, Feb2018LeptonMvaL, Feb2018LeptonMvaM, Feb2018LeptonMvaT;
  tOut->Branch("miniCombRelIsoTTH", &miniCombRelIsoTTH, "miniCombRelIsoTTH/F");
  tOut->Branch("mvaIdTTH"         , &mvaIdTTH         , "mvaIdTTH/F");
  tOut->Branch("Feb2018Loose",      &Feb2018Loose,      "Feb2018Loose/O");
  tOut->Branch("Feb2018LeptonMvaL", &Feb2018LeptonMvaL, "Feb2018LeptonMvaL/O");
  tOut->Branch("Feb2018LeptonMvaM", &Feb2018LeptonMvaM, "Feb2018LeptonMvaM/O");
  tOut->Branch("Feb2018LeptonMvaT", &Feb2018LeptonMvaT, "Feb2018LeptonMvaT/O");

  float ptratio, jetbtagCSV;

  TMVA::Reader *reader = new TMVA::Reader("!Color:!Silent");

  reader->AddVariable( "pt",                &pt);
  reader->AddVariable( "eta",               &eta);
  reader->AddVariable( "trackMult",         &trackMult);
  reader->AddVariable( "miniIsoCharged",    &miniIsoCharged);
  reader->AddVariable( "miniIsoNeutral",    &miniIsoNeutral);
  reader->AddVariable( "ptrel",             &ptrel);
  reader->AddVariable( "min(ptratio,1.5)",  &ptratio);
  reader->AddVariable( "relIso0p3",         &relIso0p3);
  reader->AddVariable( "max(jetbtagCSV,0)", &jetbtagCSV);
  reader->AddVariable( "sip3d",             &sip3d);
  reader->AddVariable( "segmComp",          &segmComp);

  reader->BookMVA("BDTG method", "../data/muBDTG.weights.xml");

  // Effective areas: |eta| < {0.8, 1.3, 2.0, 2.2, 2.4}
  Float_t muonEAs[5] = {0.0735, 0.0619, 0.0465, 0.0433, 0.0577};

  int step = tIn->GetEntries()/1000;
  double evDenom = 100.0/double(tIn->GetEntries());
  TStopwatch timer;
  timer.Start();
  for (int i=0, n=tIn->GetEntries(); i<n; ++i) {
    tIn->GetEntry(i);

    // Compute miniIso
    Float_t abseta = std::abs(eta);
    Float_t ea = muonEAs[4];
    if     (abseta<0.8) ea = muonEAs[0];
    else if(abseta<1.3) ea = muonEAs[1];
    else if(abseta<2.0) ea = muonEAs[2];
    else if(abseta<2.2) ea = muonEAs[3];
        
    miniCombRelIsoTTH = (miniIsoCharged + std::max(0.0, miniIsoNeutral - ea*fixedGridRhoFastjetCentralNeutral * std::pow((10.0/min(max((double)pt, 50.), 200.))/0.3,2)));
    miniCombRelIsoTTH /= pt;

    if(i<20) {
      printf("muon with pt = %.2f, eta = %+5.2f:", pt, eta);
      printf("   charged hadrons %6.3f, neutral hadrons %6.3f, photons %6.3f ", miniIsoCharged, miniIsoNeutral, 0.0);
      printf("   rho %6.3f, ea %6.3f", fixedGridRhoFastjetCentralNeutral, ea);
      printf("   pfCombAbsMiniIsoEAcorr %6.3f\n", miniCombRelIsoTTH);
    }

    // Compute the MVA discriminator
    ptratio         = std::min((double)JetPtRatio, 1.5);
    jetbtagCSV      = std::max((double)JetBTagCSV, 0.0);

    mvaIdTTH = reader->EvaluateMVA("BDTG method");
    Feb2018Loose      = (medium==1 and fabs(dB) < 0.05 and fabs(dzPV) < 0.1 and fabs(sip3d) < 8 and miniCombRelIsoTTH < 0.4);
    Feb2018LeptonMvaL = mvaIdTTH > 0.8;
    Feb2018LeptonMvaM = mvaIdTTH > 0.85;
    Feb2018LeptonMvaT = mvaIdTTH > 0.9;

    // Fill the output tree
    tOut->Fill();
    //if (i > 10000) break;
    if ((i+1) % step == 0) { 
      double totalTime = timer.RealTime()/60.; timer.Continue();
      double fraction = double(i+1)/double(n+1), remaining = totalTime*(1-fraction)/fraction;
      printf("Done %9d/%9d   %5.1f%%   (elapsed %5.1f min, remaining %5.1f min)\n", i, n, i*evDenom, totalTime, remaining); 
      fflush(stdout); 
    }
  }

  tOut->AutoSave(); // according to root tutorial this is the right thing to do
  fOut->Close();
}
