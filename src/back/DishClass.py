class Dish:
    """
    Dish class. Contains information about dish.
    """
    def __init__(self, name=None, description=None, ingredients=None, recipe=None, sub_info=None, photo_url=None, tags=None, price=None, url=None, ):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.recipe = recipe
        self.sub_info = sub_info
        self.photo_url = photo_url
        self.tags = tags
        self.price = price
        self.url = url

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_ingredients(self):
        return self.ingredients

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def get_recipe(self):
        return self.recipe

    def set_recipe(self, recipe):
        self.recipe = recipe

    def get_sub_info(self):
        return self.sub_info

    def set_sub_info(self, cooking_time):
        self.sub_info = cooking_time

    def get_photo_url(self):
        return self.photo_url

    def set_photo_url(self, photo_url):
        self.photo_url = photo_url

    def get_tags(self):
        return self.tags

    def set_tags(self, tags):
        self.tags = tags

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def println(self):
        print("Название: ", self.name)
        print("Описание:", self.description)
        print("Ингредиенты: ", self.ingredients)
        print("Рецепт: ", self.recipe)
        print("Дополнительная информация: ", self.sub_info)
        print("Ссылка на фото: ", self.photo_url)
        print("Теги: ", self.tags)
        print("Цена: ", self.price)
        print("Ссылка на блюдо: ", self.url)