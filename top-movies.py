from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

path = 'C:/Users/potrykus/Downloads/chromedriver.exe'

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

titles = []
sum_votes = []
links = []
ratings = []

# scrap first 10 pages
for page_num in range(1, 10):
    website = 'https://ekino-tv.pl/movie/cat/+kategoria[17]+wersja[Lektor]+strona[' + str(page_num) + ']+'
    driver.get(website)

    # this one returns a list, its iterable
    containers = driver.find_elements(by="xpath", value='//div[@class="movies-list-item"]')
    #this one return one
    # containers = driver.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]')

    #containers is a list and container is a single element
    for container in containers:
    #    print(container.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div').text)
    #    driver.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div/text()')
        title = container.find_element(by="xpath", value='./div[@class="opis-list"]/div[@class="title"]/a').get_attribute('textContent')
        sum_vote = container.find_element(by="xpath", value='./div[@class="info-list"]/div[@class="sum-vote"]/div').get_attribute('textContent')
        rating = container.find_element(by="xpath", value='./div[@class="info-list"]/font[2]').get_attribute('textContent')
        link = container.find_element(by="xpath", value='./div[@class="opis-list"]/div[@class="title"]/a').get_attribute("href")
    #
     #   # appending each element to the list
        titles.append(title)
        sum_votes.append(sum_vote)
        ratings.append(rating)
        links.append(link)

# dictionary consist of a key and a key value pair.
my_dict = {'title': titles, 'url': links, 'vote': sum_votes, 'rating': ratings}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headlines-headless.csv')

driver.quit()
# xpath
# //div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]
# //div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div/text()
# //div[@class="movies-list-item"]/div[@class="opis-list"]/div[@class="title"]/a/text()

