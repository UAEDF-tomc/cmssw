#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/View.h"

#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"

typedef edm::View<reco::Candidate> CandView;

class IsolationSum : public edm::EDProducer{
public:
  explicit IsolationSum(const edm::ParameterSet &pset);
  ~IsolationSum();

private:
  virtual void produce(edm::Event &event, const edm::EventSetup &setup) override;
  template <typename T> void putInEvent(std::string, const edm::Handle<CandView>&, std::vector<T>&, edm::Event&);
  double getPFIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
                        auto ptcl,  
                        double r_iso_min, double r_iso_max, double kt_scale,
                        bool charged_only);

  EffectiveAreas effectiveAreas_;
  edm::EDGetTokenT<CandView> probesToken_;
  edm::EDGetTokenT<pat::PackedCandidateCollection> candToken_;
  edm::EDGetTokenT<double> rhoToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > chadToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > nhadToken_;
  edm::EDGetTokenT<edm::ValueMap<float> > phoToken_;
  double minRadius_, maxRadius_;
  double ktScale_;
  double radius_;
  double activityRadius_;
  bool isRelativeIso_;
};

IsolationSum::IsolationSum(const edm::ParameterSet &pset):
  effectiveAreas_((pset.getParameter<edm::FileInPath>("effAreasConfigFile")).fullPath()),
  probesToken_(consumes<CandView>(pset.getParameter<edm::InputTag>("probes"))),
  candToken_(consumes<pat::PackedCandidateCollection>(pset.getParameter<edm::InputTag>("candidates"))),
  rhoToken_(consumes<double>(pset.getParameter<edm::InputTag>("rho"))),
  chadToken_(consumes<edm::ValueMap<float> >(pset.getParameter<edm::InputTag>("chadIso"))),
  nhadToken_(consumes<edm::ValueMap<float> >(pset.getParameter<edm::InputTag>("nhadIso"))),
  phoToken_(consumes<edm::ValueMap<float> >(pset.getParameter<edm::InputTag>("phoIso"))),
  minRadius_(pset.existsAs<double>("minRadius") ? pset.getParameter<double>("minRadius") : -1.),
  maxRadius_(pset.existsAs<double>("maxRadius") ? pset.getParameter<double>("maxRadius") : -1.),
  ktScale_(pset.existsAs<double>("ktScale")?pset.getParameter<double>("ktScale"):-1.),
  radius_(pset.existsAs<double>("radius") ? pset.getParameter<double>("radius") : -1.),
  activityRadius_(pset.existsAs<double>("actRadius") ? pset.getParameter<double>("actRadius") : -1.),
  isRelativeIso_(pset.getParameter<bool>("isRelativeIso")){
  produces<edm::ValueMap<float> >("sum");
  produces<edm::ValueMap<float> >("charged");
  produces<edm::ValueMap<float> >("neutral");
}

IsolationSum::~IsolationSum(){
}


double IsolationSum::getPFIsolation(edm::Handle<pat::PackedCandidateCollection> pfcands,
                        auto ptcl,  
                        double r_iso_min, double r_iso_max, double kt_scale,
                        bool charged_only) {

    if (ptcl->pt()<5.) return 99999.;

    double deadcone_nh(0.), deadcone_ch(0.), deadcone_ph(0.), deadcone_pu(0.);
    if(ptcl->isElectron()) {
      if (fabs(ptcl->eta())>1.479) {deadcone_ch = 0.015; deadcone_pu = 0.015; deadcone_ph = 0.08;}
    } else if(ptcl->isMuon()) {
      deadcone_ch = 0.0001; deadcone_pu = 0.01; deadcone_ph = 0.01;deadcone_nh = 0.01;  
    } else {
      //deadcone_ch = 0.0001; deadcone_pu = 0.01; deadcone_ph = 0.01;deadcone_nh = 0.01; // maybe use muon cones??
    }

    double iso_nh(0.); double iso_ch(0.); 
    double iso_ph(0.); double iso_pu(0.);
    double ptThresh(0.5);
    if(ptcl->isElectron()) ptThresh = 0;
//    double r_iso = max(r_iso_min,min(r_iso_max, kt_scale/ptcl->pt()));
//
    double r_iso = r_iso_max;
    if (kt_scale/ptcl->pt() < r_iso) r_iso = kt_scale/ptcl->pt();
    if (r_iso_min > r_iso) r_iso = r_iso_min;

    for (const pat::PackedCandidate &pfc : *pfcands) {
      if (abs(pfc.pdgId())<7) continue;

      double dr = deltaR(pfc, *ptcl);
      if (dr > r_iso) continue;
      
      //////////////////  NEUTRALS  /////////////////////////
      if (pfc.charge()==0){
        if (pfc.pt()>ptThresh) {
          /////////// PHOTONS ////////////
          if (abs(pfc.pdgId())==22) {
            if(dr < deadcone_ph) continue;
            iso_ph += pfc.pt();
	    /////////// NEUTRAL HADRONS ////////////
          } else if (abs(pfc.pdgId())==130) {
            if(dr < deadcone_nh) continue;
            iso_nh += pfc.pt();
          }
        }
        //////////////////  CHARGED from PV  /////////////////////////
      } else if (pfc.fromPV()>1){
        if (abs(pfc.pdgId())==211) {
          if(dr < deadcone_ch) continue;
          iso_ch += pfc.pt();
        }
        //////////////////  CHARGED from PU  /////////////////////////
      } else {
        if (pfc.pt()>ptThresh){
          if(dr < deadcone_pu) continue;
          iso_pu += pfc.pt();
        }
      }
    }
    double iso(0.);
    if (charged_only){
      iso = iso_ch;
    } else {
      iso = iso_ph + iso_nh;
      iso -= 0.5*iso_pu;
      if (iso>0) iso += iso_ch;
      else iso = iso_ch;
    }
    iso = iso/ptcl->pt();

    return iso;
}



