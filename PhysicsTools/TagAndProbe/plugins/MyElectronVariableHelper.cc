#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/L1Trigger/interface/L1EmParticle.h"
#include "DataFormats/L1Trigger/interface/L1EmParticleFwd.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "TMVA/Reader.h"

#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "TMath.h"

namespace{
  typedef bool MyBool;

  template<typename T>
    void Store(edm::Event &iEvent,
	       const edm::Handle<std::vector<pat::Electron> > &probes,
	       const std::vector<T> &values,
	       const std::string &name){
    std::auto_ptr<edm::ValueMap<T> > valMap(new edm::ValueMap<T>());
    typename edm::ValueMap<T>::Filler filler(*valMap);
    filler.insert(probes, values.begin(), values.end());
    filler.fill();
    iEvent.put(valMap, name);
  }

  std::vector<bool> And(const std::vector<bool> &a, std::vector<bool> b){
    size_t min_size = a.size(), max_size = b.size();
    if(a.size() > b.size()){
      size_t temp = min_size;
      min_size = max_size;
      max_size = temp;
    }
    std::vector<bool> result(max_size);
    for(size_t i = 0; i < max_size; ++i){
      if(i < min_size) result.at(i) = a.at(i) && b.at(i);
      else             result.at(i) = false;
    }
    return result;
  }

  bool PassMVAVLooseFO(double mva, double abssceta){
    if(abssceta<0.8)        return mva > -0.7;
    else if(abssceta<1.479) return mva > -0.83;
    else if(abssceta<2.5)   return mva > -0.92;
    else                    return false;
  }

  bool PassMVAVLoose(double mva, double abssceta){
    if(abssceta<0.8)        return mva > -0.16;
    else if(abssceta<1.479) return mva > -0.65;
    else if(abssceta<2.5)   return mva > -0.74;
    else                    return false;
  }

  bool PassMVATight(double mva, double abssceta){
    if(abssceta<0.8)        return mva > 0.87;
    else if(abssceta<1.479) return mva > 0.60;
    else if(abssceta<2.5)   return mva > 0.17;
    else                    return false;
  }

  bool PassMVAWP80(double mva, double abssceta){
    if(abssceta<0.8)        return mva > 0.988153;
    else if(abssceta<1.479) return mva > 0.967910;
    else if(abssceta<2.5)   return mva > 0.841729;
    else                    return false;
  }

  bool PassMVAWP90(double mva, double abssceta){
    if(abssceta<0.8)        return mva >  0.972153;
    else if(abssceta<1.479) return mva >  0.922126;
    else if(abssceta<2.5)   return mva >  0.610764;
    else                    return false;
  }

  bool PassTightIP2D(double dxy, double dz){
    return fabs(dxy) < 0.05 && fabs(dz) < 0.1;
  }

  bool PassIDEmu(const pat::Electron &ele){
    if(ele.isEB()){
      return ele.sigmaIetaIeta() < 0.011
	&& ele.hadronicOverEm() < 0.08
	&& fabs(ele.deltaEtaSuperClusterTrackAtVtx()) < 0.01
	&& fabs(ele.deltaPhiSuperClusterTrackAtVtx()) < 0.04
	&& fabs(1./ele.ecalEnergy() - ele.eSuperClusterOverP()/ele.ecalEnergy()) < 0.01;
    }else if(ele.isEE()){
      return ele.sigmaIetaIeta() < 0.031
	&& ele.hadronicOverEm() < 0.08
	&& fabs(ele.deltaEtaSuperClusterTrackAtVtx()) < 0.01
	&& fabs(ele.deltaPhiSuperClusterTrackAtVtx()) < 0.08
	&& fabs(1./ele.ecalEnergy() - ele.eSuperClusterOverP()/ele.ecalEnergy()) < 0.01;
    }else{
      return false;
    }
  }

  bool PassISOEmu(const pat::Electron &ele){
    return ele.ecalPFClusterIso() / ele.pt() < 0.45
      && ele.hcalPFClusterIso() / ele.pt() < 0.25
      && ele.dr03TkSumPt() / ele.pt() < 0.2;
  }

