import requests
import csv
import sys
from bs4 import BeautifulSoup

write_to = str(input("Enter file name: "))
page_url = str(sys.argv[1])


def get_comments(url, file_name):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    # print(soup.prettify())
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

    links_list = []
    for li_pages_list in soup.findAll("li", class_="pager__item"):
        for a_blocks in li_pages_list.find_all("a"):
            href = a_blocks.attrs["href"]
            links_list.append(href)

    return list(dict.fromkeys(links_list))


try:
    urls_array = get_comments(page_url, write_to)
    if urls_array:
        for url_ending in urls_array:
            url = str('https://www.london.gov.uk' + url_ending)
            get_comments(url, write_to)


except ValueError:
    print("getting data failded")
