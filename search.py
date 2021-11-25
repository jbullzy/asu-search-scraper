import requests, sys, webbrowser, bs4
from bs4 import BeautifulSoup
from sys import argv

script, filename, filetwo, = argv

#-------------------------------------------------------------------------
# Initial setup. searching google, creating soup
#-------------------------------------------------------------------------

search = 'ASU'
print("searching google")
res = requests.get('https://google.com/search?q=' + search)
res.raise_for_status()

print("creating soup as a variable")
soup = bs4.BeautifulSoup(res.text, "html.parser")

#-------------------------------------------------------------------------
# Attempting to write only the links to a separate file
#-------------------------------------------------------------------------

linkelements = soup.select('.r a')

print(f"We're going to erase {filetwo}")
print("If you don't want that, hit ctrl-c.")
print("Otherwise, hit enter")

input(">>> ")

print("Opening the file...")
paper = open(filetwo, 'w')

print("Truncating the file. Seeya.")
paper.truncate()

print("Writing linkelements...")
for i in linkelements:
    paper.write()

#-------------------------------------------------------------------------
# Attempting to write the soup to a seperate file without selecting elements
#-------------------------------------------------------------------------

print("stringing the soup")
stringsoup = str(soup)

print(f"Now we're going to erase {filename}")
print("If you don't want that, hit ctrl-c.")
print("Otherwise, hit enter")

input(">>>")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file. Seeya.")
target.truncate()

print("pouring the soup in...")
target.write(stringsoup)

print("Done. Check and see if it worked")

#-------------------------------------------------------------------------
# Attempting to print the headings of each entry
#-------------------------------------------------------------------------

heading = soup.find_all('h3')

for info in heading:
    print(info.getText())
    print("----------")