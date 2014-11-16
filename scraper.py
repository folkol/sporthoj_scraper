from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
from os import makedirs, chdir
from re import sub, search
from datetime import datetime


if(len(argv) < 2):
  print 'usage: python %s http://www.sporthoj.com/blogg/?blogname' % argv[0]
  exit(1)

html = urlopen(argv[1]).read()
soup = BeautifulSoup(html, 'lxml')

blog_name = soup.find(id='blogg').table.tr.td.contents[1].string
#makedirs(blog_name), chdir(blog_name)

for counter, post in enumerate(soup.find(id='inlagg')):
  print post.prettify()
  title = post.div.text.strip()
  byline = post.select('div')[3].text
  date = search('Tidpunkt:(.+)[|]', byline).group(1).strip()
  print datetime.strptime(date, '%d / %m - %Y %H:%M').strftime('%y-%m-%d')
  filename = str(counter) + '-' + sub('\W', '-', title) + '_' + date.strip().encode('utf-8')
  exit(1)
  makedirs(filename), chdir(filename)
  with open(filename + '.txt', 'w+') as file:
    print >> file, title.encode('utf-8'), '\n'
    for paragraph in post.select('div font p'):
      print >> file, paragraph.text.encode('utf-8').strip(), '\n'
  chdir('..')
