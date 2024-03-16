from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company


class CompanyAPITests(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Initial Company",
            description="Initial Description",
            location="Initial Location",
            operating_hours="9:00-18:00"
        )
        self.valid_data = {
            'name': 'New Company',
            'description': 'New Description',
            'location': 'New Location',
            'operating_hours': '10:00-19:00'
        }
        self.invalid_data = {
            'name': '',
            'description': 'No Name',
            'location': 'No Location',
            'operating_hours': '10:00-19:00'
        }

    def test_create_company(self):
        """
        Test for creating a company - Убедимся, что мы можем создать новое предприятие.
        """
        url = reverse('company-list')
        response = self.client.post(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)  # Проверяем, что предприятие действительно добавлено

    def test_get_company_list(self):
        """
        Test for getting a list of companies - Убедимся, что мы можем получить список предприятий.
        """
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # У нас уже есть одно предприятие из setUp

    def test_get_company_detail(self):
        """
        Test for getting a companies details - Убедимся, что мы можем получить детали конкретного предприятия.
        """
        url = reverse('company-detail', args=[self.company.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company.name)

    def test_update_company(self):
        """
        Test for updating a company - Убедимся, что мы можем обновить предприятие.
        """
        url = reverse('company-detail', args=[self.company.id])
        response = self.client.put(url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.company.refresh_from_db()
        self.assertEqual(self.company.name, 'New Company')

    def test_delete_company(self):
        """
        Test for deleting a company - Убедимся, что мы можем удалить предприятие.
        """
        url = reverse('company-detail', args=[self.company.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Company.objects.count(), 0)

    def test_create_company_invalid_data(self):
        """
        Test for creating a company with invalid data - Тестирование создания предприятия с невалидными данными.
        """
        url = reverse('company-list')
        response = self.client.post(url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

