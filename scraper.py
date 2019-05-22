import requests
import csv
from bs4 import BeautifulSoup

file_name = str(input("Enter file name"))

try:

    data = requests.get(
        "https://www.london.gov.uk/talk-london/economy-skills-work/what-does-brexit-mean-london?page=3&action")
    soup = BeautifulSoup(data.content, 'html.parser')
    # print(soup.prettify())

    topic_name = soup.find_all("h2")[1].getText()

    names = []
    user_comments = []
    for comment_content in soup.find_all("div", class_="comment__content"):
        name = comment_content.select_one("span")
        names.append(name.text)
        for comment in comment_content.find_all("div", class_="field__item even"):
            user_phrase = ""
            for phrase in comment.find_all('p'):
                clear_phrase = phrase.text
                user_phrase += str(clear_phrase) + ". "
            # print(user_phrase)
            user_comments.append(user_phrase.replace(u'\xa0', u''))

    data_dict = dict(zip(names, user_comments))

    with open(file_name + '.csv', 'a', encoding='utf-8') as file:
        fieldnames = ['username', 'comment']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in data_dict.items():
            writer.writerow({'username': key, "comment": value})



except ValueError:
    print("getting data failded")
