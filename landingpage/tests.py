from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('hola_mundo'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        response = self.client.get(reverse('hola_mundo'))
        self.assertContains(response, "<h1>Hola Mundo CI CD TRADICIONAL con GITHUB ACTIONS</h1>")
