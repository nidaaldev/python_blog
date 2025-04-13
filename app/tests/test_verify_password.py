from app.auth.utils import verify_password
import unittest

# python -m unittest app.tests.test_verify_password

class TestVerifyPassword(unittest.TestCase):

    def test_verify_password(self):
        # We expect this to be valid and return True
        result = verify_password("abcd1234", "$2b$12$SFp.RrEpmTkin/xsRGPM2OoobCauTnnqE4lQO0las2ehVpe8rEa8m")
        self.assertTrue(result, "Password should be verified correctly")


if __name__ == '__main__':
    unittest.main()