  // CMS coding rule number 1: be careful with POG recommended packages, especially when they were able to transform something
  // simple as a cut based id into a web of hundreds of python config files and are using bad coding standards
  // Therefore, simply implement the cut based id in a much more transparant way in the following 30 lines
  // Furthermore, we do not want the isolation cut, and you really don't want to mess with the EGamma code
  // Cuts based on: https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2#Spring15_selection_25ns
  // Spring15, 25ns		         Veto B    Loose B   Medium B  Tight B    Veto E   Loose E   Medium E  Tight E
  std::vector<float> maxSigmaIetaIeta = {0.0114,   0.0103,   0.0101,   0.0101,    0.0352,  0.0301,   0.0283,   0.0279};
  std::vector<float> maxDEtaIn        = {0.0152,   0.0105,   0.0103,   0.00926,   0.0113,  0.00814,  0.00733,  0.00724};
  std::vector<float> maxDPhiIn        = {0.216,    0.115,    0.0336,   0.0336,    0.237,   0.182,    0.114,    0.0918};
  std::vector<float> maxHOverE        = {0.181,    0.104,    0.0876,   0.0597,    0.116,   0.0897,   0.0678,   0.0615};
  std::vector<float> maxOoEmooP       = {0.207,    0.102,    0.0174,   0.012,     0.174,   0.126,    0.0898,   0.00999};
  std::vector<float> maxd0            = {0.0564,   0.0261,   0.0118,   0.0111,    0.222,   0.118,    0.0739,   0.0351};
  std::vector<float> maxdz            = {0.472,    0.41,     0.373,    0.0466,    0.921,   0.822,    0.602,    0.417};
  std::vector<int>   maxMissingHits   = {2,        2,        2,        2,         3,       1,        1,        1};
  std::vector<bool>  convVeto         = {true,     true,     true,     true,      true,    true,     true,     true};

  bool PassCutBased(const pat::Electron &ele, float dxy, float dz, int missingHits, int level){
    if(ele.isEB())      level = level;
    else if(ele.isEE()) level = level + 4;
    else return false;

    float eInvMinusPInv = std::abs(1.0 - ele.eSuperClusterOverP())/ele.ecalEnergy();

    if(ele.full5x5_sigmaIetaIeta()               >= maxSigmaIetaIeta[level]) return false;
    if(abs(ele.deltaEtaSuperClusterTrackAtVtx()) >= maxDEtaIn[level])        return false;
    if(abs(ele.deltaPhiSuperClusterTrackAtVtx()) >= maxDPhiIn[level])        return false;
    if(ele.hadronicOverEm()                      >= maxHOverE[level])        return false;
    if(eInvMinusPInv                             >= maxOoEmooP[level])       return false;
    if(abs(dxy)                                  >= maxd0[level])            return false;
    if(abs(dz)                                   >= maxdz[level])            return false;
    if(missingHits                               >  maxMissingHits[level])   return false;
    if(convVeto[level] and not ele.passConversionVeto())                     return false;

    return true;
  }


