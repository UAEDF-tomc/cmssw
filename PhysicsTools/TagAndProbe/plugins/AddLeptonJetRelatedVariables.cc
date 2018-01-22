// system include files
#include <memory>
#include <cmath>
#include <TLorentzVector.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/BTauReco/interface/JetTag.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "JetMETCorrections/JetCorrector/interface/JetCorrector.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/RefVector.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "DataFormats/Math/interface/deltaR.h"

using namespace std;


//
// class declaration
//

class AddLeptonJetRelatedVariables : public edm::EDProducer{
public:
  explicit AddLeptonJetRelatedVariables(const edm::ParameterSet&);
  ~AddLeptonJetRelatedVariables();

  typedef std::vector< edm::FwdPtr<reco::PFCandidate> > PFCollection;
  
private:
  virtual void beginJob();
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob();
  template <typename T> void putInEvent(std::string name, edm::Handle<std::vector<pat::Electron>>& probesHandle, std::vector<T>& product, edm::Event& iEvent);
  
  // ----------auxiliary functions -------------------  
  // ----------member data ---------------------------
  edm::EDGetTokenT<edm::View<reco::Jet>> jetCollectionTag_;
  edm::EDGetTokenT<std::vector<pat::Jet>> jetCollectionTag2_;
  edm::EDGetTokenT<std::vector<pat::Electron>> leptonCollectionTag_;
  edm::EDGetTokenT<reco::JetCorrector> tagL1Corrector_;
  edm::EDGetTokenT<reco::JetCorrector> tagL1L2L3ResCorrector_;
  edm::EDGetTokenT<reco::VertexCollection> vertexes_;
  edm::EDGetTokenT<reco::JetTagCollection> bTagCollectionTag_;
  edm::EDGetTokenT<std::vector<pat::PackedCandidate>> pfCandidates_;


  const double dRmax_;
  const bool subLepFromJetForPtRel_;
};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
AddLeptonJetRelatedVariables::AddLeptonJetRelatedVariables(const edm::ParameterSet& iConfig):
  dRmax_(iConfig.getParameter<double>("dRmax")),
  subLepFromJetForPtRel_(iConfig.getParameter<bool>("subLepFromJetForPtRel"))
{
  edm::InputTag jetcollection = iConfig.getParameter<edm::InputTag>("JetCollection");
  jetCollectionTag_ = consumes<edm::View<reco::Jet>>(jetcollection);

  edm::InputTag jetcollection2 = iConfig.getParameter<edm::InputTag>("JetCollectionWithCSV");
  jetCollectionTag2_ = consumes<std::vector<pat::Jet>>(jetcollection2);

  edm::InputTag leptoncollection = iConfig.getParameter<edm::InputTag>("LeptonCollection");
  leptonCollectionTag_ = consumes<std::vector<pat::Electron>>(leptoncollection);
/*
  edm::InputTag l1Cortag = iConfig.getParameter<edm::InputTag>("L1Corrector");
  tagL1Corrector_ = consumes<reco::JetCorrector>(l1Cortag);

  edm::InputTag l1l2l3ResCortag = iConfig.getParameter<edm::InputTag>("L1L2L3ResCorrector");
  tagL1L2L3ResCorrector_ = consumes<reco::JetCorrector>(l1l2l3ResCortag);
*/
  edm::InputTag pfcandidatecoll = iConfig.getParameter<edm::InputTag>("pfCandidates");
  pfCandidates_ = consumes<std::vector<pat::PackedCandidate>>(pfcandidatecoll);
  
//bTagCollectionTag_ = consumes<reco::JetTagCollection>(edm::InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"));
  
  vertexes_ = consumes<reco::VertexCollection>(edm::InputTag("offlineSlimmedPrimaryVertices")); // only for miniAOD of course

  //now do what ever initialization is needed
  produces<edm::ValueMap<float> >("JetPtRatio");
  produces<edm::ValueMap<float> >("JetPtRel");
  produces<edm::ValueMap<float> >("JetNDauCharged");
  produces<edm::ValueMap<float> >("JetBTagCSV");
}

