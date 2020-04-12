#!/bin/env python3

# this script reads new *.sitemap.xml files in ./new.sitemaps
# it converts each entry into an entry in before.json
# xml and json examples found in readme

# imports
#import untangle
import json
import os

# loop
# with open(*.sitemap.xml) as f:
# for i in f:
# real expression to grab .html file


# -----
# read filenames in ./new.sitemaps
# import os
# var mapFileName

#for root, dirs, files in os.walk("./new.sitemaps"):
#    for filename in files:
#        print(filename)
#        mapFileName = filename
#print('hi')
#print(mapFileName)
# this works and is neat but
# it grabs the README.md file, gotta exclude that
# taking too long, moving on

# -----
# read xml into variable
# import untangle

# obj = untangle.parse('./new.sitemaps/'mapFileName)

# -----
# import xmltodict
# !!!!!


# -----
import xml.etree.ElementTree as ET
tree = ET.parse('./new.sitemaps/test.partpay.co.nz.sitemap.xml')
root = tree.getroot()
# print('\nItem #2 data: ')
# print(root[1][0].text)


dom = root[0][0].text
#print(dom)
import re
#reggie = r'[^/\\&\?]+\.\w{3,4}(?=([\?&].*$|$))'
# -----
for i in range(1,1000)
    link = root[i][0].text # "yet-another-name.html" # parsed from url in <loc> in xml
#    print(link)
#    file = re.findall(reggie,link)
    if link.startswith(dom):
        file = re.sub(dom, '', link)
#    print(file)
    i += 1
# makes a list
#xml = [ html ]

#print(xml)
# desired output:
# var = some-name.html
# -----

# write variable into before.json
# { html: "some-name.html" }
# {"htmls":[ { "html":"some-name.html"},{"html":"another-name.html"} ]}

# xml["htmls"].append()

# (import json)

#with open("./json/before.json", "r+") as file:
#    data = json.load(file)
#    data.update(xml)
#    file.seek(0)
#    json.dump(data, file)
# json seems like overkill actually
# -----

    with open("./json/before.txt", "a") as f:
        f.write(str(file + '\n'))
