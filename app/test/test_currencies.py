import unittest
import os
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
        resJson = json.loads(res.data.decode('utf-8').replace("'", "\""))
        self.assertIn('success', str(resJson["status"]))
        self.assertIn('EUR', str(resJson["data"][0]["base"]))

    def tearDown(self):
     #   """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()