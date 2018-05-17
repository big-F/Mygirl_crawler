import requests
import json

file = open('ugirlU系列.txt','w',encoding='utf-8')
#其他系列自己改下面的网址
url = 'http://www.ugirls8.com/api/discussions?include=startUser%2ClastUser%2CstartPost%2Ctags&filter%5Bq%5D=%20tag%3Au&'
response = requests.get(url)
cookies = response.cookies
response.encoding = 'utf-8'
response = response.text

content = json.loads(response)
for i in content['data']:
    str = i['attributes']['title']
    str = 'http://down.ugirls8.com/U/[Ugirls8.com]' + str + '.rar'
    print(str)
    file.write(str)
    file.write('\n')
#生成第二页第三页地址
count = 1
while count < 3:
    a = count * 20
    url = 'http://www.ugirls8.com/api/discussions?include=startUser%2ClastUser%2CstartPost%2Ctags&filter%5Bq%5D=%20tag%3Au&page%5Boffset%5D={}'.format(a)
    response = requests.get(url)
    response.encoding = 'utf-8'
    response = response.text
    content = json.loads(response)
    title = content['data'][0]['attributes']['title']
    for j in content['data']:
        str = j['attributes']['title']
        str = str = 'http://down.ugirls8.com/U/[Ugirls8.com]' + str + '.rar'
        file.write(str)
        file.write('\n')
    count = count + 1
file.close()
exit()
