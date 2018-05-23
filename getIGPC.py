import BeautifulSoup
import re
import urllib2

import csv

DataBase = []

DataBaseCSV = []
DataBaseCSV.append(['PDG-LinkID', 'Type', 'IGJPC','Name'])

ParticleTypeLinks = [ ['M', ['005', '020', '035', '040', '045', '046', '049', '025', '030']] ,['B', ['005', '010', '020', '025', '030', '035', '040', '043', '045', '012']] ]

for PtypeLink in ParticleTypeLinks:
	typeLink = PtypeLink[0]
	Lists = PtypeLink[1]
	for pageID in Lists:
		print("\n New  List.")
		print(typeLink + pageID)
		print("*************")
		url = "http://pdglive.lbl.gov/ParticleGroup.action?init=0&node=" + typeLink + "XXX" + pageID
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
			
			if typeLink == 'M':
				particleType = 'Meson'
			if typeLink == 'B':
				particleType = 'Baryon'

			print("IGJPC.")
			try:
				url = "http://pdglive.lbl.gov/Particle.action?node=" + link
				requestingURL = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
				page = urllib2.urlopen(requestingURL).read()

				# print(page)
				soup = BeautifulSoup.BeautifulSoup(page)
				head1 = soup.find('h1')
				spans = head1.findAll('span')
				DataBlock['IGJPC'] = spans[1].text
				DataBlock['Name'] = spans[0].text

			except:
				# print "Mass not found"
				DataBlock['IGJPC'] = 'NAN'
				DataBlock['Name'] = 'NAN'

			print(DataBlock['IGJPC'])
			print(DataBlock['Name'])

			DataBaseCSV.append([link, particleType, DataBlock['IGJPC'], DataBlock['Name']])
			DataBase.append(DataBlock)


print(DataBaseCSV)

myFile = open('PDG-Name-IGJPC-Data.csv', 'w')
	
with myFile:
	writer = csv.writer(myFile)
	writer.writerows(DataBaseCSV)