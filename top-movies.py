from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://ekino-tv.pl/movie/cat/+kategoria[17]+wersja[Lektor]+/"
path = 'C:/Users/potrykus/Downloads/chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)
####################################

# used single quota and we can use different by than xpath
containers = driver.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]')

driver.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div/text()')




# xpath
# //div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]
# //div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div/text()
# //div[@class="movies-list-item"]/div[@class="opis-list"]/div[@class="title"]/a/text()
