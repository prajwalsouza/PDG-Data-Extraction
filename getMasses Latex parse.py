import BeautifulSoup
import re
import urllib2

import csv

DataBase = []

DataBaseCSV = []
DataBaseCSV.append(['PDG-LinkID', 'Type', 'Mass'])

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
			try:
				url = "http://pdglive.lbl.gov/DataBlock.action?node=" + link + "M"
				requestingURL = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
				page = urllib2.urlopen(requestingURL).read()

				# print(page)
				soup = BeautifulSoup.BeautifulSoup(page)
				table = soup.find('table')
				# print(table)
				rows = table.findAll('tr')
				datas = rows[0].findAll('td')
				# for data in datas:
				if datas[1].text.find('We do not') == -1:
					# print(datas[1].text)
					DataBlock['Mass'] = datas[1].text
				else:
					DataBlock['Mass'] = datas[2].text
			# for row in rows:
			# 	print("-r-")
			# 	datas = row.findAll('td')
			# 	for data in datas:
			# 		print(data.text)
			# 		print("")
				# print(table.findAll('tr'))
				# element = soup.findAll("tr", {'class' : 'z'})
				# print(element)

				# print(element[0].findAll('td')[0])
				
				# print(element.contents)
				# innerhtml = "".join([str(x) for x in element.contents]) 
				
				# print(element.find("tr"))
				# soup = BeautifulSoup.BeautifulSoup(innerhtml)
				# element = soup.findAll('script')
				# print(link)
				# print("Mass : ", element)
				# element = soup.find("span", {"style": "margin-left:50px;"})
				# print(element.contents)
			except:
				# print "Mass not found"
				DataBlock['Mass'] = 'NAN'
			print(DataBlock['Mass'])
			if typeLink == 'M':
				particleType = 'Meson'
			if typeLink == 'B':
				particleType = 'Baryon'
			DataBaseCSV.append([link, particleType, DataBlock['Mass']])
			DataBase.append(DataBlock)



DataBaseCSVCopy = DataBaseCSV[:]

for particle in DataBaseCSVCopy:
	parseLatex(particle[2])

myFile = open('PDG-MassData.csv', 'w')
	
with myFile:
	writer = csv.writer(myFile)
	writer.writerows(DataBaseCSV)