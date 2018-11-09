from bs4 import BeautifulSoup
from netaddr import IPNetwork
import urllib3

http = urllib3.PoolManager()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urls = ["https://iplists.firehol.org/files/feodo.ipset"]

url = "https://iplists.firehol.org/files/firehol_level1.netset"
response = http.request('GET', url)
soup = BeautifulSoup(response.data, features="html.parser").prettify()

soup = soup.split("\n")

for i, line in enumerate(soup):
	if len(line) == 0 or line[0] == "#":
		continue
	print("firstIP = {0}, lastIP = {1}", line[:line.find("/")])

