import os
import sys

#search file for each lexus listing URI
class search_file(object):
	
	def __init__(self, file):
		self.file = file
		self.results = []

	def search(self, string):
		file = open(self.file, "r")
		lines = file.readlines()	
		for line in lines:
			if string in line:
				result = line[70:-4]
				self.results.append(result)
				print("%s written to file" % result)
		file.close()
		return self.results
		
	def write_to_file(self):
		f = open('lexus_uris.py', 'w')
		f.write(str("uris = %s" % self.results))
		#for x in range(0, len(self.results)):
		#	f.write("\n %s" % self.results[x])
		f.close()


def main():
	file = search_file('lexus_data.txt')
	print('Searching file')
	string = "#srp_listing_description_"
	file.search(string)
	print('Printing file results')
	file.write_to_file()
	print('New file created.')
	

if __name__ == '__main__':
	main()
	
			
	
