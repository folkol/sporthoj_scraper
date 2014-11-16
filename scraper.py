from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
from os import makedirs, chdir
from re import sub


if(len(argv) < 2):
  print 'usage: python %s http://www.sporthoj.com/blogg/?blogname' % argv[0]
  exit(1)

html = urlopen(argv[1]).read()
soup = BeautifulSoup(html, 'lxml')

blog_name = soup.find(id='blogg').table.tr.td.contents[1].string
makedirs(blog_name), chdir(blog_name)

for counter, post in enumerate(soup.find(id='inlagg')):
#  makedirs(str(counter))
#  chdir(str(counter))
  title = post.div.text.strip()
  filename = str(counter) + '-' + sub('[^0-9a-zA-Z]+', '-', title)
  print filename
  makedirs(filename), chdir(filename)
  with open(filename + '.txt', 'w+') as file:
    file.write(title.encode('utf-8'))
    file.write(post.contents[4].text.encode('utf-8'))
  chdir('..')
  #makedirs(title), chdir(title)
  #pass
