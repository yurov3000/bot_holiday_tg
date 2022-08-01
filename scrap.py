# I want to say thanks https://www.calend.ru/ for the information provided :)
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Function for geting data
def get_data(url):
    html = urlopen(url)
    # print(html)
    bs4 = BeautifulSoup(html, "lxml")

    event_to_day = bs4.find("div", class_="block holidays").find("ul", class_="itemsNet")
    holidays = event_to_day.find_all("li", class_="one-two")

    titles = []
    for holiday in holidays:
        today = holiday.find("div", class_="caption").find("span", class_="title").find("a")
        title = today.get_text()
        titles.append(title)

    return titles


def get_links(url):
    html = urlopen(url)
    bs4 = BeautifulSoup(html, "lxml")

    event_to_day = bs4.find("div", class_="block holidays").find("ul", class_="itemsNet")
    holidays = event_to_day.find_all("li", class_="one-two")

    links = []
    for holiday in holidays:
        today = holiday.find("div", class_="caption").find("span", class_="title").find("a")
        link = today.get("href")
        links.append(link)

    return links


#html = 'https://www.calend.ru/'
#print(get_links(html))
#print(get_data(html))

# I want to say thanks https://www.calend.ru/ for the information provided :)
