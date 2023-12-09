from django.test import Client, TestCase
from django.urls import reverse

from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from tests.mixins import UserMixin, MenuItemMixin


class SetUpMixin:

    def setUp(self):
        self.user = self.create_user(
            username = 'test@gmail.com',
            password = 'testpasswd',
        )
        self.token = self.get_token(
            username = 'test@gmail.com',
            password = 'testpasswd',
        )
        self.client = Client(HTTP_AUTHORIZATION=f'Token {self.token}')

class MenuItemViewTest(SetUpMixin, UserMixin, MenuItemMixin, TestCase):

    def setUp(self):
        self.create_menu_items()
        super().setUp()

    def test_list(self):
        response = self.client.get(reverse('menu_items'))
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create(self):
        data = {'title': 'latte', 'price': 2.99, 'inventory': 5}
        response = self.client.post(reverse('menu_items'), data=data)
        serializer = MenuSerializer(Menu.objects.get(title='latte'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)