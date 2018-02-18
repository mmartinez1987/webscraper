import argparse
import lexus_ids #import constants

parser = argparse.ArgumentParser(description='specify file.')
parser.add_argument('-f', '--file', dest='file', action='store_true')
args = parser.parse_args()

class create_dictionaries(object):
	
	def __init__(self, list):
		self.file = file
		self.list = list
	
	def search(self, string, string2):
		for x in range(0, len(self.list)):
			file = open("car_data/%s.txt" % self.list[x], "r")
			lines = file.readlines()
			for line in lines:
				if string in line:
					print(line)
				if string2 in line:
					print(line)
			file.close()
			
		
def main():
	list = lexus_ids.ids
	data = create_dictionaries(list)
	string = 'param'
	string2 = 'short cXenseParse'
	data.search(string, string2)


if __name__ == '__main__':
	main()
