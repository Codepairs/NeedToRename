import bs4 as bs
import requests
from DishClass import Dish
from LoggerClass import Logger


class Parser:
    def __init__(self):
        self.logger = Logger('Parser')
        self.left_dish_border = 1
        self.url_to_parse = f'https://www.russianfood.com/recipes/bytype/?fid='
        self.right_dish_border = 97

    def page_parse(self, page_url):
        page = requests.get(page_url)
        soup = bs.BeautifulSoup(page.text, 'html.parser')
        print(soup)
        return soup.text

    def parse(self):
        for i in range(self.left_dish_border, self.right_dish_border + 1):
            self.logger.send_message(f'Parsing page {i}')
            page_url = self.url_to_parse + str(i)
            print(self._page_parse(page_url))


p = Parser()
#p.parse()
p.page_parse('https://www.russianfood.com/recipes/bytype/?fid=2')

