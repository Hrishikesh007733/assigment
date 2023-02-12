import urllib.request
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

website = input("Enter the url of a website:")

req = Request(
    url=website, 
    head={'User-Agent': 'Mozilla/5.0'}
)

try:
    res = urlopen(req)
    soup = BeautifulSoup(res,'html.parser',  from_encoding=res.info().get_param('charset'))
    
    if soup.findAll("meta", attrs={"name": "generator"}):
        print("Version of webiste is :", end=' ')
        print(soup.find("meta", attrs={"name": "generator"}).get("content"))

    else:
        try:
            req = Request(
                url=website+"wp-admin", 
                head={'User-Agent': 'Mozilla/5.0'}
            )

            res = urlopen(req)
            soup = BeautifulSoup(res,'html.parser',  from_encoding=res.info().get_param('charset'))

            if "WordPress" in soup.find("title").contents[0]:
                print('Yes')
            else:
                print('No')

        except:
            print('No')

except:
    print("Error")