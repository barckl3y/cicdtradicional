from django.test import TestCase
from django.urls import reverse

class BasicTests(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('hola_mundo'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        response = self.client.get(reverse('hola_mundo'))
        self.assertContains(response, "<h1>HOLA MUNDO CON CI/CD CON GITHUB ACTIONS 18 de junio 2025 -v2</h1>")
