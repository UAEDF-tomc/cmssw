#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"


#include "TMVA/Reader.h"

#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "TMath.h"

namespace{
  template<typename T> void Store(edm::Event &iEvent, const edm::Handle<std::vector<pat::Electron>> &probes,
	                          const std::vector<T> &values, const std::string &name){
      std::auto_ptr<edm::ValueMap<T>> valMap(new edm::ValueMap<T>());
      typename edm::ValueMap<T>::Filler filler(*valMap);
      filler.insert(probes, values.begin(), values.end());
      filler.fill();
      iEvent.put(valMap, name);
  }

  float slidingCut(float pt, float low, float high){
    float slope = (high - low)/10.;
    return std::min(low, std::max(high, low + slope*(pt-15)));
  }

  bool PassMVAVLooseFOIDEmu(double pt, double mva, double abssceta){
    if(abssceta<0.8)        return mva > (pt < 10 ? -0.30 : slidingCut(pt, -0.86, -0.96));
    else if(abssceta<1.479) return mva > (pt < 10 ? -0.36 : slidingCut(pt, -0.85, -0.96));
    else if(abssceta<2.5)   return mva > (pt < 10 ? -0.63 : slidingCut(pt, -0.81, -0.95));
    else                    return false;
  }

  bool PassMVAVLoose(double pt, double mva, double abssceta){
    if(abssceta<0.8)        return mva > (pt < 10 ?  0.46 : slidingCut(pt, -0.48, -0.85));
    else if(abssceta<1.479) return mva > (pt < 10 ? -0.03 : slidingCut(pt, -0.67, -0.91));
    else if(abssceta<2.5)   return mva > (pt < 10 ?  0.06 : slidingCut(pt, -0.49, -0.83));
    else                    return false;
  }

  bool PassMVATight(double pt, double mva, double abssceta){
    if(abssceta<0.8)        return mva > slidingCut(pt, 0.77,  0.52);
    else if(abssceta<1.479) return mva > slidingCut(pt, 0.56,  0.11);
    else if(abssceta<2.5)   return mva > slidingCut(pt, 0.48, -0.01);
    else                    return false;
  }

  bool PassLooseIP2D(double dxy, double dz){
    return std::abs(dxy) < 0.2 && std::abs(dz) < 0.5;
  }

  bool PassTightIP2D(double dxy, double dz){
    return std::abs(dxy) < 0.05 && std::abs(dz) < 0.1;
  }

  bool PassPOGIP2D(double dxy, double dz, bool endcap){
    if(endcap) return std::abs(dxy) < 0.1 && std::abs(dz) < 0.2;
    else       return std::abs(dxy) < 0.05 && std::abs(dz) < 0.1;
  }

  bool PassIDEmu(const pat::Electron &ele){
    float eInvMinusPInv = std::abs(1.0 - ele.eSuperClusterOverP())/ele.ecalEnergy();
    if(ele.full5x5_sigmaIetaIeta()                    >= (ele.isEB() ? 0.011 : 0.031)) return false;
    if(std::abs(ele.deltaEtaSuperClusterTrackAtVtx()) >= 0.01)                         return false;
    if(std::abs(ele.deltaPhiSuperClusterTrackAtVtx()) >= (ele.isEB() ? 0.04  : 0.08))  return false;
    if(ele.hadronicOverEm()                           >= 0.08)                         return false;
    if(eInvMinusPInv                                  >= 0.01)                         return false;
    return true;
  }

  bool PassIDEmuDoubleEG(const pat::Electron &ele){
    float eInvMinusPInv = (1.0 - ele.eSuperClusterOverP())/ele.ecalEnergy();
    if(ele.full5x5_sigmaIetaIeta()                    >= (ele.isEB() ? 0.011 : 0.030)) return false;
    if(std::abs(ele.deltaPhiSuperClusterTrackAtVtx()) >= (ele.isEB() ? 0.04  : 0.07))  return false;
    if(std::abs(ele.deltaEtaSuperClusterTrackAtVtx()) >= (ele.isEB() ? 0.01  : 0.008)) return false;
    if(ele.hadronicOverEm()                           >= (ele.isEB() ? 0.10  : 0.07))  return false;
    if(eInvMinusPInv                                  <= -0.05)                        return false;
    if(eInvMinusPInv                                  >= (ele.isEB() ? 0.01  : 0.005)) return false;
    return true;
  }

