import BeautifulSoup
import re
import urllib2
import csv



def openCSV(filepath):
	returnarray = []
	with open(filepath) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			returnarray.append(row)
	return returnarray


MassDataBaseCSV = openCSV('PDG-MassData.csv')
WidthDataBaseCSV = openCSV('PDG-Width-Data.csv')
IGJPCNameDataBaseCSV = openCSV('PDG-Name-IGJPC-Data.csv')

DataBaseCSV = []

for k in range(len(WidthDataBaseCSV)):
	linkIDM = MassDataBaseCSV[k][0]
	Ptype = MassDataBaseCSV[k][1]
	mass = MassDataBaseCSV[k][2]

	linkIDW = WidthDataBaseCSV[k][0]
	linkIDIG = IGJPCNameDataBaseCSV[k][0]
	if k == 0:
		fullWidth = "Width"
	else:
		fullWidth = WidthDataBaseCSV[k][2]
	IGJPCvalue = IGJPCNameDataBaseCSV[k][2]
	Name = IGJPCNameDataBaseCSV[k][3]

	# print("")
	DataBaseCSV.append([linkIDM, Name, Ptype, mass, fullWidth, IGJPCvalue])
	print([linkIDM, Name, Ptype, mass, fullWidth, IGJPCvalue])

	if (linkIDM != linkIDW and linkIDW != linkIDIG):
		print("\n\n\nError!!\n\n\n")



myFile = open('PDG-Data-ASitWas.csv', 'w')
	
with myFile:
	writer = csv.writer(myFile)
	writer.writerows(DataBaseCSV)
# print(DataBaseCSV)


