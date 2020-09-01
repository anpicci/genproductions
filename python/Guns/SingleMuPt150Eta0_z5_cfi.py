import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(150.01),
        MinPt = cms.double(149.99),
        PartID = cms.vint32(13),
        MaxEta = cms.double(0.01),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-0.01),
        MinPhi = cms.double(-3.14159265359), ## in radians
        MaxZ = cms.double(5.01),
        MinZ = cms.double(4.99)

    ),
    Verbosity = cms.untracked.int32(1), ## set to 1 (or greater)  for printouts

    psethack = cms.string('single mu pt 15'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
