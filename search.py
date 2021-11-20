import requests, sys, webbrowser, bs4
from bs4 import BeautifulSoup

print("searching google")
res = requests.get('https://google.com/search?q=ASU')

print("creating soup variable")
soup = bs4.BeautifulSoup(res.text, "html.parser")

print("selecting links from the results")
links = soup.select('.r a')

for i in links:
    print("-----printing-----")
    print(i.text)
    break

# print(links)

###
#   print("opening five links from the result")
#    openlinks = min(5, len(links))
#    for i in range(openlinks):
#        webbrowser.open('https://google.com'+links[i].get('href'))

