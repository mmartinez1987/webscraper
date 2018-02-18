from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class web_check(object):
    
	def __init__(self, uri):
        	self.uri = uri
		self.data = ''
		self.results = []
        
	def request(self):
		opts = Options()  # create opts object
		opts.add_argument("user-agent=Chrome/61.0.3163.100")  # set useragent to chrome
		request = webdriver.Chrome(chrome_options=opts)  # create browser object
		request.get(self.uri)
		print('Waiting 5 seconds..')  # wait for browser to load
		time.sleep(5)
		print('Closing browser')
		request.execute_script("return document.body.innerHTML")
		self.data = request.execute_script("return document.body.innerHTML")
	
		request.close()
		return self.data
	
	def get_uri(self):
		return self.uri

	def print_index(self, link):
        	list_count = len(link)
        	for x in range(0, list_count -1):
                	print(link[list_count -1].text)
            		list_count -= 1
        	print('Print finished')

	def write_to_file(self):
		f = open('lexus_data.txt','w')
		print(self.data)
		f.write(self.data.encode('utf-8'))
		f.close()
		print('Data written to file successfully')                  
   

def main():
	uri = 'https://www.ksl.com/auto/search/index?make=Lexus&model=IS+300'
	browser = web_check(uri)
	browser.request()
	browser.write_to_file()
	
    
 

    
if __name__ == '__main__':
    main()
    



