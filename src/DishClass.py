class Dish:
    """
    Dish class. Contains information about dish.
    """
    def __init__(self):
        self.name = None
        self.description = None
        self.ingredients = None
        self.recipe = None
        self.cooking_time = None
        self.photo_url = None
        self.tags = None
        self.price = None

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

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

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



