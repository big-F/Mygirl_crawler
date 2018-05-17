import requests
from lxml import etree
import time

file = open('秀人网.txt','a',encoding='utf-8')
count = 57
while count < 1025:
   a = str(count)
   b = count%50
   if 0 == b:
       time.sleep(3)
   url = 'http://www.xiuren8.com/thread-' + a +'.htm'
   print(url)
   response = requests.get(url,proxies={'http':'127.0.0.1:1088'})
   response.encoding = 'utf-8'
   html = response.text
   tree = etree.HTML(html)
   down = tree.xpath('//*[@id="body"]/div/div[1]/div[1]/div/pre[1]/text()')
   print(down)
   try:
        file.write(down[0])
        file.write('\n')
   except:
       pass
   count+=1
file.close()
exit()
