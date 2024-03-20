#!/usr/bin/python3
"""Test for City"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
import pep8
from os import getenv


class TestCity(unittest.TestCase):
    """This will test the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Tests pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring(self):
        """Checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Checking if City has attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "db storage")
    def test_save(self):
        """Test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
