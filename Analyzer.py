import BeautifulSoup
import re
import urllib2
import csv


url = "http://pdglive.lbl.gov/ParticleGroup.action?init=0&node=" + "MXXX005"
requestingURL = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
page = urllib2.urlopen(requestingURL).read()

linksRegex = r'node=(.*?)"'
linkIDs = re.findall(linksRegex, page)
print(linkIDs)
del linkIDs[0]
# print(linkIDs)

for link in linkIDs:
	DataBlock = {}
	print(link)
	DataBlock['linkID'] = link
	try:
		url = "http://pdglive.lbl.gov/Particle.action?node=" + link
		requestingURL = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		page = urllib2.urlopen(requestingURL).read()

		# print(page)
		# if page.find('($ 10^{8} $ s${}^{-1}$)') == -1:
		soup = BeautifulSoup.BeautifulSoup(page)
		head1 = soup.find('h1')
		spans = head1.findAll('span')
		print(spans[0].text, spans[1].text)
		# table = soup.find('table')
		# # print(table)
		# rows = table.findAll('tr')
		# # print(rows)
		# datas = rows[0].findAll('td')
		# # for data in datas:
		# if datas[1].text.find('We do not') == -1:
		# 	print(datas[1].text)
		# 	DataBlock['Mass'] = datas[1].text
		# else:
		# 	DataBlock['Mass'] = datas[2].text
		# 	print(datas[2].text)
	except:
		None