from lexus_check import web_check
import lexus_uris #import list

class pull_data(object):

	def __init__(self, list):
		self.list = list

	
	def create_file(self, name, data):
		name = str(name[13:])
		print(name)
		f = open('car_data/%s.txt' % name, 'w')
		print('%s file created' % name)
		f.write(data.encode('utf-8'))
		print('Data Written to file')
		f.close()
		
			
	def request(self):
		list = self.list
		for x in range(0, len(list)):
			session = web_check('https://ksl.com/%s' % list[x])
			data = session.request()
			self.create_file(list[x], data)
			



def main():
	list = lexus_uris.uris
	page = pull_data(list)
	page.request()

if __name__ == '__main__':
	main()
			
			


