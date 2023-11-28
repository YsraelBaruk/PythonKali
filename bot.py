from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
browser.get('https://www.todamateria.com.br/matematica/')

sleep(1)
# //[@id="search-text"]
downloads = browser.find_element(By.XPATH, '//input[@id="search-text"]')
downloads.clear()
downloads.send_keys('polimeros')
sleep(1)
buttonPesquisa = browser.find_element(By.XPATH, '//button[@id="search-button"]')
buttonPesquisa.click()

# clica no conteudo
clickConteudo = browser.find_element(By.XPATH, '//a[@href="/polimeros/"]')
clickConteudo.click()

# <input id="sg-feedback-radio--100" type="radio" name="checkRating" value="100">
buttonSim = browser.find_element(By.XPATH, '//input[@id="sg-feedback-radio--100"]')
buttonSim.click()

# <textarea id="feedback-improvement-comments" class="sg-feedback__comments" placeholder="Escreva aqui"></textarea>
# textArea = browser.find_element(By.XPATH, '//textarea[@id="feedback-improvement-comments"]')
# textArea.clear()
# textArea.send_keys('Conteúdo ótimo')
# sleep(1)

# <button id="feedback-improvement-submit" class="sg-feedback__improvement-submit" disabled="">Enviar</button>
# buttonEnvia = browser.find_element(By.XPATH, '//button[@id="feedback-improvement-submit"]')
# buttonEnvia.click()

# <button class="sg-print-btn sg-icon-only" title="Imprimir"><span class="icon-sg-social icon-sg-social-print"></span></button>
# buttonPrint = browser.find_element(By.XPATH, '//button[@class="sg-print-btn sg-icon-only"]')
# buttonPrint.click()

# if(time):
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
for _ in range(8):
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
# enter
# mouseInfo documento