--DROP TABLE datamart.MarketplaceItemRelationship;

CREATE TABLE datamart.MarketplaceItemRelationship (
    MarketplaceItemRelationshipId SERIAL PRIMARY KEY,
    RelationshipTypeId INTEGER NOT NULL,
    BusinessEntityId INTEGER NOT NULL,
    MarketPlaceItemId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX NaturalKey_MarketplaceItemRelationship ON datamart.MarketplaceItemRelationship (RelationshipTypeId,MarketPlaceItemId,BusinessEntityId);

--ALTER TABLE datamart.MarketplaceItemRelationship DROP COLUMN BusinessEntityId;