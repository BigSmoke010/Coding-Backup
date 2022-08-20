from bs4 import BeautifulSoup
import requests

bs = BeautifulSoup(requests.get('http://oceanofgames.com/').text, 'lxml')
pages = []

def show(link):
    for i in link.find_all('h2', class_="title"):
        print(i.text)
    print('available pages :')
    for i in link.find_all('a', class_='page'):
        print(i.text)
        pages.append(i)
        
def lesgo(num):
    global bs
    for x in pages:
        if num == str(x.text):
            goto = x.get('href')
            bs = BeautifulSoup(requests.get(goto).text, 'lxml')
    pages.clear()
    
show(bs)
selectedpage = input('which page do you want to go :')
lesgo(selectedpage)
        
while selectedpage != 'q':
    show(bs)
    selectedpage = input('which page do you want to go :')
    lesgo(selectedpage)
                

        
        
        