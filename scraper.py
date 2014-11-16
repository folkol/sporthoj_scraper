from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
from os import makedirs, chdir
from re import sub, search
from datetime import datetime


def download_image(id):
  image = urlopen('http://www.sporthoj.com/galleri/bild?id={0}&header=1'.format(id), 'image.jpg')
  with open(id + '.jpg', "wb") as file:
    file.write(image.read())


if(len(argv) < 2):
  print 'usage: python %s http://www.sporthoj.com/blogg/?blogname' % argv[0]
  exit(1)

html = urlopen(argv[1]).read()
soup = BeautifulSoup(html, 'lxml')

blog_name = soup.find(id='blogg').table.tr.td.contents[1].string
makedirs(blog_name), chdir(blog_name)

for counter, post in enumerate(soup.find(id='inlagg')):
  title = post.div.text.strip()
  byline = post.select('div')[3].text
  date = search(r'Tidpunkt:(.+)[|]', byline).group(1).strip()
  date = datetime.strptime(date, '%d / %m - %Y %H:%M').strftime('%y-%m-%d')
  filename = '{0}_{1}_{2}'.format(counter, date, sub('\W', '-', title)).encode('utf-8')
  print filename
  makedirs(filename), chdir(filename)
  with open(filename + '.txt', 'w+') as file:
    print >> file, title.encode('utf-8'), '\n'
    for paragraph in post.select('div font p'):
      print >> file, paragraph.text.encode('utf-8').strip(), '\n'
    for img in post.select('div:nth-of-type(2) a img'):
      print img['src']
      download_image(search(r'id=([0-9]+)[&]', img['src']).group(1))
  chdir('..')
