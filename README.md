<h1> Macy11-k_Scraper </h1>

<h3>What It Achieves</h3>

The code has been written to extract the 'Net assets available for benefits' value from 2007 to 2018 for Macy's (most recent available data)
 
Macy's, like most U.S. companies, has its filings buried deep inside the U.S. Securities and Exchange Commission data hole. The scraper extracts details from the 11-k forms-an annual report of employee stock purchase, savings and similar plans-submitted by the company to the Securities and Exchange Commission (SEC). 


<h3>Methodology</h3>

Root Url for all archived filings : https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000794367&type=11-k&dateb=&owner=exclude&start=0&count=100

1) Import libraries
2) Tell beautiful soup to parse html string
3) Find the table on the page
4) Click on the hyperlink, Document. 
5) Click on the first link m401k201[].htm
6) Extract Data
7) Save it in a csv by writing the function get_11K()

Note: Only uses python to extract the data. Feel free to add selenium to see the process automate right in front of your eyes.

<h3>Your output</h3>
Macy's, Inc. 
2018
3,601,848




2017
3,799,097




2016
3,627,213




2015
3,467,944




2014
3,888,963




2013
3,607,233




2012
3,045,813




2011
2,794,333




2010
$2,712,471


2009
$2,427,225


[["Macy's, Inc. ", '3,601,848', 2018], ["Macy's, Inc. ", '3,799,097', 2017], ["Macy's, Inc. ", '3,627,213', 2016], ["Macy's, Inc. ", '3,467,944', 2015], ["Macy's, Inc. ", '3,888,963', 2014], ["Macy's, Inc. ", '3,607,233', 2013], ["Macy's, Inc. ", '3,045,813', 2012], ["Macy's, Inc. ", '2,794,333', 2011], ["Macy's, Inc. ", '$2,712,471', 2010], ["Macy's, Inc. ", '$2,427,225', 2009]]
