--DROP TABLE  datamart.BusinessEntity;

CREATE TABLE datamart.BusinessEntity (
    BusinessEntityId SERIAL PRIMARY KEY,
    BusinessName VARCHAR(200) NOT NULL,
    EtlSource VARCHAR(50) NOT NULL,
    InsertDateTime TIMESTAMP DEFAULT current_timestamp
);



CREATE UNIQUE INDEX business_name ON datamart.BusinessEntity (BusinessName);


--SELECT MAX(businessentityid)
--FROM datamart.businessentity
--INSERT INTO datamart.BusinessEntity (businessentityid,BusinessName,EtlSource) VALUES (325098,'Unknown','ManualEntry');

INSERT INTO datamart.BusinessEntity (BusinessName,EtlSource) VALUES ('Unknown','ManualEntry');