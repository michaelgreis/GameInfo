--DROP TABLE datamart.Source

CREATE TABLE datamart.Source (
    SourceId SERIAL NOT NULL,
    SourceName VARCHAR(200) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);

CREATE UNIQUE INDEX Source ON datamart.Source (SourceName);

INSERT INTO datamart.Source (SourceName,EtlSource) VALUES ('Sony Online Store','ManualEntry');
INSERT INTO datamart.Source (SourceName,EtlSource) VALUES ('Steam Marketplace','ManualEntry');
INSERT INTO datamart.Source (SourceName,EtlSource) VALUES ('Unknown','ManualEntry')