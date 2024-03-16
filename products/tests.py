from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product


class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Initial Product", description="Initial Description", price=100.00, stock=50)
        self.valid_data = {'name': 'New Product', 'description': 'New Description', 'price': 50.00, 'stock': 20}
        self.invalid_data = {'name': '', 'description': 'No Name', 'price': 50.00, 'stock': 20}

    def test_create_product(self):
        """
        Test for creating a product
        """
        url = reverse('product-list')
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)  # Проверяем, что продукт действительно добавлен

    def test_get_product_list(self):
        """
        Test for getting a product list
        """
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # У нас уже есть один продукт из setUp

    def test_get_product_detail(self):
        """
        Test for getting a product details
        """
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        """
        Test for updating a product
        """
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.put(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'New Product')

    def test_delete_product(self):
        """
        Test for deleting a product
        """
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_create_product_invalid_data(self):
        """
        Test for invalid data
        """
        url = reverse('product-list')
        response = self.client.post(url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
