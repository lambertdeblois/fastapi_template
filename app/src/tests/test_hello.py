import unittest
from fastapi.testclient import TestClient

from ..app import create_app


class HelloTest(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(create_app())

    def test_hello(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
