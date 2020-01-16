import unittest
import json

from run import create_app
from Model import db


class CurrencyTestCase(unittest.TestCase):
    """This class represents the currencies test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="test")
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_currencies_creation(self):
        """Test API can get a currencues (GET request)."""
        res = self.client().post('/api/currencies')
        self.assertEqual(res.status_code, 201)

    def test_api_can_get_all_currencies(self):
        """Test API can get a currencues (GET request)."""
        res = self.client().post('/api/currencies')
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/currencies?date=2020-01-14')
        self.assertEqual(res.status_code, 200)
        resjson = json.loads(res.data.decode('utf-8').replace("'", "\""))
        self.assertIn('success', str(resjson["status"]))
        self.assertIn('EUR', str(resjson["data"][0]["base"]))

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