  // On request of Deniz for her TTZ analysis, based on the (as usual to CMS standards) horrible code given here: https://github.com/peruzzim/cmgtools-lite/blob/76X_for2016basis/TTHAnalysis/python/tools/functionsTTH.py#L10-L20
  bool PassCutBasedTTZ(const pat::Electron &ele, bool passedCutBasedM){
    if(!passedCutBasedM) return false; // This is on top of the medium working point
    float eInvMinusPInv = ele.ecalEnergy() > 0 ? (1.0/ele.ecalEnergy() - ele.eSuperClusterOverP()/ele.ecalEnergy()) : 9e9;
    if(ele.isEB()){
      if (ele.hadronicOverEm() >= 0.10)                    return false;
      if (abs(ele.deltaEtaSuperClusterTrackAtVtx())>=0.01) return false;
      if (abs(ele.deltaPhiSuperClusterTrackAtVtx())>=0.04) return false;
      if (eInvMinusPInv<=-0.05)                            return false;
      if (eInvMinusPInv>=0.01)                             return false;
      if (ele.full5x5_sigmaIetaIeta()>=0.011)              return false;
      return true;

    } else if(ele.isEE()){
      if (ele.hadronicOverEm() >= 0.07)                     return false;
      if (abs(ele.deltaEtaSuperClusterTrackAtVtx())>=0.008) return false;
      if (abs(ele.deltaPhiSuperClusterTrackAtVtx())>=0.07)  return false;
      if (eInvMinusPInv<=-0.05)                             return false;
      if (eInvMinusPInv>=0.005)                             return false;
      if (ele.full5x5_sigmaIetaIeta()>=0.03)                return false;
      return true;
    } else return false;
  }

//bool PassMultiIsoVL(double mini_iso, double jetPtRatio, double jetPtRel){  return mini_iso < 0.25 && (jetPtRatio > 0.67 || jetPtRel > 4.4);}
//bool PassMultiIsoL( double mini_iso, double jetPtRatio, double jetPtRel){  return mini_iso < 0.20 && (jetPtRatio > 0.69 || jetPtRel > 6.0);}
  bool PassMultiIsoM( double mini_iso, double jetPtRatio, double jetPtRel){  return mini_iso < 0.16 && (jetPtRatio > 0.76 || jetPtRel > 7.2);}
  bool PassMultiIsoT( double mini_iso, double jetPtRatio, double jetPtRel){  return mini_iso < 0.12 && (jetPtRatio > 0.80 || jetPtRel > 7.2);}
  bool PassMultiIsoVT(double mini_iso, double jetPtRatio, double jetPtRel){  return mini_iso < 0.09 && (jetPtRatio > 0.84 || jetPtRel > 7.2);}

//bool PassLeptonMvaVL(double mva){ return mva > -0.3;}
//bool PassLeptonMvaL(double mva){  return mva > 0.25;}
  bool PassLeptonMvaM(double mva){  return mva > 0.5;}
//bool PassLeptonMvaT(double mva){  return mva > 0.65;}
  bool PassLeptonMvaVT(double mva){ return mva > 0.75;}
//bool PassLeptonMvaET(double mva){ return mva > 0.85;}
}



class MyElectronVariableHelper : public edm::EDProducer {
public:
  explicit MyElectronVariableHelper(const edm::ParameterSet & iConfig);
  virtual ~MyElectronVariableHelper() ;
  
  virtual void beginJob();
  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) override;
  
private:
  edm::EDGetTokenT<std::vector<pat::Electron> > probesToken_;
  edm::EDGetTokenT<edm::View<reco::Candidate> > probesViewToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > mvaToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > dxyToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > dzToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > miniIsoToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > chargedMiniIsoToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > neutralMiniIsoToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > jetPtRatioToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > jetPtRelToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > jetNDauChargedToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > jetBTagCSVToken_;
  Float_t LepGood_pt, LepGood_eta, LepGood_jetNDauChargedMVASel,
    LepGood_miniRelIsoCharged, LepGood_miniRelIsoNeutral,
    LepGood_jetPtRelv2, LepGood_jetPtRatio,
    LepGood_jetBTagCSV,
    LepGood_sip3d, LepGood_dxy, LepGood_dz,
    LepGood_mvaIdSpring15;

  TMVA::Reader *readerEle;
};

