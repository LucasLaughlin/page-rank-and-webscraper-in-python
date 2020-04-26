# Page Rank and web scraper in python
Recreated the Original Google page-rank algorithm and built a web scraper
## Python modules used:
 -scrapy
 -numpy
 -json
 
 Steps to scrape data:
 1. open backlinkscraper/backlinkscraper/spiders/link_scraper.py
 
 2. change start_url and allowed domains to the domain you want to crawl. Make sure you do not include "http://" in allowed domains
 
 3. from the backlinkscraper root folder run "scrapy crawl link_spider -o 'output'.json", changing the ouput name to whatever you want. Do not run this command on the same output name. It will append the second oupute to the edn of the first
 
 4. If you wish to simply test the conversion to a matrix, from the root project folder, run "python JsonToMatrix.py 'output'.json using your ouput file name  

5. To use within another program call the JsonToMatrix construtor and pass it the relative path to your ouput.json file. Then call the getMatrix function to return and numpy matrix 
