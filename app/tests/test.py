import unittest
from app import app
from app.api.routes import fetch_us_population_data


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()

    def test_get_menu_en(self):
        response = self.client.get('/getMenu/?locale=en')
        self.assertEqual(response.status_code, 200)

    def test_get_us_population_data(self):
        response = self.client.get('/rules/us_population_data/')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, list))

    def test_get_about(self):
        response = self.client.get('/rules/about/')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertTrue(isinstance(data, dict))

if __name__ == '__main__':
    unittest.main()
