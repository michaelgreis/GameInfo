This repo serves the following purpose.
1. Scraping
2. ETL
3. Database SQL

Item 1: are currently a couple of different scrapers. One which scrapes the sony playstore, the other which is much more comprehensive and scrapes the steam store. Both of these files output to json.

Item 2: We have the etl scripts which utilize python libraries and sql to move data from the json files output by the scrapers to the database. THen further transform the database into a 3NF model for consumption on whatever application will be consuming the data.

Item 3: This is all the SQL used to create the database. From the different accounts (cleaned of usernames and passwords), to the creation of the tables themselves and the creation of different indexs.

This repository exclusively uses python and SQL. With the following packages.
1. Scrapy
2. Scrapyd
3. PETL
4. psycopg2
5. Various other standard libraries like JSON and others