MyElectronVariableHelper::MyElectronVariableHelper(const edm::ParameterSet & iConfig) :
  probesToken_(        consumes<std::vector<pat::Electron>>(iConfig.getParameter<edm::InputTag>("probes"))),
  probesViewToken_(    consumes<edm::View<reco::Candidate>>(iConfig.getParameter<edm::InputTag>("probes"))),
  mvaToken_(           consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("mvas"))),
  dxyToken_(           consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("dxy"))),
  dzToken_(            consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("dz"))),
  miniIsoToken_(       consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("miniIso"))),
  chargedMiniIsoToken_(consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("chargedMiniIso"))),
  neutralMiniIsoToken_(consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("neutralMiniIso"))),
  jetPtRatioToken_(    consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetPtRatio"))),
  jetPtRelToken_(      consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetPtRel"))),
  jetNDauChargedToken_(consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetNDauCharged"))),
  jetBTagCSVToken_(    consumes<edm::ValueMap<float>>(      iConfig.getParameter<edm::InputTag>("jetBTagCSV"))){
  
    produces<edm::ValueMap<float> >("sip3d");
    produces<edm::ValueMap<float> >("ecalIso");
    produces<edm::ValueMap<float> >("hcalIso");
    produces<edm::ValueMap<float> >("trackIso");
    produces<edm::ValueMap<int> >("missIHits");
    produces<edm::ValueMap<MyBool> >("passConvVeto");
    produces<edm::ValueMap<MyBool> >("passMVAVLooseFO");
    produces<edm::ValueMap<MyBool> >("passMVAVLoose");
    produces<edm::ValueMap<MyBool> >("passMini");
    produces<edm::ValueMap<MyBool> >("passMini2");
    produces<edm::ValueMap<MyBool> >("passMini4");
    produces<edm::ValueMap<MyBool> >("passMVAVLooseMini");
    produces<edm::ValueMap<MyBool> >("passMVAVLooseMini2");
    produces<edm::ValueMap<MyBool> >("passMVAVLooseMini4");
    produces<edm::ValueMap<MyBool> >("passMVATight");
    produces<edm::ValueMap<MyBool> >("passMVAWP80");
    produces<edm::ValueMap<MyBool> >("passMVAWP90");
    produces<edm::ValueMap<MyBool> >("passTightIP2D");
    produces<edm::ValueMap<MyBool> >("passTightIP3D");
    produces<edm::ValueMap<MyBool> >("passIDEmu");
    produces<edm::ValueMap<MyBool> >("passISOEmu");
    produces<edm::ValueMap<MyBool> >("passCharge");
    produces<edm::ValueMap<MyBool> >("passIHit0");
    produces<edm::ValueMap<MyBool> >("passIHit1");
    produces<edm::ValueMap<MyBool> >("passLoose2D");
    produces<edm::ValueMap<MyBool> >("passFOID2D");
    produces<edm::ValueMap<MyBool> >("passTight2D3D");
    produces<edm::ValueMap<MyBool> >("passTightID2D3D");
    produces<edm::ValueMap<MyBool> >("passConvIHit0");
    produces<edm::ValueMap<MyBool> >("passTightConvIHit0");
    produces<edm::ValueMap<MyBool> >("passConvIHit1");
    produces<edm::ValueMap<MyBool> >("passConvIHit0Chg");
    produces<edm::ValueMap<MyBool> >("passMultiIsoM");
    produces<edm::ValueMap<MyBool> >("passMultiIsoT");
    produces<edm::ValueMap<MyBool> >("passMultiIsoVT");
    produces<edm::ValueMap<MyBool> >("passMultiIsoEmu");
    produces<edm::ValueMap<MyBool> >("passLeptonMvaM");
    produces<edm::ValueMap<MyBool> >("passLeptonMvaVT");
    produces<edm::ValueMap<MyBool> >("passCutBasedVeto");
    produces<edm::ValueMap<MyBool> >("passCutBasedLoose");
    produces<edm::ValueMap<MyBool> >("passCutBasedMedium");
    produces<edm::ValueMap<MyBool> >("passCutBasedTight");
    produces<edm::ValueMap<MyBool> >("passCutBasedMediumMini");
    produces<edm::ValueMap<MyBool> >("passCutBasedTightMini");
    produces<edm::ValueMap<MyBool> >("passCutBasedTTZ");
    produces<edm::ValueMap<MyBool> >("passCutBasedIllia");
    produces<edm::ValueMap<MyBool> >("passCutBasedStopsDilepton");
    produces<edm::ValueMap<MyBool> >("passLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04");
    produces<edm::ValueMap<MyBool> >("passLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04");
}

MyElectronVariableHelper::~MyElectronVariableHelper(){
}

void MyElectronVariableHelper::beginJob(){
    readerEle = new TMVA::Reader( "!Color:!Silent" );

    readerEle->AddVariable( "LepGood_pt", &LepGood_pt );
    readerEle->AddVariable( "LepGood_eta", &LepGood_eta );
    readerEle->AddVariable( "LepGood_jetNDauChargedMVASel", &LepGood_jetNDauChargedMVASel );
    readerEle->AddVariable( "LepGood_miniRelIsoCharged", &LepGood_miniRelIsoCharged );
    readerEle->AddVariable( "LepGood_miniRelIsoNeutral", &LepGood_miniRelIsoNeutral );
    readerEle->AddVariable( "LepGood_jetPtRelv2", &LepGood_jetPtRelv2 );
    readerEle->AddVariable( "min(LepGood_jetPtRatiov2,1.5)", &LepGood_jetPtRatio );
    readerEle->AddVariable( "max(LepGood_jetBTagCSV,0)", &LepGood_jetBTagCSV );
    readerEle->AddVariable( "LepGood_sip3d", &LepGood_sip3d );  
    readerEle->AddVariable( "log(abs(LepGood_dxy))", &LepGood_dxy );  
    readerEle->AddVariable( "log(abs(LepGood_dz))", &LepGood_dz );  
    readerEle->AddVariable( "LepGood_mvaIdSpring15", &LepGood_mvaIdSpring15 );
    edm::FileInPath *fip = new edm::FileInPath("PhysicsTools/TagAndProbe/data/forMoriond16_el_sigTTZ_bkgTT_BDTG.weights.xml");
    readerEle->BookMVA( "BDTG method", fip->fullPath().c_str());
}


void MyElectronVariableHelper::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {
  // read input
  edm::Handle<std::vector<pat::Electron>> probes;      iEvent.getByToken(probesToken_,         probes);
  edm::Handle<edm::View<reco::Candidate>> probes_view; iEvent.getByToken(probesViewToken_,     probes_view);
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

  // prepare vector for output
  std::vector<float> sip3dValues;
  std::vector<float> ecalIsoValues;
  std::vector<float> hcalIsoValues;
  std::vector<float> trackIsoValues;
  std::vector<int> missingInnerHitsValues;
  std::vector<MyBool> passConversionVeto;
  std::vector<MyBool> passMVAVLooseFO;
  std::vector<MyBool> passMVAVLoose;
  std::vector<MyBool> passMVAVLooseMini;
  std::vector<MyBool> passMVAVLooseMini2;
  std::vector<MyBool> passMVAVLooseMini4;
  std::vector<MyBool> passMVATight;
  std::vector<MyBool> passMVAWP80;
  std::vector<MyBool> passMVAWP90;
  std::vector<MyBool> passTightIP2D;
  std::vector<MyBool> passSIP3D4;
  std::vector<MyBool> passSIP3D8;
  std::vector<MyBool> passMiniIso1;
  std::vector<MyBool> passMiniIso2;
  std::vector<MyBool> passMiniIso4;
  std::vector<MyBool> passIDEmu;
  std::vector<MyBool> passISOEmu;
  std::vector<MyBool> passCharge;
  std::vector<MyBool> passIHit0;
  std::vector<MyBool> passIHit1;
  std::vector<MyBool> passMultiIsoM;
  std::vector<MyBool> passMultiIsoT;
  std::vector<MyBool> passMultiIsoVT;
  std::vector<MyBool> passLeptonMvaM;
  std::vector<MyBool> passLeptonMvaVT;
  std::vector<MyBool> passCutBasedLoose;
  std::vector<MyBool> passCutBasedMedium;
  std::vector<MyBool> passCutBasedVeto;
  std::vector<MyBool> passCutBasedTight;
  std::vector<MyBool> passCutBasedTTZ;

  size_t i = 0;
  for(const auto &probe: *probes){
    edm::RefToBase<reco::Candidate> pp = probes_view->refAt(i);

    float ip3d             = probe.dB(pat::Electron::PV3D);
    float ip3d_err         = probe.edB(pat::Electron::PV3D);
    float sip3d            = ip3d/ip3d_err;
    float mva              = (*mvas)[pp];
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

    LepGood_pt                   = pp->pt();
    LepGood_eta                  = pp->eta();
    LepGood_jetNDauChargedMVASel = jetNDauCharged;
    LepGood_miniRelIsoCharged    = charged_mini_iso;
    LepGood_miniRelIsoNeutral    = neutral_mini_iso;
    LepGood_jetPtRelv2           = jetPtRel;
    LepGood_jetPtRatio           = TMath::Min(jetPtRatio,(float)1.5);
    LepGood_jetBTagCSV           = TMath::Max(jetBTagCSV,(float)0.);
    LepGood_sip3d                = sip3d;
    LepGood_dxy                  = TMath::Log(fabs(dxy));
    LepGood_dz                   = TMath::Log(fabs(dz));
    LepGood_mvaIdSpring15        = mva;

    float leptonMva             = readerEle->EvaluateMVA( "BDTG method" );

    float passCutBasedV = PassCutBased(probe, dxy, dz, missingInnerHits, 0);
    float passCutBasedL = PassCutBased(probe, dxy, dz, missingInnerHits, 1);
    float passCutBasedM = PassCutBased(probe, dxy, dz, missingInnerHits, 2);
    float passCutBasedT = PassCutBased(probe, dxy, dz, missingInnerHits, 3);


    sip3dValues.push_back(sip3d);
    ecalIsoValues.push_back(ecalIso);
    hcalIsoValues.push_back(hcalIso);
    trackIsoValues.push_back(trackIso);
    missingInnerHitsValues.push_back(missingInnerHits);
    passConversionVeto.push_back(probe.passConversionVeto());
    passMVAVLooseFO.push_back(PassMVAVLooseFO(mva, fabs(probe.superCluster()->eta())));
    passMVAVLoose.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())));
    passMVAVLooseMini.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())) && mini_iso<0.1);
    passMVAVLooseMini2.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())) && mini_iso<0.2);
    passMVAVLooseMini4.push_back(PassMVAVLoose(mva, fabs(probe.superCluster()->eta())) && mini_iso<0.4);
    passMVATight.push_back(PassMVATight(mva, fabs(probe.superCluster()->eta())));
    passMVAWP80.push_back(PassMVAWP80(mva, fabs(probe.superCluster()->eta())));
    passMVAWP90.push_back(PassMVAWP90(mva, fabs(probe.superCluster()->eta())));
    passTightIP2D.push_back(PassTightIP2D(dxy, dz));
    passSIP3D4.push_back(fabs(sip3d) < 4.);
    passSIP3D8.push_back(fabs(sip3d) < 8.);
    passMiniIso1.push_back(mini_iso < 0.1);
    passMiniIso2.push_back(mini_iso < 0.2);
    passMiniIso4.push_back(mini_iso < 0.4);
    passIDEmu.push_back(PassIDEmu(probe));
    passISOEmu.push_back(PassISOEmu(probe));
    passCharge.push_back(probe.isGsfCtfScPixChargeConsistent());
    passIHit0.push_back(missingInnerHits == 0);
    passIHit1.push_back(missingInnerHits <= 1);
    passMultiIsoM.push_back(PassMultiIsoM(mini_iso, jetPtRatio, jetPtRel));
    passMultiIsoT.push_back(PassMultiIsoT(mini_iso, jetPtRatio, jetPtRel));
    passMultiIsoVT.push_back(PassMultiIsoVT(mini_iso, jetPtRatio, jetPtRel));
    passLeptonMvaM.push_back(PassLeptonMvaM(leptonMva));
    passLeptonMvaVT.push_back(PassLeptonMvaVT(leptonMva));
    passCutBasedVeto.push_back(passCutBasedV);
    passCutBasedLoose.push_back(passCutBasedL);
    passCutBasedMedium.push_back(passCutBasedM);
    passCutBasedTight.push_back(passCutBasedT);
    passCutBasedTTZ.push_back(PassCutBasedTTZ(probe, passCutBasedM));
    ++i;
  }

  // convert into ValueMap and store
  // If time after ICHEP, this should get cleaned up and re-checked because all the code and boookkeeping is horrible
  Store(iEvent, probes, sip3dValues, "sip3d");
  Store(iEvent, probes, ecalIsoValues, "ecalIso");
  Store(iEvent, probes, hcalIsoValues, "hcalIso");
  Store(iEvent, probes, trackIsoValues, "trackIso");
  Store(iEvent, probes, missingInnerHitsValues, "missIHits");
  Store(iEvent, probes, passConversionVeto, "passConvVeto");
  Store(iEvent, probes, passMVAVLooseFO, "passMVAVLooseFO");
  Store(iEvent, probes, passMVAVLoose, "passMVAVLoose");
  Store(iEvent, probes, passMiniIso1, "passMini");
  Store(iEvent, probes, passMiniIso2, "passMini2");
  Store(iEvent, probes, passMiniIso4, "passMini4");
  Store(iEvent, probes, passMVAVLooseMini, "passMVAVLooseMini");
  Store(iEvent, probes, passMVAVLooseMini2, "passMVAVLooseMini2");
  Store(iEvent, probes, passMVAVLooseMini4, "passMVAVLooseMini4");
  Store(iEvent, probes, passMVATight, "passMVATight");
  Store(iEvent, probes, passMVAWP80, "passMVAWP80");
  Store(iEvent, probes, passMVAWP90, "passMVAWP90");
  Store(iEvent, probes, passTightIP2D, "passTightIP2D");
  Store(iEvent, probes, passSIP3D4, "passTightIP3D");
  Store(iEvent, probes, passIDEmu, "passIDEmu");
  Store(iEvent, probes, passISOEmu, "passISOEmu");
  Store(iEvent, probes, passCharge, "passCharge"); 
  Store(iEvent, probes, passIHit0, "passIHit0");
  Store(iEvent, probes, passIHit1, "passIHit1");
  Store(iEvent, probes, And(passMVAVLoose, passTightIP2D), "passLoose2D");
  Store(iEvent, probes, And(And(passMVAVLooseFO, passIDEmu), passTightIP2D), "passFOID2D");
  Store(iEvent, probes, And(And(passMVATight, passTightIP2D), passSIP3D4), "passTight2D3D");
  Store(iEvent, probes, And(And(passCutBasedTight, passTightIP2D), passSIP3D4), "passCutBasedStopsDilepton");
  Store(iEvent, probes,	And(And(And(passMVATight, passIDEmu), passTightIP2D), passSIP3D4), "passTightID2D3D");
  Store(iEvent, probes, And(passConversionVeto, passIHit1), "passConvIHit1");
  Store(iEvent, probes, And(passConversionVeto, passIHit0), "passConvIHit0");
  Store(iEvent, probes, And(And(And(And(passMVATight, passTightIP2D), passSIP3D4), passConversionVeto), passIHit0), "passTightConvIHit0");
  Store(iEvent, probes, And(And(passConversionVeto, passIHit0), passCharge), "passConvIHit0Chg");
  Store(iEvent, probes, passMultiIsoM, "passMultiIsoM");
  Store(iEvent, probes, passMultiIsoT, "passMultiIsoT");
  Store(iEvent, probes, passMultiIsoVT, "passMultiIsoVT");
  Store(iEvent, probes, And(passMultiIsoT, passISOEmu), "passMultiIsoEmu");
  Store(iEvent, probes, passLeptonMvaM, "passLeptonMvaM");
  Store(iEvent, probes, passLeptonMvaVT, "passLeptonMvaVT");
  Store(iEvent, probes, passCutBasedVeto, "passCutBasedVeto");
  Store(iEvent, probes, passCutBasedMedium, "passCutBasedMedium");
  Store(iEvent, probes, And(passCutBasedMedium, passMiniIso1), "passCutBasedMediumMini");
  Store(iEvent, probes, passCutBasedLoose, "passCutBasedLoose");
  Store(iEvent, probes, passCutBasedTight, "passCutBasedTight");
  Store(iEvent, probes, And(passCutBasedTight, passMiniIso1), "passCutBasedTightMini");
  Store(iEvent, probes, And(And(passCutBasedTTZ, passTightIP2D), passSIP3D4), "passCutBasedTTZ");
  Store(iEvent, probes, And(And(And(passCutBasedTTZ, passTightIP2D), passSIP3D4), passCharge), "passCutBasedIllia");
  Store(iEvent, probes, And(And(And(And(passLeptonMvaVT, passIDEmu), passTightIP2D), passSIP3D8), passMiniIso4), "passLeptonMvaVTIDEmuTightIP2DSIP3D8miniIso04");
  Store(iEvent, probes, And(And(And(And(passLeptonMvaM,  passIDEmu), passTightIP2D), passSIP3D8), passMiniIso4), "passLeptonMvaMIDEmuTightIP2DSIP3D8miniIso04");
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(MyElectronVariableHelper);
