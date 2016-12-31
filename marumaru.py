import urllib
import urllib2
import BeautifulSoup
import re

#http://marumaru.in/b/manga/66687
print "start"
url="http://marumaru.in/b/manga/66687"
req=urllib2.Request(url)

req.add_header("User-agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
req.add_header("Cookie","__cfduid=d5615a04a393b7ad90381819064147afe1475473497; __utma=15075498.153873936.1475473504.1480147421.1481311584.11; __utmz=15075498.1476899575.7.2.utmcsr=facebook.com|utmccn=(referral)|utmcmd=referral|utmcct=/; PHPSESSID=be0fc01bdff9f041d1576c9f752f3bcd")

response = urllib2.urlopen(req)
html=response.read()

pas=BeautifulSoup.BeautifulSoup(html)
paslist=pas.findAll('a',attrs={'target':'_blank'})
count=1
for manurl in paslist:
    manurl=str(paslist[count])
    startIndex=manurl.index("http://")
    endIndex=manurl.index('" style')
    print str(count)+"화 "+manurl[startIndex:endIndex]
    count+=1

    
print "end"
