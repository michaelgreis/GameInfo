CREATE VIEW datamart.marketitem_basic_currentvprevious AS
SELECT mibr.marketplaceitemid
	, mibr.marketentryid
    , mibl.marketentryid as lastmarketentryid
    , mibr.title
    , mibr.alternatename
    , mibr.releasedate
    , mibr.primaryprice as CurrentPrimaryPrice
    , mibl.primaryprice as LastPrimaryPrice
    , mibr.entryupdatetime
    , mibl.entryupdateTime as LastEntryUpdateDateTime
    , mibr.consolename
    , mibr.sourcename

FROM (
    SELECT marketplaceitemid,
        MAX(RecentEntryRank) as MostRecentEntry,
        MAX(RecentEntryRank)-1 as PreviousEntry
    FROM (
    SELECT marketplaceitemid, marketentryid, RANK() OVER (PARTITION BY marketplaceitemid ORDER BY marketentryid DESC) as RecentEntryRank
    FROM datamart.marketitem_basic
    ) RecentEntries
    GROUP BY marketplaceitemid
    ) MostRecent
INNER JOIN 
    (
    SELECT *, RANK() OVER (PARTITION BY marketplaceitemid ORDER BY marketentryid DESC) as RecentEntryRank
    FROM datamart.marketitem_basic
    ) mibr
ON MostRecent.marketplaceitemid = mibr.marketplaceitemid
AND MostRecent.MostRecentEntry = mibr.RecentEntryRank
LEFT JOIN
    (
    SELECT *, RANK() OVER (PARTITION BY marketplaceitemid ORDER BY marketentryid DESC) as RecentEntryRank
    FROM datamart.marketitem_basic
    ) mibl
ON MostRecent.Marketplaceitemid = mibl.marketplaceitemid
AND MostRecent.PreviousEntry = mibl.RecentEntryRank
WHERE mibr.primaryprice <> mibl.primaryprice;