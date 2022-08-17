import requests
from bs4 import BeautifulSoup
import time


'''                Функция парсинга РИА новости                '''

def parse_ria():
    URL = "https://ria.ru/world/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.findAll("a", class_="list-item__title color-font-hover-only")
    news = []
    for card in cards:
        time.sleep(0.1)
        text = card.text.strip()
        link = card.get("href")
        new = []
        new.append(text)
        new.append(link)
        news.append(new)
    return news


'''           Функция парсинга Кинопоиска         '''

def parse_kino():
    URL = "https://www.kinopoisk.ru/media/news/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.findAll("div", class_="_2RiC7vJoIfsgbZgo3IYhdM posts-grid__post VtnR3gLBt2s28hpqlbOQX")
    news = []
    for card in cards:
        time.sleep(0.1)
        try:
            text = card.find("h3", class_="_3-myKTe_VSc_aeMcGWCat1 Q_ZsXk_1Blta6tCxFn1UX _1V0Z9RpAohOC841uVqsDjJ _1y_4Uv4LmV6e3OaRQWjzvM").find("span").text.strip()
            link = "https://www.kinopoisk.ru/" + card.find("a", class_="_2mhHALgPiuhrRWWyp4q-e7").get("href")
        except:
            pass
        new = []
        new.append(text)
        new.append(link)
        news.append(new)
    return news


'''           Функция парсинга новостей спорта             '''
    
def parse_sport():
    URL = "https://www.gazeta.ru/sport/news/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.findAll("div", class_="m_techlisting")
    news = []
    for card in cards:
        time.sleep(0.1)
        try:
            text = card.find("div", class_="b_ear-title").find("a").text.strip().replace('\xa0', ' ')
            link = "https://www.gazeta.ru" + card.find("div", class_="b_ear-title").find("a").get("href")
        except:
            pass
        new = []
        new.append(text)
        new.append(link)
        news.append(new)
    return news


'''                Функция парсинга новостей видеоигры                   '''

def parse_games():
    URL = "https://www.igromania.ru/news/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.findAll("div", class_="aubl_item")
    news = []
    for card in cards:
        time.sleep(0.1)
        try:
            text = card.find("a", class_="aubli_name").text.strip()
            link = "https://www.igromania.ru" + card.find("a", class_="aubli_name").get("href")
        except:
            pass
        new = []
        new.append(text)
        new.append(link)
        news.append(new)
    return news


'''                Функция парсинга новостей технологий                   '''

def parse_tecnology():
    URL = "https://ria.ru/technology/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    cards = soup.findAll("a", class_="list-item__title color-font-hover-only")
    news = []
    for card in cards:
        time.sleep(0.1)
        text = card.text.strip()
        link = card.get("href")
        new = []
        new.append(text)
        new.append(link)
        news.append(new)
    return news







