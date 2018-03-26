--DROP TABLE  datamart.BusinessEntity;

CREATE TABLE datamart.BusinessEntity (
    BusinessEntityId SERIAL PRIMARY KEY,
    BusinessName VARCHAR(200) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);



CREATE UNIQUE INDEX business_name ON datamart.BusinessEntity (BusinessName);

INSERT INTO datamart.BusinessEntity (BusinessName,EtlSource) VALUES ('Unknown','ManualEntry');