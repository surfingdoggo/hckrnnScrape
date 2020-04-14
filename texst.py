#!/usr/bin/env python3

import urllib
import requests
from bs4 import BeautifulSoup
import pprint
import json

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


        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                


#                item = {
#                    'title': title,
#                    'link': link
#                }
#                results.append(item)
                results.append(link)
# now read the html from the website
        for item in results:
            linklink = item
            print('item is: ' + item)
            print('link is: ' + linklink)
            respresp = requests.get(link, headers=headers)
            print('respresp is: ' + respresp)
            if respresp.status_code == 200:
                soupsoup = BeautifulSoup(respresp.content, "html.parser")
                print(soupsoup)
            hackerCounter = 0
            for h in soupsoup.find_all('div', class_='r'):
                moreAnchors = h.find_all('h2')
                print(moreAnchors)
                if moreAnchors:
                    hackerCounter += 1
                    print(hackerCounter)


#        pprint.pprint(results)


#        pprint.pprint(results[-1]) 
        with open("./json/testing.txt", "a") as file:
#            file.writelines('[' + '\n')
#            file.writelines('\n' + '{' + '\"file\": ' + line.strip() + ", " + '\"URL\": ' + URL.strip() + "}," + '\n')
            file.writelines("%s\n" % result for result in results)
#            file.writelines('\n' + ']')
#            file.writelines("what tho")
        if not line:
            break
