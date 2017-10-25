from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
opts.add_argument("user-agent=Chrome/61.0.3163.100")
browser = webdriver.Chrome(chrome_options=opts)
lexus_results = 'https://www.ksl.com/auto/search/index?make=Lexus&model=IS+300'

browser.get(lexus_results)
print('Waiting 5 seconds..')
time.sleep(5)

browser.execute_script("return document.body.innerHTML")

fset = browser.find_elements_by_xpath("//a[@class='link']")
listing = browser.find_elements_by_xpath("//a/href[contains=('/auto/listing/')]")

fset_count = len(fset)
listing_count = len(listing)

print(fset_count)
print(listing_count)

for x in range(0, fset_count-1):
  print(fset[fset_count - 1].text)
  fset_count -= 1

for x in range(0, listing_count-1):
  print(listing[listing_count-1].text)
  listing_count -=1

browser.close()