AddLeptonJetRelatedVariables::~AddLeptonJetRelatedVariables()
{

  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//




// ------------ method called for each event  ------------
void 
AddLeptonJetRelatedVariables::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) 
{
  using namespace edm;

  edm::Handle<std::vector<pat::Jet>> jets;       // This is the fully corrected one
  iEvent.getByToken (jetCollectionTag2_, jets);    

  edm::Handle<edm::View<reco::Jet>> jets2;      // This is the one with L1FastJet 
  iEvent.getByToken (jetCollectionTag_, jets2);    

  edm::Handle<std::vector<pat::Electron>> leptons; iEvent.getByToken (leptonCollectionTag_, leptons);       

  edm::Handle<std::vector<pat::PackedCandidate>> pfCandidates;
  iEvent.getByToken(pfCandidates_, pfCandidates);

  edm::Handle<std::vector<reco::Vertex>> vertices; iEvent.getByToken(vertexes_, vertices);
  auto vertex=*(vertices->begin());

  //Make skimmed "close jet" collection
  std::vector<pat::Jet> selectedJetsAll;
  std::vector<pat::Jet> selectedJetsAll2;
  auto jet2 = jets2->begin();
  for(auto jet = jets->begin(); jet != jets->end(); ++jet, ++jet2){
      if( jet->pt() > 5 && fabs( jet->eta() ) < 3){
        selectedJetsAll.push_back(*jet);
        selectedJetsAll2.push_back(*jet2);
      }
  }



  //Output
  std::vector<float> ptratio,ptrel,nchargeddaughers,btagcsv;
  for(auto lepton = leptons->begin(); lepton != leptons->end(); ++lepton){
    // Find closest selected jet
    unsigned closestIndex = 0;
    for(unsigned j = 1; j < selectedJetsAll.size(); ++j){
        if(reco::deltaR(selectedJetsAll[j], *lepton) < reco::deltaR(selectedJetsAll[closestIndex], *lepton)) closestIndex = j;
    }
    const pat::Jet& jet  = selectedJetsAll[closestIndex];
    const pat::Jet& jet2 = selectedJetsAll2[closestIndex];
    if(selectedJetsAll.size() == 0 || reco::deltaR(jet, *lepton) > 0.4){ //Now includes safeguard for 0 jet events
      ptratio.push_back(1);
      ptrel.push_back(0);
      btagcsv.push_back(0);
      nchargeddaughers.push_back(0);
    } else {
      auto  l1Jet       = jet2.p4();
      float JEC         = jet.p4().E()/l1Jet.E();
      auto  l           = lepton->p4();
      auto  lepAwareJet = (l1Jet - l)*JEC + l;
      TLorentzVector lV(l.px(), l.py(), l.pz(), l.E());
      TLorentzVector jV(lepAwareJet.px(), lepAwareJet.py(), lepAwareJet.pz(), lepAwareJet.E());

      ptratio.push_back(l.pt()/lepAwareJet.pt());
      ptrel.push_back(lV.Perp((jV - lV).Vect()));
      btagcsv.push_back(jet.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"));

      //compute selected track multiplicity of closest jet
      int selectedTrackMult = 0;
      for(unsigned d = 0; d < jet.numberOfDaughters(); ++d){
        const pat::PackedCandidate* daughter = (const pat::PackedCandidate*) jet.daughter(d);
        try {                                                                                                     // In principle, from CMSSW_9_X you need to use if(daughter->hasTrackDetails()){ here, bus that function does not exist in CMSSW_8_X
            const reco::Track& daughterTrack = daughter->pseudoTrack();                                             // Using try {} catch (...){} the code compiles in both versions
            TLorentzVector trackVec(daughterTrack.px(), daughterTrack.py(), daughterTrack.pz(), daughterTrack.p());
            double daughterDeltaR            = trackVec.DeltaR(jV);
            bool goodTrack                   = daughterTrack.pt() > 1 && daughterTrack.charge() != 0 && daughterTrack.hitPattern().numberOfValidHits() > 7
                && daughterTrack.hitPattern().numberOfValidPixelHits() > 1 && daughterTrack.normalizedChi2() < 5 && fabs(daughterTrack.dz(vertex.position())) < 17
                && fabs(daughterTrack.dxy(vertex.position())) < 17;
            if(daughterDeltaR < 0.4 && daughter->fromPV() > 1 && goodTrack) ++selectedTrackMult;
        } catch (...){}
      }
      nchargeddaughers.push_back(selectedTrackMult); 
    }
  }//end e loop
  
  
  /// Filling variables previously computed
  putInEvent("JetPtRatio",     leptons, ptratio,          iEvent);
  putInEvent("JetPtRel",       leptons, ptrel,            iEvent);
  putInEvent("JetNDauCharged", leptons, nchargeddaughers, iEvent);
  putInEvent("JetBTagCSV",     leptons, btagcsv,          iEvent);
}

/// Function to put product into event
template <typename T> void AddLeptonJetRelatedVariables::putInEvent(std::string name, edm::Handle<std::vector<pat::Electron>>& probesHandle, std::vector<T>& product, edm::Event& iEvent){
  std::auto_ptr<edm::ValueMap<T>> out(new edm::ValueMap<T>());
  typename edm::ValueMap<T>::Filler filler(*out);
  filler.insert(probesHandle, product.begin(), product.end());
  filler.fill();
  iEvent.put(out, name);
}



// ------------ method called once each job just before starting event loop  ------------
void 
AddLeptonJetRelatedVariables::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
AddLeptonJetRelatedVariables::endJob() 
{
}

//define this as a plug-in
DEFINE_FWK_MODULE(AddLeptonJetRelatedVariables);
