# Stock-Market-Watchlist-Assistant
Get an automatic weekly watchlist using the Finviz.com screener

Running the stonks.py module will print out the contents of your weekly watchlist and save it to a file called watchlist.txt.

The module comes with two defualt criteria for a watchlist:
  1. Oversold: Stocks with an RSI(14) value of 30 or less whose price is still above the SMA 200.
  2. Sector Winners: Stocks from the top performing sector of the week with a relative volume of over 1.5.

Add new criteria by selecting criteria on https://finviz.com/screener.ashx and adding the url to the module (comments to point out where to do this)

Libraries: Must have BeautifulSoup and cloudscraper installed
