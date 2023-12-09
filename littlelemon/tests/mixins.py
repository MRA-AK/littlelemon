from django.test import Client
from restaurant.models import Menu

from random import randint

MENU_ITEMS = {
    1: {'title': 'ApplePie', 'price': 13.78, 'inventory': randint(0, 11)},
    2: {'title': 'VanillaLatte', 'price': 3.99, 'inventory': randint(0, 11)},
    3: {'title': 'Icecream', 'price': 5.00, 'inventory': randint(0, 11)},
    4: {'title': 'IrishCoffe', 'price': 7.89, 'inventory': randint(0, 11)},
}


class UserMixin:

    def create_user(self, username, password):
        url = 'http://localhost:8000/auth/users/'
        data = {
            'username': username,
            'password': password,
        }
        response = Client().post(url, data=data)
        return response

    def get_token(self, username, password):
        url = 'http://localhost:8000/auth/token/login/'
        data = {
            'username': username,
            'password': password,
        }
        token = Client().post(url, data=data).data.get('auth_token')
        return token

    def get_auth_header(self, token):
        return {'Authorization': f'Token {token}'}


class MenuItemMixin:
    items = MENU_ITEMS

    def create_menu_items(self):
        for idx in self.items.keys():
            item = Menu.objects.create(
                title = self.items[idx]['title'],
                price = self.items[idx]['price'],
                inventory = self.items[idx]['inventory']
            )
            item.save()
