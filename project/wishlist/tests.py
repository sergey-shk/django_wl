from django.test import TestCase
from django.urls import reverse 
from .views import index


class IndexTestCase(TestCase):
    def test_ind(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
