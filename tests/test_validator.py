import unittest 

from my_package.validator import DataValidator  # type: ignore

class TestDataValidator(unittest.TestCase):
    def setUp(self):
          self.validator = DataValidator()
     
    def test_validate_email(self):
        self.assertEqual(self.validator.validate_email("aroglobal1@gmail.com"), "aroglobal1@gmail.com")

    def test_validate_phone(self):
        self.assertEqual(self.validator.validate_phone("+2348016248907"), "+2348016248907")
   

    def test_validate_date(self):
        self.assertEqual(self.validator.validate_date("11-12-2000"), "11-12-2000")

    def test_validate_url(self):
        self.assertEqual(self.validator.validate_url("http://www.payoneer.org"), "http://www.payoneer.org")

if __name__ == "__main__":
    unittest.main()