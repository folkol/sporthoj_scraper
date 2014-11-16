from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
from os import makedirs, chdir


if(len(argv) < 2):
  print 'usage: python %s http://www.sporthoj.com/blogg/?blogname' % argv[0]
  exit(1)

html = urlopen(argv[1]).read()
soup = BeautifulSoup(html, 'lxml')

title = soup.find(id='blogg').table.tr.td.contents[1].string
makedirs(title), chdir(title)
file = open('myfile.dat', 'w+')

for post in soup.find_all(id='inlagg'):
  # print post
  pass
