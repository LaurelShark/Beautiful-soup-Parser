import requests
import re
from bs4 import BeautifulSoup, Comment



try:
    data = requests.get("https://www.london.gov.uk/talk-london/economy-skills-work/what-does-brexit-mean-london?page=1&action")
    soup = BeautifulSoup(data.content, 'html.parser')
    #print(soup.prettify())
    usernames_spans = soup.findAll('span', class_='username')
    list_of_usernames = []
    for i in range(0, len(usernames_spans)):
        list_of_usernames.append(usernames_spans[i].get_text())
    comments = soup.find('div', class_='comment-body')
    #print(list_of_usernames)
    print(comments)
except ValueError:
    print("getting data failded")


# soup = BeautifulSoup(data, 'lxml')
# for comment in soup.findAll(text=lambda text:isinstance(text,Comment)):
#     print (comment)

#   count_of_occurence = soup.find(text=re.compile(r"\bregister\b"))
#     print(count_of_occurence)
#
