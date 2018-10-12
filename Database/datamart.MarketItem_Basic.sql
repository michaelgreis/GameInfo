--View to be used for basic analysis


CREATE VIEW datamart.MarketItem_Basic AS
SELECT mpi.title
	, mpi.alternatename
    , mpe.releasedate
    , mpe.primaryprice
    , mpe.gameimageurl
    , mpe.insertdatetime AS entryupdatetime
    , con.consolename
    , src.sourcename
FROM datamart.marketplaceitem mpi
INNER JOIN datamart.marketentry mpe
ON mpi.marketplaceitemid = mpe.marketplaceitemid
INNER JOIN datamart.console con
ON mpi.consoleid = con.consoleid
INNER JOIN datamart.source src
ON mpe.sourceid = src.sourceid;