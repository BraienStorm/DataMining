import requests
import re
import time

ker = dict()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

url = "https://testadmin.omvk.hu/onlinetest/setstatus"
url2 = "https://testadmin.omvk.hu/onlinetest/getresult"
data = {"qNum": 1,"chA": 1}

s = requests.Session()
s.max_redirects = 300

r= s.get('https://testadmin.omvk.hu/onlinetest',headers=headers)
asks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
i = 0
while True:
    try:
        time.sleep( 5 )
        r= s.get('https://testadmin.omvk.hu/onlinetest/startTest',headers=headers)
        for ask in asks:
            data = {"qNum": ask,"chA": 1}
            r= s.post(url,data=data,headers=headers1)

        r= s.post(url2,headers=headers1)
        ret =  r.json()
        a = ret['output']
        points = [m.start() for m in re.finditer('\<td class="rtd-question" colspan="4">', a)]
        for point in points:
            b = a[point:]    
            x = b.find('</td>')
            c = b[37:x]
            x = c.find('.')
            c = c[x+2:] 
            x = b.find('"rtd-answer">')
            d = b[x+13:]
            x = d.find('</td>')
            d = d[:x]
            if  c not in ker:
                ker[c] = d
        if i == 300:
            break
        i = i+1    
    except:
        time.sleep( 100 )
with open('file.txt', 'w') as file:
   print(ker, file=file)