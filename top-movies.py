from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://ekino-tv.pl/movie/cat/+kategoria[17]+wersja[Lektor]+/"
path = 'C:/Users/potrykus/Downloads/chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)