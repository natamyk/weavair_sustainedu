import unittest
from models.user_model import User

class TestUserModel(unittest.TestCase):

    def test_update_skills(self):
        user = User(1, "Alice", ["Python"])
        user.update_skills(["Data Science"])
        self.assertIn("Data Science", user.skills)

if __name__ == '__main__':
    unittest.main()
