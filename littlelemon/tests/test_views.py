from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(Title='Pizza', Price=9.99, Inventory=10)
        self.menu_item2 = Menu.objects.create(Title='Burger', Price=5.99, Inventory=20)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)