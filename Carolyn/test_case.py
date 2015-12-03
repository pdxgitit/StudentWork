import unittest
import cryptogramtest

class CryptoTests(unittest.TestCase):
    def setUp(self):
        self.md = cryptogramtest.make_dash

    def test_make_dash(self):
        self.assertEqual(len("Carolyn"), len(self.md("Carolyn")))

    # def test_make_new_key(self):
    #
    # def test_scramble(self, string, mapper):




if __name__ == '__main__':
    unittest.main()
