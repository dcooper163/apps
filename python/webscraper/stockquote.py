import urllib.request
import urllib.parse
import re

url = "https://www.google.com/finance?q=NASDAQ%3ASPWR&ei=n3PsWNmbCcGmmAGf4ofICQ"
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686)'

req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read().decode("utf8")

#print the entire web page
#print(resp_data)

#https://www.google.com/finance?q=NASDAQ%3ASPWR&ei=n3PsWNmbCcGmmAGf4ofICQ
#<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="244">19.17</span>

#print a subset of that webpage matching the regex criteria
par = re.findall(r'<span id="ref_702189_l">(.*?)</span>', str(resp_data))
print(par)
