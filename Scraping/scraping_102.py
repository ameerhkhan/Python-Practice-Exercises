from bs4 import BeautifulSoup
import requests
import csv

# you can also use public apis to gather data from websites such as youtube or twitter or facebook/instagram
# For that you can use the requests library only. and Beautiful soup may not be required as such.

# let's get some information from a real website.

# first we need to get the source code using requests module

source = requests.get('http://coreyms.com').text        # .text used to convert it into text.


soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'Video_link'])

for article in soup.find_all('article'):
#article = soup.find('article')
    print(article.__class__)

    headline = article.header.h2.a.text
    print(headline.__class__)
    # print(str(headline))

    summary = article.find('div', class_='entry-content').p.text
    print(summary.__class__)
    #print(summary.__repr__)
    # print(summary)
    # To get away with error when program may not find an element we can use try and except.
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src'] # --> Access source attribute of a tag like a dictionary.
        # print(vid_src)

        vid_id = vid_src.split('/')[4] # item at 4th index of the list created via split.
        vid_id = vid_id.split('?')[0]
        print(vid_id)

        yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)
        print(yt_link)
    except:
        yt_link = None
        print(yt_link)


    print()
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()