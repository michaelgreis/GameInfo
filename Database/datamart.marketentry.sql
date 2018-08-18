--DROP TABLE datamart.MarketEntry;

CREATE TABLE datamart.MarketEntry (
    MarketEntryId SERIAL PRIMARY KEY,
    ReleaseDate VARCHAR(25) NULL ,
    SourceId INTEGER NULL, --Changed from sourcemarketidentifier (mismatch on the source table's name)
    PrimaryPrice DECIMAL(12,2) NULL,
    SourceUrl VARCHAR(300) NULL,
    GameImageUrl VARCHAR(300) NULL,
    ReviewsUrl VARCHAR(300) NULL,
    MarketplaceItemId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX NaturalKey_MarketEntry ON datamart.MarketEntry (SourceId, PrimaryPrice,MarketplaceItemId,releaseDate);
