import requests
import json
from lxml import etree
file = open('推女神www.tuigod.com.txt','a',encoding='utf-8')
response = requests.get('http://www.tuigod.com/api/discussions?include=startUser%2ClastUser%2CstartPost%2Ctags&filter%5Bq%5D=%20tag%3Atuigod&',proxies ={"http": "http://127.0.0.1:1088"})
response.encoding='utf-8'
content = json.loads(response.text)
for i in content['data']:
    id = i['id']
    slug = i['attributes']['slug']
    url = 'http://www.tuigod.com/d/' + id + '-' + slug
    print(url)
    #代理ip请更换成你自己的
    r1 = requests.get(url,proxies ={"http": "http://127.0.0.1:1088"})
    tree = etree.HTML(r1.text)
    down = tree.xpath('//code/text()')
    b = str(down[0])
    file.write(b)
    file.write('\n')
d=1
while d < 16:
    print(d)
    e = d * 20
    x = str(e)
    response = requests.get('http://www.tuigod.com/api/discussions?include=startUser%2ClastUser%2CstartPost%2Ctags&filter%5Bq%5D=%20tag%3Atuigod&page%5Boffset%5D={}'.format(x),proxies ={"http": "http://127.0.0.1:1088"})
    response.encoding='utf-8'
    print(response.url)
    content = json.loads(response.text)
    for c in content['data']:
        id = c['id']
        slug = c['attributes']['slug']
        url = 'http://www.tuigod.com/d/' + id + '-' + slug
        r1 = requests.get(url, proxies={"http": "http://127.0.0.1:1088"})
        tree = etree.HTML(r1.text)
        down = tree.xpath('//code/text()')
        b = str(down[0])
        file.write(b)
        file.write('\n')
    d+=1
file.close()
exit()
