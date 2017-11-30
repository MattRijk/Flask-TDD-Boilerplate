import os
import unittest

from main.app import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """inital test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass


    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
