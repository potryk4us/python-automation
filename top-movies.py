from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://ekino-tv.pl/movie/cat/+kategoria[17]+wersja[Lektor]+/"
path = 'C:/Users/potrykus/Downloads/chromedriver.exe'

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)
####################################

# used single quota, and we can use different by than xpath
# this one returns a list, its iterable
containers = driver.find_elements(by="xpath", value='//div[@class="movies-list-item"]')

#this one return one
# containers = driver.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]')


sum_votes = []
titles = []
links = []



#containers is a list and container is a single element
for container in containers:
#    print(container.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div').text)
#    driver.find_element(by="xpath", value='//div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div/text()')
    title = container.find_element(by="xpath", value='./div[@class="opis-list"]/div[@class="title"]/a').text
    sum_vote = container.find_element(by="xpath", value='./div[@class="info-list"]/div[@class="sum-vote"]/div').text
    link = container.find_element(by="xpath", value='./div[@class="opis-list"]/div[@class="title"]/a').get_attribute("href")
#
 #   # appending each element to the list
    titles.append(title)
    sum_votes.append(sum_vote)
    links.append(link)

# dictionary consist of a key and a key value pair.
my_dict = {'title': titles, 'vote': sum_votes, 'url': links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headlines-headless.csv')

driver.quit()
# xpath
# //div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]
# //div[@class="movies-list-item"]/div[@class="info-list"]/div[@class="sum-vote"]/div/text()
# //div[@class="movies-list-item"]/div[@class="opis-list"]/div[@class="title"]/a/text()

