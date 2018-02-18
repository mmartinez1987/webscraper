import lexus_uris

class create_ids(object):
	
	def __init__(self, list):
		self.list = list
		self.id_list = []

	def search(self):
		for x in range(0, len(self.list)):
			id = self.list[x]
			id = id[13:]
			print('Adding %s to list' % id)
			self.id_list.append(id)
		return self.id_list

	def write_to_file(self):
		f = open('lexus_ids.py', 'w')
		f.write(str("ids = %s" % self.id_list))
		f.close()
			

def main():
	ids = create_ids(lexus_uris.uris)
	ids.search()
	ids.write_to_file()

if __name__ == '__main__':
	main()
