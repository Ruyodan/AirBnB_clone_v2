#!/usr/bin/python3
"""Test for User"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8
from os import getenv


class TestUser(unittest.TestCase):
    """This will test the User class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmail.com"
        cls.user.password = "secret"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Tests pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring(self):
        """Checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_attributes(self):
        """Checking if User has attributes C=created U=updated FL=first last"""
        user_attrs = ["id", "C_at", "U_at", "email", "pas", "F_name", "L_name"]
        for attr in user_attrs:
            self.assertTrue(attr in self.user.__dict__)

    def test_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "db storage")
    def test_save(self):
        """Test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
