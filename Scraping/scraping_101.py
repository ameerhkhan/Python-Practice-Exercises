from bs4 import BeautifulSoup
import requests

# can use both lxml as well html5lib parser.
# for this exercise we will use lxml parser

# We will use the testwebsite.html for checking our scrapper.

# let's pass our html into our beautiful soup to get an object.
# We can pass HTML as a string or an HTML file.


with open('testwebsite.html') as html_file:
    soup = BeautifulSoup(html_file,     #file
                            'lxml')     #parser

print(soup)
print(soup.prettify())

# To grab any Title or a paragraph we can access it like an attribut.
print()
match = soup.title.text
print(match)

print()
match_div = soup.find('div', class_='footer') # to find a div with class of footer. # use class_ because python already uses class
print(match_div)

# A good way to start is to get one object and then scale.
print()
article = soup.find('div', class_='article')
print(article)

#Stringing --> Very Pythonic hmmm...
print()
headline = article.h2.a.text
print(headline)
summary = article.p.text
print(summary)


#to find all tags that match an argument.
print()
for article in soup.find_all('div', class_='article'):
    #print()
    headline = article.h2.a.text
    summary = article.p.text
    print(headline, ': ',summary)
    print()

