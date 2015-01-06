#ifndef MuonAssociatorByHitsHelper_h
#define MuonAssociatorByHitsHelper_h

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/RecoCandidate/interface/TrackAssociation.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimMuon/MCTruth/interface/DTHitAssociator.h"
#include "SimMuon/MCTruth/interface/MuonTruth.h"
#include "SimMuon/MCTruth/interface/RPCHitAssociator.h"
#include "SimTracker/TrackerHitAssociation/interface/TrackerHitAssociator.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"

#include <boost/ptr_container/ptr_vector.hpp>

class TrackerTopology;

class MuonAssociatorByHitsHelper {
  
 public:
  typedef std::pair <uint32_t, EncodedEventId> SimHitIdpr;
  //typedef std::map<unsigned int, std::vector<SimHitIdpr> > MapOfMatchedIds;
  typedef std::pair<unsigned int,std::vector<SimHitIdpr> > uint_SimHitIdpr_pair;
  typedef boost::ptr_vector<uint_SimHitIdpr_pair> MapOfMatchedIds;
  
  MuonAssociatorByHitsHelper (const edm::ParameterSet& conf, edm::ConsumesCollector && iC);   
  MuonAssociatorByHitsHelper (const edm::ParameterSet& conf);   
  ~MuonAssociatorByHitsHelper();
  
 
  typedef std::vector<std::pair<trackingRecHit_iterator, trackingRecHit_iterator> > TrackHitsCollection;
  struct IndexMatch {
      IndexMatch(size_t index, double global_quality) : idx(index), quality(global_quality) {}
      size_t idx; double quality; 
      bool operator<(const IndexMatch &other) const { return other.quality < quality; } 
  };
  typedef std::map<size_t, std::vector<IndexMatch> > IndexAssociation;
 
  IndexAssociation associateSimToRecoIndices(const TrackHitsCollection &, 
                                             const edm::RefVector<TrackingParticleCollection>&,
					     const edm::Event * event = 0, const edm::EventSetup * setup = 0)  const; 
  IndexAssociation associateRecoToSimIndices(const TrackHitsCollection &, 
                                             const edm::RefVector<TrackingParticleCollection>&,
					     const edm::Event * event = 0, const edm::EventSetup * setup = 0) const;
  


 private:
  void getMatchedIds
    (MapOfMatchedIds & tracker_matchedIds_valid, MapOfMatchedIds & muon_matchedIds_valid,
     MapOfMatchedIds & tracker_matchedIds_INVALID, MapOfMatchedIds & muon_matchedIds_INVALID,
     int& n_tracker_valid, int& n_dt_valid, int& n_csc_valid, int& n_rpc_valid,
     int& n_tracker_matched_valid, int& n_dt_matched_valid, int& n_csc_matched_valid, int& n_rpc_matched_valid,
     int& n_tracker_INVALID, int& n_dt_INVALID, int& n_csc_INVALID, int& n_rpc_INVALID,
     int& n_tracker_matched_INVALID, int& n_dt_matched_INVALID, int& n_csc_matched_INVALID, int& n_rpc_matched_INVALID,
     trackingRecHit_iterator begin, trackingRecHit_iterator end,
     TrackerHitAssociator* trackertruth, DTHitAssociator& dttruth, MuonTruth& csctruth, RPCHitAssociator& rpctruth,
     bool printRts, const TrackerTopology *) const;
  
  int getShared(MapOfMatchedIds & matchedIds, TrackingParticleCollection::const_iterator trpart) const;

  const bool includeZeroHitMuons;    
  const bool acceptOneStubMatchings;
  bool UseTracker;
  bool UseMuon;
  const bool AbsoluteNumberOfHits_track;
  unsigned int NHitCut_track;    
  double EfficiencyCut_track;
  double PurityCut_track;
  const bool AbsoluteNumberOfHits_muon;
  unsigned int NHitCut_muon;    
  double EfficiencyCut_muon;
  double PurityCut_muon;
  const bool UsePixels;
  const bool UseGrouped;
  const bool UseSplitting;
  const bool ThreeHitTracksAreSpecial;
  const bool dumpDT;
  const edm::ParameterSet conf_;

  int LayerFromDetid(const DetId&) const;
  const TrackingRecHit* getHitPtr(edm::OwnVector<TrackingRecHit>::const_iterator iter) const {return &*iter;}
  const TrackingRecHit* getHitPtr(const trackingRecHit_iterator& iter) const {return &**iter;}

  std::string write_matched_simtracks(const std::vector<SimHitIdpr>&) const;

};

#endif
