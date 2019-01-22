/*
This aggregation is meant to show price changes that have occurred at a daily aggregation

This is a view on a view, which is not a good practice and should be refactored as needed.
*/
CREATE VIEW datamart.MarketItem_Basic_DailyChange AS
SELECT 
    CAST(entryupdatetime AS DATE) as MostRecentUpdateDate,
    AVG(currentprimaryprice) as AverageRecentPrice,
    AVG(lastprimaryprice) as AverageLastPrice,
    AVG(currentprimaryPrice-lastprimaryprice) as AveragePriceChangeNumber,
    MIN(currentprimaryPrice-lastprimaryprice) as BiggestPriceDrop,
    MAX(currentprimaryPrice-lastprimaryprice) as BiggestPriceIncrease,
    COUNT(*) as RecordCount
FROM datamart.marketitem_basic_currentvprevious
WHERE currentprimaryPrice < 100
AND lastprimaryprice < 100
GROUP BY 
    CAST(entryupdatetime AS DATE)