  bool PassISOEmu(const pat::Electron &ele){
    return ele.ecalPFClusterIso()/ele.pt() < 0.45 and ele.hcalPFClusterIso()/ele.pt() < 0.25 and ele.dr03TkSumPt()/ele.pt() < 0.2;
  }

  // Cuts based on: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2#Working_points_for_2016_data_for
  // Spring16, 25ns		         Veto B    Loose B   Medium B  Tight B    Veto E   Loose E   Medium E  Tight E
  std::vector<float> maxSigmaIetaIeta = {0.0115,   0.011,    0.00998,  0.00998,   0.037,   0.0314,   0.0298,   0.0292};
  std::vector<float> maxDEtaIn        = {0.00749,  0.00477,  0.00311,  0.00308,   0.00895, 0.00868,  0.00609,  0.00605};
  std::vector<float> maxDPhiIn        = {0.228,    0.222,    0.103,    0.0816,    0.213,   0.213,    0.045,    0.0394};
  std::vector<float> maxHOverE        = {0.356,    0.298,    0.253,    0.0414,    0.211,   0.101,    0.0878,   0.0641};
  std::vector<float> maxOoEmooP       = {0.299,    0.241,    0.134,    0.0129,    0.15,    0.14,     0.13,     0.0129};
  std::vector<int>   maxMissingHits   = {2,        1,        1,        1,         3,       1,        1,        1};
  std::vector<bool>  convVeto         = {true,     true,     true,     true,      true,    true,     true,     true};

  // Cuts based on: https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Spring15_selection_25ns
  // Spring15, 25ns		         Veto B    Loose B   Medium B  Tight B    Veto E   Loose E   Medium E  Tight E
  std::vector<float> maxSigmaIetaIetaSpring15 = {0.0114,   0.0103,   0.0101,   0.0101,    0.0352,  0.0301,   0.0283,   0.0279};
  std::vector<float> maxDEtaInSpring15        = {0.0152,   0.0105,   0.0103,   0.00926,   0.0113,  0.00814,  0.00733,  0.00724};
  std::vector<float> maxDPhiInSpring15        = {0.216,    0.115,    0.0336,   0.0336,    0.237,   0.182,    0.114,    0.0918};
  std::vector<float> maxHOverESpring15        = {0.181,    0.104,    0.0876,   0.0597,    0.116,   0.0897,   0.0678,   0.0615};
  std::vector<float> maxOoEmooPSpring15       = {0.207,    0.102,    0.0174,   0.012,     0.174,   0.126,    0.0898,   0.00999};
  std::vector<float> maxd0Spring15            = {0.0564,   0.0261,   0.0118,   0.0111,    0.222,   0.118,    0.0739,   0.0351};
  std::vector<float> maxdzSpring15            = {0.472,    0.41,     0.373,    0.0466,    0.921,   0.822,    0.602,    0.417};
  std::vector<int>   maxMissingHitsSpring15   = {2,        2,        2,        2,         3,       1,        1,        1};
  std::vector<bool>  convVetoSpring15         = {true,     true,     true,     true,      true,    true,     true,     true};



  float dEtaInSeed(const pat::Electron& ele){
    if(ele.superCluster().isNonnull() and ele.superCluster()->seed().isNonnull()) return ele.deltaEtaSuperClusterTrackAtVtx() - ele.superCluster()->eta() + ele.superCluster()->seed()->eta();
    else                                                                          return std::numeric_limits<float>::max();
  }

  bool PassCutBased(const pat::Electron &ele, float dxy, float dz, int missingHits, int level){
    if(ele.isEB())                                                    level = level;
    else if(ele.isEE() and std::abs(ele.superCluster()->eta()) < 2.5) level = level + 4;
    else return false;

    float eInvMinusPInv = std::abs(1.0 - ele.eSuperClusterOverP())/ele.ecalEnergy();

    if(ele.full5x5_sigmaIetaIeta()                    >= maxSigmaIetaIeta[level]) return false;
    if(std::abs(dEtaInSeed(ele))                      >= maxDEtaIn[level])        return false;
    if(std::abs(ele.deltaPhiSuperClusterTrackAtVtx()) >= maxDPhiIn[level])        return false;
    if(ele.hadronicOverEm()                           >= maxHOverE[level])        return false;
    if(eInvMinusPInv                                  >= maxOoEmooP[level])       return false;
    if(missingHits                                    >  maxMissingHits[level])   return false;
    if(convVeto[level] and not ele.passConversionVeto())                          return false;

    return true;
  }

