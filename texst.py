#!/usr/bin/env python3

import urllib
import requests
from bs4 import BeautifulSoup
import pprint
import json
from urllib.parse import urlparse

with open('./json/example.before', 'r') as e:

#    line = e.readline()
    while True:
        line = e.readline()
        URL = f"https://google.com/search?q={line}"
#        print(URL)
# desktop user-agent
        USER_AGENT = "mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

        headers = {"user-agent" : USER_AGENT}
        resp = requests.get(URL, headers=headers)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
        # HTTPConnectionPool fails before else:
        else:
            print('status code !==200 ooof')

        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                
# NEXT ALTERNATIVE ATTEMPT: CHECK BASE URL FOR /sitemap.xml or /stat.js
                print('link is::::::::: ')
                print(link)
# NOW PULL BASE URL
                o = urlparse(link)
               
                oo = o.scheme + '://' + o.netloc + '/sitemap.xml'

                print('ooooooooo')
                print(oo)
                # no but this is printing still 
                resp_two = requests.get(oo, headers=headers)
                print('made it')
                print(resp_two.status_code)
                if resp_two.status_code == 200:
                    more_soup = BeautifulSoup(resp_two.content, "html.parser")
                    more_results = []
                    for m in more_soup.find_all('url', class_='r'):
                        more_anchors = m.find_all('loc')
                        if more_anchors:
                            print('there are more anchors')



#                item = {
#                    'title': title,
#                    'link': link
#                }
#                results.append(item)
                results.append(link)




# uuuugggghhhh 
# this section is supposed to count the H2 tags in the document
# also see countH2.py

# now read the html from the website
#        for item in results:
#            print('item is: ' + item)
#            respresp = requests.get(item, headers=headers)
            
#            if respresp.status_code == 200:
#                soupsoup = BeautifulSoup(respresp.content, "html.parser")
#                print(soupsoup)
#            hackerCounter = 0
            #for h in soupsoup.find_all('h2', class_='r'):
                #moreAnchors = h.find_all('h2')
                #print(moreAnchors)
                #if moreAnchors:
                    #hackerCounter += 1
                    #print(hackerCounter)
            #for tag in soup.find_all():
                #print tag.name

            




#        pprint.pprint(results)

# ALL THE EXTRA FILE WRITES BELOW WERE FROM THE COMMENTED OUT item VAR ABOVE
# IT ENDED UP BEING TOO COMPLEX, EASIER TO JUST WRITE STRAIGHT TO FILE
#        pprint.pprint(results[-1]) 
        with open("./json/testing.txt", "a") as file:
#            file.writelines('[' + '\n')
#            file.writelines('\n' + '{' + '\"file\": ' + line.strip() + ", " + '\"URL\": ' + URL.strip() + "}," + '\n')
            file.writelines("%s\n" % result for result in results)
#            file.writelines('\n' + ']')
#            file.writelines("what tho")

# WHERE IS THE EXTRA [] COMING FROM IN THE TXT FILE?????

        if not line:
            break
