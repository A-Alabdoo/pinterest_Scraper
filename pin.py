from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
import wget
web = webdriver.Chrome()

web.get('https://pinterest.de')
pins=[]

#num = input('Enter the number of photos you want to upload')
num = 100
for i in range(int(num / 20)):
    con  =web.find_elements(By.CSS_SELECTOR,'[data-test-id = "pin"]')
    for  i in con :
        try: 
            if i.get_attribute('data-test-pin-id') not in pins: # To continue if img downloaded
                pins.append(i.get_attribute('data-test-pin-id'))
                img = i.find_element(By.TAG_NAME,'img')
                #get src
                base_url = img.get_attribute('src')
                #get All Src Res..
                original_url = img.get_attribute('srcset').split(',')[-1].replace(' 4x','')
                print(original_url)
                #if IMG Has attr srcset
                if bool (img.get_attribute('srcset') )== True:
                    wget.download(url=original_url)
                elif '75x75' in base_url:
                    continue
                else: #get First Link
                    wget.download(url=base_url)
            else:
                continue
        except:
            continue
    for i in range(300):
        web.execute_script('window.scrollBy(0, 10)')
    

