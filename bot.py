from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
browser = webdriver.Firefox()
browser.get('https://www.todamateria.com.br/')

downloads = browser.find_element(By.XPATH, '//input[@id="search-text"]')
buttonClose = browser.find_element(By.XPATH, '//div[@id="close"]').click()
downloads.send_keys('polimeros')
sleep(3)
# <div id="close" class="TvD9Pc-Bz112c ZYIfFd-aGxpHf-FnSee" role="button" aria-label="Fechar" tabindex="0"><div class="Bz112c-ZmdkE"></div><svg class="Bz112c Bz112c-r9oPif" xmlns="https://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#5f6368"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"></path><path fill="none" d="M0 0h24v24H0z"></path></svg></div>
buttonPesquisa = browser.find_element(By.XPATH, '//button[@id="search-button"]').click()
# <button id="search-button" class="search-button" type="submit" value="Buscar" title="Buscar"><span class="search-icon"></span></button>
# <input id="search-text" name="s" type="text" placeholder="Busque um tema" value="" class=" js-bound">
# input_log = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
# <a class="nav-link" href="/downloads"><span>Downloads</span></a>
# https://youtu.be/Ot10qzrb13c