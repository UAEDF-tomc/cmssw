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
  
  // ----------auxiliary functions -------------------  
  // ----------member data ---------------------------
  edm::EDGetTokenT<edm::View<reco::Jet>> jetCollectionTag_;
  edm::EDGetTokenT<edm::View<reco::Jet>> jetCollectionTag2_;
  edm::EDGetTokenT<reco::CandidateView> leptonCollectionTag_;
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
  jetCollectionTag2_ = consumes<edm::View<reco::Jet>>(jetcollection2);

  edm::InputTag leptoncollection = iConfig.getParameter<edm::InputTag>("LeptonCollection");
  leptonCollectionTag_ = consumes<reco::CandidateView>(leptoncollection);
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
  produces<edm::ValueMap<int> >("JetNDauCharged");
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

  edm::Handle<edm::View<reco::Jet>> jets;       
  iEvent.getByToken (jetCollectionTag_, jets);    

  edm::Handle<edm::View<reco::Jet>> jets2;       
  iEvent.getByToken (jetCollectionTag2_, jets2);    

  edm::Handle<reco::CandidateView> leptons;               
  iEvent.getByToken (leptonCollectionTag_, leptons);       
/*
  edm::Handle<reco::JetCorrector> correctorL1L2L3Res;
  iEvent.getByToken(tagL1L2L3ResCorrector_, correctorL1L2L3Res);

  edm::Handle<reco::JetCorrector> correctorL1;
  iEvent.getByToken(tagL1Corrector_, correctorL1);

  edm::Handle<reco::JetTagCollection> bTagHandle;
  iEvent.getByToken(bTagCollectionTag_, bTagHandle);
  const reco::JetTagCollection & bTags = *(bTagHandle.product());
*/
  edm::Handle<std::vector<pat::PackedCandidate>> pfCandidates;
  iEvent.getByToken(pfCandidates_, pfCandidates);

  edm::Handle<reco::VertexCollection> PVs;
  iEvent.getByToken(vertexes_, PVs);
  reco::VertexRef PV(PVs.id());
  reco::VertexRefProd PVRefProd(PVs);

  //Output
  std::vector<double > ptratio,ptrel,nchargeddaughers,btagcsv;
  for( reco::CandidateView::const_iterator icand = leptons->begin(); icand != leptons->end(); ++ icand){

    //Initialise loop variables
    float dR = 9999;
    reco::Candidate::LorentzVector jet, e;
    float csv(-999.);
    int nchdaugthers(0);    

    int i = 0, j = 0;
    for (auto ijet = jets->begin(); ijet != jets->end(); ++ijet, ++i) {

      // get smallest deltaR with the lepton
      if(deltaR(*ijet, *icand) > dR) continue;
      dR = deltaR(*ijet, *icand);

      // A hacky way to easily get the csv value even if we run on the raw jet collection
      for (auto jjet = jets2->begin(); jjet != jets2->end(); ++jjet, ++j) {
        if(i==j){
          auto patJet = static_cast<const pat::Jet*> (&*jjet);
          csv = patJet->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags");
        }
      }
      
      e   = icand->p4();
      jet = ijet->p4();

      unsigned int ic=0;
      for (auto pfcand = pfCandidates->begin(); pfcand !=pfCandidates->end(); ++pfcand){
	ic++;
	if (pfcand->charge()==0) continue;
	if (deltaR(*ijet,*pfcand) > 0.4) continue;	
	if (!pfcand->bestTrack()) continue;
	if (!pfcand->bestTrack()->quality(reco::Track::highPurity)) continue;
	if (pfcand->bestTrack()->pt()<1.) continue;
	if (pfcand->bestTrack()->hitPattern().numberOfValidHits()<8) continue;
	if (pfcand->bestTrack()->hitPattern().numberOfValidPixelHits()<2) continue;
	if (pfcand->bestTrack()->normalizedChi2()>=5) continue;
	
	PV = reco::VertexRef(PVs, 0);
	math::XYZPoint PVpos = PV->position();

	if (std::fabs(pfcand->bestTrack()->dxy(PVpos)) > 0.2) continue;
	if (std::fabs(pfcand->bestTrack()->dz(PVpos)) > 17) continue;
	nchdaugthers++;
      }
    }    

    //
    //Fill the pt ratio and pt rel
    //
    //No jets found
    if(dR > dRmax_){
      ptratio.push_back(-99);
      ptrel.push_back(-99);
      btagcsv.push_back(-999.);
      nchargeddaughers.push_back(-1);
    }
    else{
      ptratio.push_back(e.pt()/jet.pt());

      if(subLepFromJetForPtRel_) jet -= e;
      TLorentzVector tmp_e, tmp_jet;
      tmp_e.SetPxPyPzE(e.px(),e.py(),e.pz(),e.E());
      tmp_jet.SetPxPyPzE(jet.px(),jet.py(),jet.pz(),jet.E());
      if ((tmp_jet-tmp_e).Rho()<0.0001)  ptrel.push_back(0.);
      else                               ptrel.push_back(tmp_e.Perp(tmp_jet.Vect()));

      btagcsv.push_back(csv);
      nchargeddaughers.push_back(nchdaugthers);
    }


  }//end e loop
  
  
  /// Filling variables previously computed
   std::auto_ptr<ValueMap<float> > JetPtRatio(new ValueMap<float>());
   ValueMap<float>::Filler filler(*JetPtRatio);
   filler.insert(leptons, ptratio.begin(), ptratio.end()); 
   filler.fill();
   iEvent.put(JetPtRatio,"JetPtRatio");
 
   std::auto_ptr<ValueMap<float> > JetPtRel(new ValueMap<float>());
   ValueMap<float>::Filler filler1(*JetPtRel);
   filler1.insert(leptons, ptrel.begin(), ptrel.end()); 
   filler1.fill();
   iEvent.put(JetPtRel,"JetPtRel");

  std::auto_ptr<ValueMap<int> > JetNDauCharged(new ValueMap<int>());
  ValueMap<int>::Filler filler2(*JetNDauCharged);
  filler2.insert(leptons, nchargeddaughers.begin(), nchargeddaughers.end()); 
  filler2.fill();
  iEvent.put(JetNDauCharged,"JetNDauCharged");

  std::auto_ptr<ValueMap<float> > JetBTagCSV(new ValueMap<float>());
  ValueMap<float>::Filler filler3(*JetBTagCSV);
  filler3.insert(leptons, btagcsv.begin(), btagcsv.end()); 
  filler3.fill();
  iEvent.put(JetBTagCSV,"JetBTagCSV");

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
