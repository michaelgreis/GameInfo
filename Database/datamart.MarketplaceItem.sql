--DROP TABLE datamart.MarketplaceItem;

CREATE TABLE datamart.MarketplaceItem (
    MarketplaceItemId SERIAL PRIMARY KEY, --PRIMARY KEY,
    Title VARCHAR(500) NOT NULL,
    AlternateName VARCHAR(500) NULL,
    ConsoleId INTEGER NOT NULL,
    --BusinessEntityId INTEGER NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
    );

CREATE UNIQUE INDEX NaturalKey_MarketplaceItem ON datamart.MarketplaceItem (Title, ConsoleId);

INSERT INTO datamart.MarketplaceItem (Title,AlternateName,ConsoleId,EtlSource) 
    SELECT 'Unknown' AS Title,
    'Unknown' AS AlternateName,
    (SELECT console.consoleId FROM datamart.console WHERE consolename = 'Unknown') as ConsoleId,
    'ManualEntry' AS etlSource;