  bool PassCutBasedSpring15(const pat::Electron &ele, float dxy, float dz, int missingHits, int level){
    if(ele.isEB())                                                    level = level;
    else if(ele.isEE() and std::abs(ele.superCluster()->eta()) < 2.5) level = level + 4;
    else return false;

    float eInvMinusPInv = std::abs(1.0 - ele.eSuperClusterOverP())/ele.ecalEnergy();

    if(ele.full5x5_sigmaIetaIeta()                    >= maxSigmaIetaIetaSpring15[level]) return false;
    if(std::abs(ele.deltaEtaSuperClusterTrackAtVtx()) >= maxDEtaInSpring15[level])        return false;
    if(std::abs(ele.deltaPhiSuperClusterTrackAtVtx()) >= maxDPhiInSpring15[level])        return false;
    if(ele.hadronicOverEm()                           >= maxHOverESpring15[level])        return false;
    if(eInvMinusPInv                                  >= maxOoEmooPSpring15[level])       return false;
    if(missingHits                                    >  maxMissingHitsSpring15[level])   return false;
    if(std::abs(dxy)                                  >= maxd0Spring15[level])            return false;
    if(std::abs(dz)                                   >= maxdzSpring15[level])            return false;
    if(convVetoSpring15[level] and not ele.passConversionVeto())                          return false;

    return true;
  }


  bool PassMultiIso(TString level, double mini_iso, double jetPtRatio, double jetPtRel){
    if(level == "VL") return mini_iso < 0.25 && (jetPtRatio > 0.67 || jetPtRel > 4.4);
    if(level == "L")  return mini_iso < 0.20 && (jetPtRatio > 0.69 || jetPtRel > 6.0);
    if(level == "M")  return mini_iso < 0.16 && (jetPtRatio > 0.76 || jetPtRel > 7.2);
    if(level == "T")  return mini_iso < 0.12 && (jetPtRatio > 0.80 || jetPtRel > 7.2);
    if(level == "VT") return mini_iso < 0.09 && (jetPtRatio > 0.84 || jetPtRel > 7.2);
    return false;
  }

  bool PassLeptonMva(TString level, double mva){
    if(level == "L")  return mva > 0.8;
    if(level == "M")  return mva > 0.85;
    if(level == "T")  return mva > 0.9;
    return false;
  }

  // Because CMS wouldn't be CMS if some people want to make it really complicated, can't understand how this kind of selections get through approval
  bool PassTTHLoose(const pat::Electron &ele, float dxy, float dz, float sip3d, double miniIso, int missingHits, double mva){
    if(!PassIDEmuDoubleEG(ele))                       return false;
    if(std::abs(dxy) > 0.05)                          return false;
    if(std::abs(dz) > 0.1)                            return false;
    if(std::abs(sip3d) > 8)                           return false;
    if(miniIso > 0.4)                                 return false;
    if(!PassMVAVLoose(ele.pt(), mva, abs(ele.eta()))) return false;
    return true;
  }
/*
  bool PassTTHFO(const pat::Electron &ele, float dxy, float dz, float sip3d, double miniIso, int missingHits, double closestJetCSV, double mva, double mvaHZZ, double ptRatio, double leptonMva){
    if(!PassTTHLoose(ele, dxy, dz, sip3d, miniIso, missingHits, mva)) return false;
    if(closestJetCSV > 0.8484)                                        return false;
    if(leptonMva < 0.9){
      if(ptRatio < 0.5)                                               return false;
      if(closestJetCSV > 0.3)                                         return false;
      if(mvaHZZ  < (ele.isEB()? 0 : 0.7))                             return false;
    }
    if(!PassIDEmuDoubleEG(ele))                                       return false;
//  if(!eleIsClean)                                                   return false; // won't add this one, should have not much effect for the tag and pro be
    return true;
  }*/
}



class MyElectronVariableHelper : public edm::EDProducer {
public:
  explicit MyElectronVariableHelper(const edm::ParameterSet & iConfig);
  virtual ~MyElectronVariableHelper() ;
  
  virtual void beginJob();
  bool combine(std::map<TString, std::vector<bool>>& passWorkingPoints, std::vector<TString> wps);
  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) override;
  
