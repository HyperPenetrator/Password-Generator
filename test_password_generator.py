import unittest
from Password_Generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_length(self):
        pwd = generate_password(12)
        self.assertEqual(len(pwd), 12)

    def test_uppercase(self):
        pwd = generate_password(20, use_upper=True, use_digits=False, use_symbols=False)
        self.assertTrue(any(c.isupper() for c in pwd))

    def test_digits(self):
        pwd = generate_password(20, use_upper=False, use_digits=True, use_symbols=False)
        self.assertTrue(any(c.isdigit() for c in pwd))

    def test_symbols(self):
        pwd = generate_password(20, use_upper=False, use_digits=False, use_symbols=True)
        self.assertTrue(any(not c.isalnum() for c in pwd))

    def test_no_upper_digits_symbols(self):
        pwd = generate_password(20, use_upper=False, use_digits=False, use_symbols=False)
        self.assertTrue(all(c.islower() for c in pwd))

if __name__ == '__main__':
    unittest.main()
