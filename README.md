

xml.py

example before (xml)
<url>
<loc>
http://builds.wbgames.com/free/free-desi-chat-canada.html
</loc>
<lastmod>2019-09-10</lastmod>
<changefreq>monthly</changefreq>
<priority>0.6</priority>
</url>

xml.py grabs the html file from between the <loc> tags

example converted to json (before.json)
obj00000000 = {
   "html":"free-desi-chat-canada.html",
   "domains": {
      "domain0":"builds.wbgames.com",
   }
}

------------

scraper.py

iterates through the before.json in json/before.json
obj(i=00000000; i++)[index of html file]
searches google for this file

searches for results whose url is a subdomain

## I think we can actually skip this step entirely
reads the HTML for # of h2 html tags
if it's a match, it writes the domain to the after.json file
##
instead do:
##
grabs sub.domain.com 
adds /sitemap.xml
if exists, writes as much in after.json file with the domain
if !exists, writes false with domain
if exists, downloads it to ./new.sitemaps/
