import requests, sys, webbrowser, bs4
from bs4 import BeautifulSoup
from os import write

print("searching google")
res = requests.get('https://google.com/search?q=ASU')
res.raise_for_status()

# print("printing res variable")
# print(res)

print("creating soup as a variable")
soup = bs4.BeautifulSoup(res.text, "html.parser")

# print("printing soup.a")
# print(soup.a)

print("printing soup.h3")
print(soup.h3)

# print("printing soup.p")
# print(soup.p)

#print("printing prettified soup to a separate text file")
# with open('prettified.txt', 'w') as f:
#    write(print(soup.prettify), file=f)

# print("selecting links from the results")
# links = soup.select('.r a')

# for i in links:
   # print("-----printing-----")
    # print(i.text)
    # break


