import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/History_of_Mexico"
# res=requests.get(url)
# html_text=res.text
# # print(html_text)
# with open ("file.html","w")as file:
#     file.write(html_text)
# soup=BeautifulSoup(html_text,"html.parser")
# print(soup)    
def get_citations_needed_count(url):
    res=requests.get(url)
    html_text=res.text
    soup=BeautifulSoup(html_text,"html.parser")
    num=soup.find_all("a",title="Wikipedia:Citation needed")
    return ("this url has this  number of citations needed",len(num))

def get_citations_needed_report(url):
    res=requests.get(url)
    html_text=res.text
    soup=BeautifulSoup(html_text,"html.parser")
    parent=soup.find_all("sup",class_="noprint Inline-Template Template-Fact")
    num=0
    for ele in parent:
        num+=1
        print(f'number {num}. references needed for report: {ele.parent.text}')
get_citations_needed_report(url)