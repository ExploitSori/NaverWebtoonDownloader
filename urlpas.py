import urllib
import BeautifulSoup
import re
import os
html=urllib.urlopen(webtoonUrl)
pas=BeautifulSoup.BeautifulSoup(html)
paslist=pas.findAll('div',attrs={'class':'wt_viewer'})
imgdata=str(paslist)
imglist=re.split('/>',imgdata)
count=0
for i in imglist:
    aa=i
    if count==0:
        print aa[248+11:103+248+11]+"\n"
    elif count<10:
        print aa[11:11+103]+"\n"
    else:
        print aa[11:11+104]+"\n"
        
    count+=1
 
 
#down X > 403 Error
