import requests
from lxml import etree


file = open('美媛馆.txt','a',encoding='utf-8')
count = 1
while count < 384:
   a = str(count)
   url = 'http://www.mygirl8.com/thread-' + a +'.htm'
   count+=1
   response = requests.get(url)
   response.encoding = 'utf-8'
   html = response.text
   tree = etree.HTML(html)
   down = tree.xpath('//*[@id="body"]/div/div[1]/div[1]/div/pre[1]/text()')
   file.write(down[0])
   file.write('\n')
   print(down[0])
file.close()
exit()
