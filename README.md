# Scraper

Scraper uses [snscrape](https://github.com/JustAnotherArchivist/snscrape) to scrape twitter and reddit posts. Thank you to Martin Beck's [How to Scrape Tweets With snscrape](https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af) write-up, which got me started. See his files under `/TwitterScraper`. The files in that directory are not necessary to run `Scraper.py`

## To run
* Type `python3 Scraper.py`
* Choose:
  1. To search on Twitter. This accepts the same [advanced search operators](https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators) as the Twitter search box.
  2. To search on Reddit. 
  3. To search for a Subreddit with the term you entered. Results should show posts from that subreddit if it exists. This results aren't complete. It doesn't show the post, but it does show the URL.
* Type the maximum number of results to receive.
* Type a search term or terms.
* Type a filename prefix (random numbers and the count will be appended to this name).
* Output is a `.csv` file with the full name shown in the console.

## To do
* make first choice a function
* make if statements into functions
* make it so that you can go back and make a different choice
* twitter from:username search
* twitter from:username since: until: options
* twitter search -- choose from straight up search to username, since, until

## Helpful links
* print to csv: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
* https://www.w3schools.com/python/ref_func_input.asp
* https://www.freecodecamp.org/news/python-convert-string-to-int-how-to-cast-a-string-in-python/
* https://docs.python.org/3/library/json.html#basic-usage
* https://stackoverflow.com/questions/68453165/python-can-you-refresh-a-variable-to-re-initialize-with-new-sub-variables
* https://docs.python.org/3/library/csv.html
* https://stackoverflow.com/questions/18791882/how-to-make-program-go-back-to-the-top-of-the-code-instead-of-closing -- for the if/elif/else example
* https://stackoverflow.com/questions/39612262/how-to-convert-a-large-json-file-into-a-csv-using-python -- convert json lines to csv (a lifesaver)
* https://github.com/JustAnotherArchivist/snscrape/blob/master/snscrape/modules/twitter.py
* https://github.com/JustAnotherArchivist/snscrape
* https://stackoverflow.com/questions/44287011/valueerror-expected-object-or-value-when-reading-json-as-pandas-dataframe
* https://stackoverflow.com/questions/30088006/loading-a-file-with-more-than-one-line-of-json-into-pandas -- dead end, ended up using csv.writer
* https://www.statology.org/valueerror-trailing-data/ -- same as above
* https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write -- future to do, use pandas for data manipulation
* https://www.w3schools.com/python/gloss_python_elif.asp

## Reddit search help https://www.reddit.com/wiki/search/
* Summary:
* `author:name`
* `flair:flairname`
* Show text posts only `self:true`
* The body of the post: `selftext:term`
* The domain of the submitted URL: `site:domain`
* The submission's subreddit: `subreddit:name`
* The submission title: `title:term`
* The submission's URL (the website's address): `url:address`
* Combined search: `author:name subreddit:name searchterm`
