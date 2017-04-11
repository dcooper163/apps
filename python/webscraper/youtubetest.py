import urllib.request
import urllib.parse
import re

url = 'https://www.nytimes.com/'
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'

req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read().decode("utf8")
par = re.findall(r'story-heading"><a href="(.*?)">(.*?)</a>',str(resp_data))

for n in par:
    print(n[1])
    #print(n[1].replace("\xe2\x80\x99","'"))
