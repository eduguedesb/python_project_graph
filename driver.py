from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Criando instância das opções do Chrome
options = webdriver.ChromeOptions()

# Inicializando o WebDriver
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

driver.quit()

driver_path = ChromeDriverManager().install()
print(driver_path)