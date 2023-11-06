import random
import time

import bs4 as bs
import requests
from bs4 import BeautifulSoup
from LoggerClass import Logger
from DishClass import Dish


class Parser:
    def __init__(self):
        self._logger = Logger('Parser')
        self._home_url = 'https://www.russianfood.com/'
        self._chapter_url = self._home_url + r'/recipes/bytype/?fid='
        self._current_parsing_dish_url = None
        self._left_dish_border = 2
        self._right_dish_border = 97
        self._not_found = 'Not Found'
        self._parser = 'html.parser'
        self._user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                           ' Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76'
        self._accept_encoding = 'gzip, deflate, br'
        self._accept_language = 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7'
        self._headers = {'user-Agent': self._user_agent, 'accept-Encoding': self._accept_encoding,
                         'accept-Language': self._accept_language}

    @staticmethod
    def _random_delay():
        up = random.randint(1, 4)
        down = random.randint(3, 8)
        time.sleep(up / down)

    def _get_raw_data(self, response) -> BeautifulSoup | str:
        """
        Get raw data from response
        :param response:
        :return: BeautifulSoup raw data
        """
        try:
            soup = bs.BeautifulSoup(response.text, self._parser)
            return soup.find('table', class_='recipe_new')
        except AttributeError:
            self._logger.send_message(f"Raw data not found at dish {self._current_parsing_dish_url}."
                                      f" Continue parsing...", 'error')
            return self._not_found

    def _get_recipe(self, raw_data) -> list:
        """
        Get recipe from raw data
        :param raw_data:
        :return: recipe
        """
        try:
            steps = raw_data.find_all('div', class_='step_n')
            recipe = []
            for step in steps:
                resulted_step = step.text.replace('\r', '').strip()
                resulted_step = resulted_step.replace('\n', '')
                recipe.append([resulted_step, 'https://' + step.find('a')['href']])
            return recipe
        except AttributeError:
            self._logger.send_message(f"Recipe not found at dish {self._current_parsing_dish_url}."
                                      f" Continue parsing...", 'error')
            return [self._not_found]

    def _get_title(self, raw_data) -> str:
        """
        Get title from raw data
        :param raw_data:
        :return: title
        """
        try:
            title = raw_data.find('td', class_='padding_l padding_r')
            return title.find('h1', class_='title').text
        except AttributeError:
            self._logger.send_message(f"Title not found at dish {self._current_parsing_dish_url}."
                                      f" Continue parsing...", 'error')
            return self._not_found

    def _get_sub_info(self, raw_data) -> list:
        """
        Get sub info from raw data
        :param raw_data:
        :return: sub info
        """
        try:
            sub_info = raw_data.find('div', class_='sub_info')
            users_shit = sub_info.find_all('div', class_='el')
            users_shits = []
            for shit in users_shit:
                users_shits.append(shit.text.strip())
            return users_shits
        except AttributeError:
            self._logger.send_message(f"Sub info not found at dish {self._current_parsing_dish_url}."
                                      f" Continue parsing...", 'error')
            return [self._not_found]

    def _get_ingredients(self, raw_data) -> list:
        """
        Get ingredients from raw data
        :param raw_data:
        :return: ingredients
        """
        try:
            ingredients_block = raw_data.find('table', class_='ingr')
            ingredients = ingredients_block.find_all('td', class_='padding_l padding_r')
            ingredients_list = []
            for item in ingredients:
                resulted_item = item.text.replace('\t', '').strip()
                resulted_item = resulted_item.replace('\n', '')
                ingredients_list.append(resulted_item)
            return ingredients_list
        except AttributeError:
            self._logger.send_message(f"Ingredients not found at dish {self._current_parsing_dish_url}."
                                      f" Continue parsing...", 'error')
            return [self._not_found]

    def _get_description(self, raw_data) -> str:
        """
        Get description from raw data
        :param raw_data:
        :return: description
        """
        try:
            return raw_data.find('p').text.strip()
        except AttributeError:
            self._logger.send_message(f"Description not found at dish {self._current_parsing_dish_url}."
                                      f"  Continue parsing...", 'error')
            return self._not_found

    def _get_image_url(self, raw_data) -> str:
        """
        Get image url from raw data
        :param raw_data:
        :return: image url
        """
        try:
            return 'https://' + raw_data.find('table', class_='main_image').find('a')['href']
        except AttributeError:
            self._logger.send_message(f"Image not found at dish {self._current_parsing_dish_url}."
                                      f"  Continue parsing...", 'error')
            return self._not_found

    def parse_dish(self, dish_url) -> Dish:
        """
        Parse all dish information by dish_url
        :param dish_url:
        :return: Dish
        """
        response = requests.get(dish_url, headers=self._headers)
        if response.ok:
            self._current_parsing_dish_url = dish_url
            raw_data = self._get_raw_data(response)
            title = self._get_title(raw_data)
            sub_info = self._get_sub_info(raw_data)
            ingredients = self._get_ingredients(raw_data)
            recipe = self._get_recipe(raw_data)
            description = self._get_description(raw_data)
            image = self._get_image_url(raw_data)
            dish_object = Dish(name=title, recipe=recipe, description=description, ingredients=ingredients,
                               photo_url=image, url=dish_url, sub_info=sub_info)
            return dish_object
        else:
            self._logger.send_message(f"Response is bad :( Response: {response.text}", 'error')

    def parse_page(self, page_url) -> list:
        """
        Parse all dishes from page
        :param page_url:
        :return: list of dishes at page
        """
        response = requests.get(page_url, headers=self._headers)
        if response.ok:
            raw_data = bs.BeautifulSoup(response.text, self._parser)
            raw_dishes = raw_data.find('div', class_='recipe_list_new')
            dishes = raw_dishes.find_all('div', class_='title')
            dishes_array = []
            for i, dish_item in enumerate(dishes):
                dish_url = self._home_url + dish_item.find('a')['href']
                dish_item = self.parse_dish(dish_url)
                dishes_array.append(dish_item)
                self._logger.send_message(f'Parsed dish_item {dish_item.get_url()} number {i + 1} successfully!',
                                          'info')
                self._random_delay()
            return dishes_array
        else:
            self._logger.send_message(f"Response is bad :( Response: {response.text}", 'error')

    def parse_chapters(self) -> list:
        """
        Parse all chapters at russian food website.
        :return: list of lists, consist dishes
        """
        all_dishes = []
        for i in range(self._left_dish_border, self._right_dish_border + 1):
            self._logger.send_message(f'Parsing page {i}', 'info')
            page_url = self._chapter_url + str(i)
            dishes = self.parse_page(page_url)
            all_dishes.append(dishes)
            self._random_delay()
        return all_dishes


p = Parser()
array = p.parse_page('https://www.russianfood.com/recipes/bytype/?fid=2')
for dish in array:
    print(dish.get_title(), dish.get_url())
