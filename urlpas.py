
import urllib
import BeautifulSoup
import re
import os

webtoonUrl = "http://comic.naver.com/webtoon/detail.nhn?titleId=650304&no=123&weekday=tue";#super secret
html=urllib.urlopen(webtoonUrl)
pas=BeautifulSoup.BeautifulSoup(html)
title = pas.findAll('h2',attrs={'class':'ly_tit'})
print str(title)[36:str(title).find('<',36):]#comics title
ep = pas.findAll('h3')#episode
print str(ep)[5:str(ep).find('<',4):]
paslist=pas.findAll('div',attrs={'class':'wt_viewer'})
imgdata=str(paslist)
imglist=re.split('/>',imgdata)
count=0
for i in imglist:
    aa=i
    if count==0:
        print aa[51+11:167]#+"\n"
    elif count<9:
        print aa[11:11+105]#+"\n"
    else:
        print aa[11:11+106]#+"\n"

    count+=1


#down X > 403 Error
