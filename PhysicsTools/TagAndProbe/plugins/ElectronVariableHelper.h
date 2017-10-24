#ifndef _ELECTRONVARIABLEHELPER_H
#define _ELECTRONVARIABLEHELPER_H

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

//#include "DataFormats/L1Trigger/interface/L1EmParticle.h"
//#include "DataFormats/L1Trigger/interface/L1EmParticleFwd.h"
#include "HLTrigger/HLTcore/interface/HLTFilter.h"
#include "DataFormats/L1Trigger/interface/EGamma.h"
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h"
#include "CondFormats/L1TObjects/interface/L1CaloGeometry.h"
#include "CondFormats/DataRecord/interface/L1CaloGeometryRecord.h"

#include "DataFormats/Math/interface/deltaR.h"

template <class T>
class ElectronVariableHelper : public edm::EDProducer {
 public:
  explicit ElectronVariableHelper(const edm::ParameterSet & iConfig);
  virtual ~ElectronVariableHelper() ;
  
  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup) override;

  void Store(edm::Event &iEvent, const edm::Handle<std::vector<T>> &probes,
	                          const std::vector<float> &values, const std::string &name){
    auto valMap = std::make_unique<edm::ValueMap<float>>();
    typename edm::ValueMap<float>::Filler filler(*valMap);
    filler.insert(probes, values.begin(), values.end());
    filler.fill();
    iEvent.put(std::move(valMap), name);
  };


private:
  edm::EDGetTokenT<std::vector<T> > probesToken_;
  edm::EDGetTokenT<reco::VertexCollection> vtxToken_;
  edm::EDGetTokenT<BXVector<l1t::EGamma> > l1EGTkn;
};



template<class T>
ElectronVariableHelper<T>::ElectronVariableHelper(const edm::ParameterSet & iConfig) :
  probesToken_(consumes<std::vector<T> >(iConfig.getParameter<edm::InputTag>("probes"))),
  vtxToken_(consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("vertexCollection"))),
  l1EGTkn(consumes<BXVector<l1t::EGamma> >(iConfig.getParameter<edm::InputTag>("l1EGColl"))) {

  produces<edm::ValueMap<float> >("chi2");
  produces<edm::ValueMap<float> >("dz");
  produces<edm::ValueMap<float> >("dxy");
  produces<edm::ValueMap<float> >("missinghits");
  produces<edm::ValueMap<float> >("l1e");
  produces<edm::ValueMap<float> >("l1et");
  produces<edm::ValueMap<float> >("l1eta");
  produces<edm::ValueMap<float> >("l1phi");
}

template<class T>
ElectronVariableHelper<T>::~ElectronVariableHelper()
{}

template<class T>
void ElectronVariableHelper<T>::produce(edm::Event & iEvent, const edm::EventSetup & iSetup) {

  // read input
  edm::Handle<std::vector<T> > probes;
  edm::Handle<reco::VertexCollection> vtxH;
  
  iEvent.getByToken(probesToken_, probes);
  iEvent.getByToken(vtxToken_, vtxH);
  const reco::VertexRef vtx(vtxH, 0);

  edm::Handle<BXVector<l1t::EGamma> > l1Cands;
  iEvent.getByToken(l1EGTkn, l1Cands);

  // prepare vector for output
  std::vector<float> chi2Vals;
  std::vector<float> dzVals;
  std::vector<float> dxyVals;
  std::vector<float> mhVals;
  std::vector<float> l1EVals;
  std::vector<float> l1EtVals;
  std::vector<float> l1EtaVals;
  std::vector<float> l1PhiVals;

  typename std::vector<T>::const_iterator probe, endprobes = probes->end();

  for (probe = probes->begin(); probe != endprobes; ++probe) {
    
    chi2Vals.push_back(probe->gsfTrack()->normalizedChi2());
    dzVals.push_back(probe->gsfTrack()->dz(vtx->position()));
    dxyVals.push_back(probe->gsfTrack()->dxy(vtx->position()));
    mhVals.push_back(float(probe->gsfTrack()->hitPattern().numberOfHits(reco::HitPattern::MISSING_INNER_HITS)));

    float l1e = 999999.;    
    float l1et = 999999.;
    float l1eta = 999999.;
    float l1phi = 999999.;
    float dRmin = 0.3;
    for (std::vector<l1t::EGamma>::const_iterator l1Cand = l1Cands->begin(0); l1Cand != l1Cands->end(0); ++l1Cand) {

      float dR = deltaR(l1Cand->eta(), l1Cand->phi() , probe->superCluster()->eta(), probe->superCluster()->phi());
      if (dR < dRmin) {
	dRmin = dR;
	l1e = l1Cand->energy();
	l1et = l1Cand->et();
        l1eta = l1Cand->eta();
        l1phi = l1Cand->phi();
      }
    }

    l1EVals.push_back(l1e);
    l1EtVals.push_back(l1et);
    l1EtaVals.push_back(l1eta);
    l1PhiVals.push_back(l1phi);
  }

  Store(iEvent, probes, chi2Vals,  "chi2");
  Store(iEvent, probes, dzVals,    "dz");
  Store(iEvent, probes, dxyVals,   "dxy");
  Store(iEvent, probes, mhVals,    "missinghits");
  Store(iEvent, probes, l1EVals,   "l1e");
  Store(iEvent, probes, l1EtVals,  "l1et");
  Store(iEvent, probes, l1EtaVals, "l1eta");
  Store(iEvent, probes, l1PhiVals, "l1phi");
}

#endif
