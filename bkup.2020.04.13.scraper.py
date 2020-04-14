#!/env/bin/python3

import urllib
import requests
from bs4 import BeautifulSoup
import pprint
import json

with open('./json/before.txt', 'r') as e:

#    line = e.readline()
    while True:
        line = e.readline()
        URL = f"https://google.com/search?q={line}" 
        print(URL)
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
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
        pprint.pprint(results)
        print(type(results))

        with open("./json/after.txt", "a") as file:
            file.writelines('\n' + line + '\n')
            file.writelines('\n' + 'URL: ' + URL + '\n')
            file.writelines("%s\n" % result for result in results)
        if not line:
            break
#
