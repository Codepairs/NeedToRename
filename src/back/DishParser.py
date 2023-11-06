import random
import time

import bs4 as bs
import requests
from LoggerClass import Logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from DishClass import Dish


class Parser:
    def __init__(self):
        self.options = Options()
        self.service, self.chrome_options = self.setup_driver()
        self.browser = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.logger = Logger('Parser')
        self.left_dish_border = 2
        self.home_url = 'https://www.russianfood.com/'
        self.chapter_url = f'https://www.russianfood.com/recipes/bytype/?fid='
        self.right_dish_border = 97
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
        self.accept_encoding = 'gzip, deflate, br'
        self.accept_language = 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7'
        self.headers = {'user-Agent': self.user_agent, 'accept-Encoding': self.accept_encoding, 'accept-Language': self.accept_language}

    def _setup_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        service = ChromeService(executable_path='C:\\Program Files (x86)\\chromedriver-win32')
        return service, chrome_options

    def random_delay(self):
        up = random.randint(1, 4)
        down = random.randint(3, 8)
        time.sleep(up/down)

    def _shit_output(self, list):
        """
        Not understandable information about dish
        """
        new_list = []
        for item in list:
            new_list.append(item.text.strip())
        return new_list

    @staticmethod
    def _get_raw_data(response):
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        return soup.find('table', class_='recipe_new')

    @staticmethod
    def _get_recipe(raw_data) -> list:
        steps = raw_data.find_all('div', class_='step_n')
        recipe = []
        for rec in steps:
            recipe.append([rec.text.strip(), 'https://' + rec.find('a')['href']])
        return recipe

    @staticmethod
    def _get_title(raw_data) -> str:
        title = raw_data.find('td', class_='padding_l padding_r')
        return title.find('h1', class_='title').text

    @staticmethod
    def _get_subinfo(raw_data) -> list:
        sub_info = raw_data.find('div', class_='sub_info')
        users_shit = sub_info.find_all('div', class_='el')
        users_shits = []
        for shit in users_shit:
            users_shits.append(shit.text.strip())
        return users_shits

    @staticmethod
    def _get_ingredients(raw_data) -> list:
        ingredients_block = raw_data.find('table', class_='ingr')
        ingredients = ingredients_block.find_all('td', class_='padding_l padding_r')
        ingredients_list = []
        for item in ingredients:
            ingredients_list.append(item.text.strip())
        return ingredients_list

    @staticmethod
    def _get_description(raw_data) -> str:
        description = raw_data.find('p').text.strip()
        return description

    @staticmethod
    def _get_image_url(raw_data) -> str:
        return 'https://' + raw_data.find('table', class_='main_image').find('a')['href']

    def parse_dish(self, dish_url):
        response = requests.get(dish_url, headers=self.headers)
        raw_data = self._get_raw_data(response)
        title = self._get_title(raw_data)
        sub_info = self._get_subinfo(raw_data)
        ingredients = self._get_ingredients(raw_data)
        recipe = self._get_recipe(raw_data)
        description = self._get_description(raw_data)
        image = self._get_image_url(raw_data)
        dish = Dish(name=title, recipe=recipe, description=description, ingredients=ingredients, photo_url=image, url=dish_url, sub_info=sub_info)
        dish.println()

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

