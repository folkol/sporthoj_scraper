from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
from os import makedirs, chdir
from re import sub, search
from datetime import datetime


def download_img(id):
  base_url = 'http://www.sporthoj.com/galleri/bild?id={0}&header=1'
  img = urlopen(base_url.format(id))
  with open(id + '.jpg', "wb") as file:
    file.write(img.read())


def main(blog_name):
  html = urlopen('http://www.sporthoj.com/blogg/?' + blog_name).read()
  soup = BeautifulSoup(html, 'lxml')

  blog_title = soup.find(id='blogg').table.tr.td.contents[1].string
  makedirs(blog_title), chdir(blog_title)

  for counter, post in enumerate(soup.find(id='inlagg')):
    title = post.div.text.strip()
    byline = post.select('div[id=publicerad]')[0].text
    print byline
    date = search(r'Tidpunkt:(.+)[|]', byline).group(1).strip()
    date = datetime.strptime(date, '%d / %m - %Y %H:%M').strftime('%y-%m-%d')
    filename_cleaned = sub('\W', '-', title)
    filename = '{0}_{1}_{2}'.format(counter, date, filename_cleaned).encode('utf-8')
    print filename
    makedirs(filename), chdir(filename)
    with open(filename_cleaned.encode('utf-8') + '.txt', 'w+') as file:
      print >> file, title.encode('utf-8'), '\n'
      paragraphs = post.select('div:nth-of-type(3) p')
      if not paragraphs:
          # Ever heard of semantic web?
          p=post.select('div:nth-of-type(3)')
          print >> file, p[0].text.encode('utf-8').strip(), '\n'
      for p in paragraphs:
        print >> file, p.text.encode('utf-8').strip(), '\n'
      for img in post.select('div:nth-of-type(2) a img'):
        print img['src']
        download_img(search(r'id=([0-9]+)[&]', img['src']).group(1))
    chdir('..')


if __name__ == "__main__":
    if(len(argv) < 2):
      print 'usage: python %s blogname' % argv[0]
      exit(1)
    main(argv[1])
