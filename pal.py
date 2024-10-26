import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base="https:/xkcd.com/"
archive="https:/xkcd.com/archive/"

output="XKCD comics"
if not os.path.exists(output):
    os.makedirs(output)

def download(url,filename):
    response=requests.get(url)
    with open(filename,"wb") as file:
        file.write(response.content)
    print(f"Downloaded : {filename}")

response=requests.get(archive)
soup=BeautifulSoup(response.text,"html.parser")
clink=soup.select("#middleContainer a")

for link in clink:
    cnum=link["href"].strip("/")
    comic_url=urljoin(base,f"{cnum}/")
    response=requests.get(comic_url)
    c_soup=BeautifulSoup(response.text,"html.parser")
    img=c_soup.find("div",id="comic").img["src"]
    img=urljoin(base,img)
    img_ext=os.path.split(img)[1]
    img_fname=os.path.join(output,f"{cnum}{img_ext}")
    download(img,img_fname)

print("All XKCD downloaded")