private:
  EffectiveAreas effectiveAreas_;
  edm::EDGetTokenT<std::vector<pat::Electron>> probesToken_;
  edm::EDGetTokenT<edm::View<reco::Candidate>> probesViewToken_;
  edm::EDGetTokenT<edm::ValueMap<bool>> tightToken_;
  edm::EDGetTokenT<edm::ValueMap<bool>> triggerEmuToken_;
  edm::EDGetTokenT<edm::ValueMap<bool>> mvaWP80Token_;
  edm::EDGetTokenT<edm::ValueMap<bool>> mvaWP90Token_;
  edm::EDGetTokenT<edm::ValueMap<float>> mvaTokenHZZ_;
  edm::EDGetTokenT<edm::ValueMap<float>> mvaToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> dxyToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> dzToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> miniIsoToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> chargedMiniIsoToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> neutralMiniIsoToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> jetPtRatioToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> jetPtRelToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> jetNDauChargedToken_;
  edm::EDGetTokenT<edm::ValueMap<float>> jetBTagCSVToken_;
  edm::EDGetTokenT<double>               rhoToken_;
  float pt, eta, trackMult, miniIsoCharged, miniIsoNeutral;
  float ptrel, ptratio, relIso0p3, jetbtagCSV, sip3d, eleMVA;

  TMVA::Reader *readerEle;

  std::vector<TString> workingPoints;
};



