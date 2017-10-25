from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class web_check():
    
    def __init__(self):
        return
        
    def request(self, uri):
        opts = Options()  # create opts object
        opts.add_argument("user-agent=Chrome/61.0.3163.100")  # set useragent to chrome
        self = webdriver.Chrome(chrome_options=opts)  # create browser object
        self.get(uri)
        print('Waiting 5 seconds..')  # wait for browser to load
        time.sleep(5)
        print('Closing browser')
        self.execute_script("return document.body.innerHTML")
        info = self.execute_script("return document.body.innerHTML")
        print(info)
        print('Script executed')
        content = self.find_elements_by_xpath("//a[@class='link']")
        return content
        self.close()

    def print_index(self, link):
        list_count = len(link)
        for x in range(0, list_count -1):
            print(link[list_count -1].text)
            list_count -= 1
        print('Print finished')
                   
   
def main():
    uri = 'https://www.ksl.com/auto/search/index?make=Lexus&model=IS+300'
    browser = web_check()
    link = browser.request(uri)
    browser.print_index(link)
    
    #fset = data.find_elements_by_xpath("//a[@class='link']")
 

    
if __name__ == '__main__':
    main()
    