void IsolationSum::produce(edm::Event &event, const edm::EventSetup &setup){
  edm::Handle<double> rhoHandle;
  edm::Handle<edm::ValueMap<float> > chadHandle, nhadHandle, phoHandle;
  edm::Handle<CandView> probesHandle;
  edm::Handle<pat::PackedCandidateCollection> candHandle;

  event.getByToken(probesToken_, probesHandle);
  event.getByToken(candToken_, candHandle);
  event.getByToken(rhoToken_, rhoHandle);
  event.getByToken(chadToken_, chadHandle);
  event.getByToken(nhadToken_, nhadHandle);
  event.getByToken(phoToken_, phoHandle);

  auto rho = static_cast<float>(*rhoHandle);
  const auto &chadMap = static_cast<edm::ValueMap<float> >(*chadHandle);
  const auto &nhadMap = static_cast<edm::ValueMap<float> >(*nhadHandle);
  const auto &phoMap = static_cast<edm::ValueMap<float> >(*phoHandle);

  std::vector<float> isos(probesHandle->size());
  std::vector<float> chargedIsos(probesHandle->size());
  std::vector<float> neutralIsos(probesHandle->size());

  for(size_t iprobe = 0; iprobe < probesHandle->size(); ++iprobe){
    auto cand = probesHandle->ptrAt(iprobe);
    reco::GsfElectronPtr gsf(cand);
    double absEta = gsf->superCluster()->position().eta();
    double area;
    if(ktScale_>=0. && minRadius_>=0. && maxRadius_>=0.){
      double the_radius = std::max(minRadius_,std::min(maxRadius_,ktScale_/gsf->pt()));
      if(activityRadius_ >= 0.){
	area = activityRadius_*activityRadius_ - the_radius*the_radius;
      }else{
	area = the_radius*the_radius;
      }
      area = std::max(minRadius_*minRadius_,
		      std::min(maxRadius_*maxRadius_,
			       std::pow(static_cast<double>(ktScale_/gsf->pt()),.2)));
    }else if(radius_ >= 0.){
      area = radius_*radius_;
    }else{
      //Give up and just use the standard PF eff. area
      area = 0.3*0.3;
    }
    double effectiveArea = effectiveAreas_.getEffectiveArea(absEta)*area/(0.3*0.3);
    double chad = chadMap[cand];
    double nhad = nhadMap[cand];
    double pho = phoMap[cand];

    isos.at(iprobe)        = chad + std::max(0., nhad+pho-rho*effectiveArea);
    chargedIsos.at(iprobe) = chad;
    neutralIsos.at(iprobe) = std::max(0., nhad+pho-rho*effectiveArea);

    for(auto i : {isos, chargedIsos, neutralIsos}){
      if(isRelativeIso_) i.at(iprobe) /= cand->pt();
    }

    isos.at(iprobe)        = getPFIsolation(candHandle, cand, minRadius_, maxRadius_, ktScale_, false);
    chargedIsos.at(iprobe) = getPFIsolation(candHandle, cand, minRadius_, maxRadius_, ktScale_, true);
    neutralIsos.at(iprobe) = isos.at(iprobe) - neutralIsos.at(iprobe);
  }

  putInEvent("sum",     probesHandle, isos,        event);
  putInEvent("charged", probesHandle, chargedIsos, event);
  putInEvent("neutral", probesHandle, neutralIsos, event);
}

/// Function to put product into event
template <typename T> void IsolationSum::putInEvent(std::string name, const edm::Handle<CandView>& probesHandle, std::vector<T>& product, edm::Event& iEvent){
  std::auto_ptr<edm::ValueMap<T>> out(new edm::ValueMap<T>());
  typename edm::ValueMap<T>::Filler filler(*out);
  filler.insert(probesHandle, product.begin(), product.end());
  filler.fill();
  iEvent.put(out, name);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(IsolationSum);
