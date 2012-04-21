from urllib import urlopen
import re

PATH = 'data/' #Where to save sitemap txts.
count = 0
finder = re.compile('<loc>(.*?)</loc>')
for f in finder.findall(urlopen('http://www.gstatic.com/s2/sitemaps/profiles-sitemap.xml').read()):
	txt = urlopen(f).read()
	count += len(txt.split('\n'))
	open(''.join([PATH, f.split('/')[-1]]), 'w').write(txt)

print '%s users found.' % count