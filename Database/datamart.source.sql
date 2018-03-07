--DROP TABLE datamart.Source

CREATE TABLE datamart.Source (
    SourceId SERIAL PRIMARY KEY,
    SourceName VARCHAR(200) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);