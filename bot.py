from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from time import sleep

browser = webdriver.Firefox(service=Service(r'C:\geckodriver\geckodriver.exe'))
# browser = webdriver.Firefox()
browser.get('http://google.com/')
search = browser.find_element(By.XPATH, '//textarea[@id="APjFqb"]')
search.clear()
search.send_keys('Uma pesquisa comum')
search.send_keys(Keys.ENTER)
sleep(10)
browser.quit()