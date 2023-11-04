import random
import time

import bs4 as bs
import requests
from LoggerClass import Logger
from DishClass import Dish


class Parser:
    def __init__(self):
        self.logger = Logger('Parser')
        self.left_dish_border = 2
        self.home_url = 'https://www.russianfood.com/'
        self.chapter_url = f'https://www.russianfood.com/recipes/bytype/?fid='
        self.right_dish_border = 97
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
        self.accept_encoding = 'gzip, deflate, br'
        self.accept_language = 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7'
        self.headers = {'user-Agent': self.user_agent, 'accept-Encoding': self.accept_encoding, 'accept-Language': self.accept_language}

    def random_delay(self):
        up = random.randint(1,4)
        down = random.randint(3,8)
        time.sleep(up/down)
    def _shit_output(self, list):
        new_list = []
        for item in list:
            new_list.append(item.text.strip())
        return new_list
    def parse_dish(self, dish_url):
        response = requests.get(dish_url, headers=self.headers)
        print(response)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        raw_data = soup.find('table', class_='recipe_new')
        title_block = raw_data.find('td', class_='padding_l padding_r')
        sub_info = title_block.find('div', class_='sub_info')

        ingredients_block = raw_data.find('table', class_='ingr')
        ingredients = ingredients_block.find_all('td', class_='padding_l padding_r')
        for item in ingredients:
            print(item.text.strip())
        print('=========================================================================================================')
        users_shit = sub_info.find_all('div', class_='el')
        description = title_block.find('p').text.strip()
        title = title_block.find('h1', class_='title').text
        image_url = 'https://' + title_block.find('table', class_='main_image').find('a')['href']


        print(title, dish_url, image_url)
        print(self._shit_output(users_shit))
        print(description)
        print('=========================================================================================================')

    def _parse_page(self, page_url):
        response = requests.get(page_url, headers=self.headers)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        raw_data = bs.BeautifulSoup(str(soup), 'html.parser')
        raw_dishes = raw_data.find('div', class_='recipe_list_new')
        dishes = raw_dishes.find_all('div', class_='title')
        for dish in dishes:
            dish_url =self.home_url + dish.find('a')['href']
            self.parse_dish(dish_url)
            self.random_delay()
            #dish_object = Dish(self.parse_dish)
        return dishes

    def parse_chapters(self):
        for i in range(self.left_dish_border, self.right_dish_border + 1):
            self.logger.send_message(f'Parsing page {i}', 'info')
            page_url = self.chapter_url + str(i)
            self._parse_page(page_url)
            self.random_delay()


p = Parser()
#p.parse_chapters()
#p._parse_page('https://www.russianfood.com/recipes/bytype/?fid=2')
p.parse_dish('https://www.russianfood.com//recipes/recipe.php?rid=102711')