MyElectronVariableHelper::MyElectronVariableHelper(const edm::ParameterSet & iConfig) :
  effectiveAreas_(                                         (iConfig.getParameter<edm::FileInPath>("effAreasConfigFile")).fullPath()),
  probesToken_(        consumes<std::vector<pat::Electron>>(iConfig.getParameter<edm::InputTag>("probes"))),
  probesViewToken_(    consumes<edm::View<reco::Candidate>>(iConfig.getParameter<edm::InputTag>("probes"))),
  tightToken_(         consumes<edm::ValueMap<bool>>(       iConfig.getParameter<edm::InputTag>("tight"))),
  triggerEmuToken_(    consumes<edm::ValueMap<bool>>(       iConfig.getParameter<edm::InputTag>("triggerEmu"))),
  mvaWP80Token_(       consumes<edm::ValueMap<bool>>(       iConfig.getParameter<edm::InputTag>("mvaWP80"))),
  mvaWP90Token_(       consumes<edm::ValueMap<bool>>(       iConfig.getParameter<edm::InputTag>("mvaWP90"))),
  mvaTokenHZZ_(        consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("mvasHZZ"))),
  mvaToken_(           consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("mvas"))),
  dxyToken_(           consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("dxy"))),
  dzToken_(            consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("dz"))),
  miniIsoToken_(       consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("miniIso"))),
  chargedMiniIsoToken_(consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("chargedMiniIso"))),
  neutralMiniIsoToken_(consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("neutralMiniIso"))),
  jetPtRatioToken_(    consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetPtRatio"))),
  jetPtRelToken_(      consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetPtRel"))),
  jetNDauChargedToken_(consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetNDauCharged"))),
  jetBTagCSVToken_(    consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetBTagCSV"))),
  rhoToken_(           consumes<double>(                    iConfig.getParameter<edm::InputTag>("rho"))){

    produces<edm::ValueMap<float> >("sip3d");
    produces<edm::ValueMap<float> >("ecalIso");
    produces<edm::ValueMap<float> >("hcalIso");
    produces<edm::ValueMap<float> >("trackIso");
    produces<edm::ValueMap<int> >("missIHits");

    workingPoints = {"CutBasedV", "CutBasedVPOGIP2D", "CutBasedSpring15V",
                     "CutBasedL", "CutBasedLPOGIP2D", "CutBasedSpring15L",
                     "CutBasedM", "CutBasedMPOGIP2D", "CutBasedSpring15M",
                     "CutBasedT", "CutBasedTPOGIP2D", "CutBasedSpring15T",
                     "CutBasedStopsDilepton", "TTZ", "TTG", "MVAWP90IDEMuTTZRelIsoCBL", "MVAWP90IDEMuTTZ", "MVAWP90", "TTZ2017", "TTZ2017TightCharge",
                     "MVAVLooseTightIP2D", "MVAVLooseFOIDEmuTightIP2D", 
                     "MVATightTightIP2DSIP3D4", "MVATightIDEmuTightIP2DSIP3D4", "MVATightIDEmuTightIP2DSIP3D4ConvVetoIHit0",
                     "Mini", "Mini2", "Mini4", "RelIso010", "RelIso012",
                     "MultiIsoM", "MultiIsoT", "MultiIsoVT", "MultiIsoTISOEmu",
                     "ConvVetoIHit1", "ConvVetoIHit0", "Charge",
                     "Feb2018Loose","Feb2018LeptonMvaL","Feb2018LeptonMvaM","Feb2018LeptonMvaT","TightCharge",
                     "RFeb2018LeptonMvaL","RFeb2018LeptonMvaM","RFeb2018LeptonMvaT",
                     "triggerEmu"};
    for(TString wp : workingPoints) produces<edm::ValueMap<bool>>(("pass" + wp).Data());
}

MyElectronVariableHelper::~MyElectronVariableHelper(){
}

void MyElectronVariableHelper::beginJob(){

    readerEle  = new TMVA::Reader( "!Color:!Silent" );

    readerEle->AddVariable( "pt",                &pt);
    readerEle->AddVariable( "eta",               &eta);
    readerEle->AddVariable( "trackMult",         &trackMult);
    readerEle->AddVariable( "miniIsoCharged",    &miniIsoCharged);
    readerEle->AddVariable( "miniIsoNeutral",    &miniIsoNeutral);
    readerEle->AddVariable( "ptrel",             &ptrel);
    readerEle->AddVariable( "min(ptratio,1.5)",  &ptratio);
    readerEle->AddVariable( "relIso0p3",         &relIso0p3);
    readerEle->AddVariable( "max(jetbtagCSV,0)", &jetbtagCSV);
    readerEle->AddVariable( "sip3d",             &sip3d);
    readerEle->AddVariable( "eleMVA",            &eleMVA);

    edm::FileInPath *fip = new edm::FileInPath("PhysicsTools/TagAndProbe/data/eleBDTG.weights.xml");
    readerEle->BookMVA("BDTG method", fip->fullPath().c_str());
}

// Combine workingpoints
bool MyElectronVariableHelper::combine(std::map<TString, std::vector<bool>>& passWorkingPoints, std::vector<TString> wps){
    for(TString wp : wps) if(!passWorkingPoints[wp].back()) return false;
    return true;
}


void MyElectronVariableHelper::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  // read input
  edm::Handle<std::vector<pat::Electron>> probes;      iEvent.getByToken(probesToken_,         probes);
  edm::Handle<edm::View<reco::Candidate>> probes_view; iEvent.getByToken(probesViewToken_,     probes_view);
  edm::Handle<edm::ValueMap<bool>> tightBools;         iEvent.getByToken(tightToken_,          tightBools);
  edm::Handle<edm::ValueMap<bool>> triggerEmuBools;    iEvent.getByToken(triggerEmuToken_,     triggerEmuBools);
  edm::Handle<edm::ValueMap<bool>> mvasWP80;           iEvent.getByToken(mvaWP80Token_,        mvasWP80);
  edm::Handle<edm::ValueMap<bool>> mvasWP90;           iEvent.getByToken(mvaWP90Token_,        mvasWP90);
  edm::Handle<edm::ValueMap<float>> mvasHZZ;           iEvent.getByToken(mvaTokenHZZ_,         mvasHZZ);
  edm::Handle<edm::ValueMap<float>> mvas;              iEvent.getByToken(mvaToken_,            mvas);
  edm::Handle<edm::ValueMap<float>> dxys;              iEvent.getByToken(dxyToken_,            dxys);
  edm::Handle<edm::ValueMap<float>> dzs;               iEvent.getByToken(dzToken_,             dzs);
  edm::Handle<edm::ValueMap<float>> miniIsos;          iEvent.getByToken(miniIsoToken_,        miniIsos);
  edm::Handle<edm::ValueMap<float>> chargedMiniIsos;   iEvent.getByToken(chargedMiniIsoToken_, chargedMiniIsos);
  edm::Handle<edm::ValueMap<float>> neutralMiniIsos;   iEvent.getByToken(neutralMiniIsoToken_, neutralMiniIsos);
  edm::Handle<edm::ValueMap<float>> jetPtRatios;       iEvent.getByToken(jetPtRatioToken_,     jetPtRatios);
  edm::Handle<edm::ValueMap<float>> jetPtRels;         iEvent.getByToken(jetPtRelToken_,       jetPtRels);
  edm::Handle<edm::ValueMap<float>> jetNDauChargeds;   iEvent.getByToken(jetNDauChargedToken_, jetNDauChargeds);
  edm::Handle<edm::ValueMap<float>> jetBTagCSVs;       iEvent.getByToken(jetBTagCSVToken_,     jetBTagCSVs);
  edm::Handle<double>               rhoHandle;         iEvent.getByToken(rhoToken_,            rhoHandle);

  double rho = *rhoHandle;

  // prepare vector for output
  std::vector<float> sip3dValues;
  std::vector<float> ecalIsoValues;
  std::vector<float> hcalIsoValues;
  std::vector<float> trackIsoValues;
  std::vector<int> missingInnerHitsValues;

  std::map<TString, std::vector<bool>> passWorkingPoints;
  for(TString wp : workingPoints) passWorkingPoints[wp] = std::vector<bool>();

  size_t i = 0;
  for(const auto &probe: *probes){
    edm::RefToBase<reco::Candidate> pp = probes_view->refAt(i);

    float ip3d             = probe.dB(pat::Electron::PV3D);
    float ip3d_err         = probe.edB(pat::Electron::PV3D);
    float sip3d            = ip3d/ip3d_err;
    bool  tight            = (*tightBools)[pp];
    bool  triggerEmu       = (*triggerEmuBools)[pp];
    bool  mvaWP80          = (*mvasWP80)[pp];
    bool  mvaWP90          = (*mvasWP90)[pp];
    float mva              = pp->pt() < 10 ? (*mvasHZZ)[pp] : (*mvas)[pp];
   // float mvaHZZ           = (*mvasHZZ)[pp];
    float dxy              = (*dxys)[pp];
    float dz               = (*dzs)[pp];
    float mini_iso         = (*miniIsos)[pp];
    float charged_mini_iso = (*chargedMiniIsos)[pp];
    float neutral_mini_iso = (*neutralMiniIsos)[pp];
    float jetPtRatio       = (*jetPtRatios)[pp];
    float jetPtRel         = (*jetPtRels)[pp];
    float jetNDauCharged   = (*jetNDauChargeds)[pp];
    float jetBTagCSV       = (*jetBTagCSVs)[pp];
    float ecalIso          = probe.ecalPFClusterIso();
    float hcalIso          = probe.hcalPFClusterIso();
    float trackIso         = probe.dr03TkSumPt();
    int missingInnerHits   = probe.gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS);

    double CorrectedTerm = rho*effectiveAreas_.getEffectiveArea(probe.superCluster()->eta());
    double pfRelIso = (probe.pfIsolationVariables().sumChargedHadronPt + std::max(0.0, probe.pfIsolationVariables().sumNeutralHadronEt + probe.pfIsolationVariables().sumPhotonEt - CorrectedTerm))/probe.pt();

    pt             = pp->pt();
    eta            = pp->eta();
    trackMult      = jetNDauCharged;
    miniIsoCharged = charged_mini_iso;
    miniIsoNeutral = neutral_mini_iso;
    relIso0p3      = pfRelIso;
    ptrel          = jetPtRel;
    ptratio        = TMath::Min(jetPtRatio,(float)1.5);
    jetbtagCSV     = TMath::Max(jetBTagCSV,(float)0.);
    sip3d          = sip3d;
    eleMVA         = mva;

    float leptonMva = readerEle->EvaluateMVA( "BDTG method" );

    sip3dValues.push_back(sip3d);
    ecalIsoValues.push_back(ecalIso);
    hcalIsoValues.push_back(hcalIso);
    trackIsoValues.push_back(trackIso);
    missingInnerHitsValues.push_back(missingInnerHits);

    bool mytight = PassCutBased(probe, dxy, dz, missingInnerHits, 3) and pfRelIso < (probe.isEB()? 0.0588 :  0.0571 );
    if(tight != mytight) std::cout << "WARNING: Cutbased-id is not up to date anymore, please check" << std::endl;

    passWorkingPoints["ConvVeto"].push_back(         probe.passConversionVeto());
    passWorkingPoints["MVAVLooseFO"].push_back(      PassMVAVLooseFOIDEmu(pp->pt(), mva, std::abs(probe.superCluster()->eta())));
    passWorkingPoints["MVAVLoose"].push_back(        PassMVAVLoose(       pp->pt(), mva, std::abs(probe.superCluster()->eta())));
    passWorkingPoints["MVATight"].push_back(         PassMVATight(        pp->pt(), mva, std::abs(probe.superCluster()->eta())));
    passWorkingPoints["MVAWP80"].push_back(          mvaWP80);
    passWorkingPoints["MVAWP90"].push_back(          mvaWP90);
    passWorkingPoints["POGIP2D"].push_back(          PassPOGIP2D(dxy, dz, probe.isEE()));
    passWorkingPoints["LooseIP2D"].push_back(        PassLooseIP2D(dxy, dz));
    passWorkingPoints["TightIP2D"].push_back(        PassTightIP2D(dxy, dz));
    passWorkingPoints["TightIP3D"].push_back(        std::abs(sip3d) < 4.);
    passWorkingPoints["SIP3D4"].push_back(           std::abs(sip3d) < 4.);
    passWorkingPoints["SIP3D8"].push_back(           std::abs(sip3d) < 8.);
    passWorkingPoints["Mini"].push_back(             mini_iso < 0.1);
    passWorkingPoints["Mini2"].push_back(            mini_iso < 0.2);
    passWorkingPoints["Mini4"].push_back(            mini_iso < 0.4);
    passWorkingPoints["RelIso012"].push_back(        pfRelIso < 0.12);
    passWorkingPoints["RelIso010"].push_back(        pfRelIso < 0.10);
    passWorkingPoints["RelIsoCBL"].push_back(        pfRelIso < (probe.isEB() ? 0.0994 : 0.107));
    passWorkingPoints["triggerEmu"].push_back(       triggerEmu);
    passWorkingPoints["IDEmuSpring15"].push_back(    PassIDEmu(probe));
    passWorkingPoints["IDEmuDoubleEG"].push_back(    PassIDEmuDoubleEG(probe));
    passWorkingPoints["ISOEmuSpring15"].push_back(   PassISOEmu(probe));
    passWorkingPoints["Charge"].push_back(           probe.isGsfCtfScPixChargeConsistent());
    passWorkingPoints["IHit0"].push_back(            missingInnerHits == 0);
    passWorkingPoints["IHit1"].push_back(            missingInnerHits <= 1);
    passWorkingPoints["MultiIsoM"].push_back(        PassMultiIso("M",  mini_iso, jetPtRatio, jetPtRel));
    passWorkingPoints["MultiIsoT"].push_back(        PassMultiIso("T",  mini_iso, jetPtRatio, jetPtRel));
    passWorkingPoints["MultiIsoVT"].push_back(       PassMultiIso("VT", mini_iso, jetPtRatio, jetPtRel));
    passWorkingPoints["LeptonMvaL"].push_back(       PassLeptonMva("L", leptonMva));
    passWorkingPoints["LeptonMvaM"].push_back(       PassLeptonMva("M",  leptonMva));
    passWorkingPoints["LeptonMvaT"].push_back(       PassLeptonMva("T", leptonMva));
    passWorkingPoints["CutBasedV"].push_back(        PassCutBased(probe, dxy, dz, missingInnerHits, 0));
    passWorkingPoints["CutBasedL"].push_back(        PassCutBased(probe, dxy, dz, missingInnerHits, 1));
    passWorkingPoints["CutBasedM"].push_back(        PassCutBased(probe, dxy, dz, missingInnerHits, 2));
    passWorkingPoints["CutBasedT"].push_back(        PassCutBased(probe, dxy, dz, missingInnerHits, 3));
    passWorkingPoints["CutBasedSpring15V"].push_back(PassCutBasedSpring15(probe, dxy, dz, missingInnerHits, 0));
    passWorkingPoints["CutBasedSpring15L"].push_back(PassCutBasedSpring15(probe, dxy, dz, missingInnerHits, 1));
    passWorkingPoints["CutBasedSpring15M"].push_back(PassCutBasedSpring15(probe, dxy, dz, missingInnerHits, 2));
    passWorkingPoints["CutBasedSpring15T"].push_back(PassCutBasedSpring15(probe, dxy, dz, missingInnerHits, 3));

    passWorkingPoints["CutBasedVPOGIP2D"].push_back(                         combine(passWorkingPoints, {"CutBasedV", "POGIP2D"}));
    passWorkingPoints["CutBasedLPOGIP2D"].push_back(                         combine(passWorkingPoints, {"CutBasedL", "POGIP2D"}));
    passWorkingPoints["CutBasedMPOGIP2D"].push_back(                         combine(passWorkingPoints, {"CutBasedM", "POGIP2D"}));
    passWorkingPoints["CutBasedTPOGIP2D"].push_back(                         combine(passWorkingPoints, {"CutBasedT", "POGIP2D"}));
    passWorkingPoints["MVAVLooseTightIP2D"].push_back(                       combine(passWorkingPoints, {"MVAVLoose", "TightIP2D"}));
    passWorkingPoints["MVAVLooseFOIDEmuTightIP2D"].push_back(                combine(passWorkingPoints, {"MVAVLooseFO", "IDEmuSpring15", "TightIP2D"}));
    passWorkingPoints["MVATightTightIP2DSIP3D4"].push_back(                  combine(passWorkingPoints, {"MVATight", "TightIP2D", "SIP3D4"}));
    passWorkingPoints["MVATightIDEmuTightIP2DSIP3D4"].push_back(             combine(passWorkingPoints, {"MVATight", "IDEmuSpring15", "TightIP2D", "SIP3D4"}));
    passWorkingPoints["MVATightIDEmuTightIP2DSIP3D4ConvVetoIHit0"].push_back(combine(passWorkingPoints, {"MVATight", "IDEmuSpring15", "TightIP2D", "SIP3D4","ConvVeto","IHit0"}));
    passWorkingPoints["CutBasedStopsDilepton"].push_back(                    combine(passWorkingPoints, {"CutBasedT", "TightIP2D", "SIP3D4"}));
    passWorkingPoints["TTG"].push_back(                                      combine(passWorkingPoints, {"MVAVLoose", "TightIP2D", "SIP3D4", "IDEmuDoubleEG","ConvVeto","IHit0","RelIso012"}));
    passWorkingPoints["ConvVetoIHit1"].push_back(                            combine(passWorkingPoints, {"ConvVeto","IHit1"}));
    passWorkingPoints["ConvVetoIHit0"].push_back(                            combine(passWorkingPoints, {"ConvVeto","IHit0"}));
    passWorkingPoints["MultiIsoTISOEmu"].push_back(                          combine(passWorkingPoints, {"MultiIsoT", "ISOEmuSpring15"}));
    passWorkingPoints["TTZ"].push_back(                                      combine(passWorkingPoints, {"MVAWP90","IDEmuDoubleEG","RelIsoCBL","TightIP2D","SIP3D4"}));
    passWorkingPoints["MVAWP90IDEMuTTZ"].push_back(                          combine(passWorkingPoints, {"MVAWP90","IDEmuDoubleEG"}));
    passWorkingPoints["MVAWP90IDEMuTTZRelIsoCBL"].push_back(                 combine(passWorkingPoints, {"MVAWP90","IDEmuDoubleEG","RelIsoCBL"}));
    passWorkingPoints["TTZ2017"].push_back(                                  combine(passWorkingPoints, {"IDEmuDoubleEG", "LeptonMva2017"}));
    passWorkingPoints["TTZ2017TightCharge"].push_back(                       combine(passWorkingPoints, {"IDEmuDoubleEG", "LeptonMva2017", "Charge", "ConvVeto","IHit0"}));

    bool TTHLoose = PassTTHLoose(probe, dxy, dz, sip3d, mini_iso, missingInnerHits, mva);
//    bool TTHFO    = PassTTHFO(   probe, dxy, dz, sip3d, mini_iso, missingInnerHits, jetBTagCSV, mva, mvaHZZ, jetPtRatio, leptonMva);
    passWorkingPoints["Feb2018Loose"].push_back(TTHLoose);
    passWorkingPoints["Feb2018LeptonMvaL"].push_back(                        combine(passWorkingPoints, {"LeptonMvaL"}));
    passWorkingPoints["Feb2018LeptonMvaM"].push_back(                        combine(passWorkingPoints, {"LeptonMvaM"}));
    passWorkingPoints["Feb2018LeptonMvaT"].push_back(                        combine(passWorkingPoints, {"LeptonMvaT"}));
    passWorkingPoints["RFeb2018LeptonMvaL"].push_back(                       combine(passWorkingPoints, {"Feb2017Loose", "LeptonMvaL"}));
    passWorkingPoints["RFeb2018LeptonMvaM"].push_back(                       combine(passWorkingPoints, {"Feb2017Loose", "LeptonMvaM"}));
    passWorkingPoints["RFeb2018LeptonMvaT"].push_back(                       combine(passWorkingPoints, {"Feb2017Loose", "LeptonMvaT"}));
    passWorkingPoints["TightCharge"].push_back(                              combine(passWorkingPoints, {"Charge", "ConvVeto","IHit0"}));

    ++i;
  }

  Store(iEvent, probes, sip3dValues, "sip3d");
  Store(iEvent, probes, ecalIsoValues, "ecalIso");
  Store(iEvent, probes, hcalIsoValues, "hcalIso");
  Store(iEvent, probes, trackIsoValues, "trackIso");
  Store(iEvent, probes, missingInnerHitsValues, "missIHits");

  for(TString wp : workingPoints){
    Store(iEvent, probes, passWorkingPoints[wp], ("pass" + wp).Data());
  }
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(MyElectronVariableHelper);
