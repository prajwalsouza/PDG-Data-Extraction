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


MassDataBaseCSV = openCSV('PGD-Data-Mass-Float.csv')
WidthDataBaseCSV = openCSV('PGD-Data-Width-Float.csv')
IGJPCNameDataBaseCSV = openCSV('PDG-Name-IGJPC-Data.csv')

DataBaseCSV = []

for k in range(len(WidthDataBaseCSV)):
	linkIDM = MassDataBaseCSV[k*2][0]
	Ptype = MassDataBaseCSV[k*2][1]
	mass = MassDataBaseCSV[k*2][2]

	linkIDW = WidthDataBaseCSV[k][0]
	linkIDIG = IGJPCNameDataBaseCSV[k][0]

	fullWidth = WidthDataBaseCSV[k][2]
	IGJPCvalue = IGJPCNameDataBaseCSV[k][2]
	Name = IGJPCNameDataBaseCSV[k][3]

	# print("")
	DataBaseCSV.append([linkIDM, Name, Ptype, mass, fullWidth, IGJPCvalue])
	if (linkIDM != linkIDW and linkIDW != linkIDIG):
		print("\n\n\nError!!\n\n\n")



myFile = open('PDG-Data.csv', 'w')
	
with myFile:
	writer = csv.writer(myFile)
	writer.writerows(DataBaseCSV)
# print(DataBaseCSV)


