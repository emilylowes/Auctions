# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("ul li a")
#cssselect is a selector, root stores the html so we can explore the data, cssselect will grab anything under an "a" tag, which is
#then stored in new variable links.
links = root.cssselect("ul li a")

print (links)

for li in links[:300]:
  liststexts = li.text_content()
  print (liststexts)

 
record = {}
for li in links:
  liststexts = li.text_content()
  print (liststexts)
  record['address']=liststexts
  scraperwiki.sqlite.save(['address'],record)


#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
