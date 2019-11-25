## NWMLS Real Estate Data Project

This is a project pulls NWMLS data at the regional level down into a mysql data base. Then analytical queries are applaied and the resulst are sent out to twitter via the twitter API.

NWMLS publishes regional level Year over Year home closing data for residential and codos that resolves to some of the most local level data regarding home sales in the greater seattle area. A region in the NWMLS data is at a very granular level and each region breaks down into smaller neighborhoods. The major issue with getting this data is that NWMLS only publishes highly unstructured PDFs to the public. This project takes that 

### Data flow
1. Data is moved from unstructured PDFs to unstructured text files.
2. Unstructed text files are paresed and pruned into sturctured files.
3. Structured text files are entered into tables within a relational database.
4. Analytical queryes are applied to the database.
5. Results from the queries are sent to twitter via the twitter api, custom emojis are programatically added to the tweet based on the preformance of the region over the past year. 

![alt text](https://github.com/glstream/real_estate/blob/master/images/Real_estate.png)



### Regional Map:
![alt text](https://github.com/glstream/real_estate/blob/master/images/regions.png)

### End result
![alt text](https://github.com/glstream/real_estate/blob/master/images/tweet.png)
