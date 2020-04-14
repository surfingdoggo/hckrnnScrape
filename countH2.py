# import stuff
# see texst.py or whatever

def num_appearances_of_tag(tag_name, html):
    tripleSoup = BeautifulSoup(html)
    return len(tripleSoup.find_all(tag_name))

anotherVar = 'http://test.partpay.co.nz/kevin-durand-nackt.html'
lolo = num_appearances_of_tag('h2', anotherVar)
print('lolo is ;;;;;;;;;;;;;;;;;;;;'
print(lolo)
