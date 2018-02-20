from selenium import webdriver
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
binary = FirefoxBinary('') #location of firefox.exe
b = webdriver.Firefox(firefox_binary=binary)
b.get('http://web.whatsapp.com')
raw_input()
print("Success!!!")
elem = b.find_element_by_xpath('//span[contains(text(),"Deeksha")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
while True:
 elem1[1].send_keys('hi')
 b.find_element_by_class_name('send-container').click()
