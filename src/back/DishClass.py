class Dish:
    """
    Dish class. Contains information about dish.
    """
    def __init__(self, name=None, description=None, ingredients=None, recipe=None, sub_info=None, photo_url=None, tags=None, price=None, url=None, ):
        self._title = name
        self._description = description
        self._ingredients = ingredients
        self._recipe = recipe
        self._sub_info = sub_info
        self._photo_url = photo_url
        self._tags = tags
        self._price = price
        self._url = url

    def get_title(self):
        return self._title

    def set_title(self, name):
        self._title = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_ingredients(self):
        return self._ingredients

    def set_ingredients(self, ingredients):
        self._ingredients = ingredients

    def get_recipe(self):
        return self._recipe

    def set_recipe(self, recipe):
        self._recipe = recipe

    def get_sub_info(self):
        return self._sub_info

    def set_sub_info(self, cooking_time):
        self._sub_info = cooking_time

    def get_photo_url(self):
        return self._photo_url

    def set_photo_url(self, photo_url):
        self._photo_url = photo_url

    def get_tags(self):
        return self._tags

    def set_tags(self, tags):
        self._tags = tags

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_url(self):
        return self._url

    def set_url(self, url):
        self._url = url

    def output(self):
        print("Название: ", self._title)
        print("Ссылка: ", self._url)
        print("Фото: ", self._photo_url)
        print("Описание:", self._description)
        print("Ингредиенты: ", self._ingredients)
        print("Рецепт: ", self._recipe)
        print("Дополнительная информация: ", self._sub_info)
        print("Теги: ", self._tags)
        print("Цена: ", self._price)
