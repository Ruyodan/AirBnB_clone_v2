#!/usr/bin/python3
"""
Test cases for the Amenity class.

This module contains unit tests for the Amenity class, which represents
an amenity for a place (e.g., WiFi, pool, etc.). The tests cover various
aspects of the class, including its attributes, methods, and inheritance
from the BaseModel class.
"""

import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up an instance of the Amenity class for testing.
        """
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the instance of the Amenity class after testing.
        """
        del cls.amenity

    def tearDown(self):
        """
        Remove the file.json file after each test case.
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """
        Test that the Amenity class conforms to PEP8 style guidelines.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style violations found")

    def test_docstrings(self):
        """
        Test that the Amenity class has docstrings.
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """
        Test that the Amenity instance has the required attributes.
        """
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass(self):
        """
        Test that the Amenity class is a subclass of BaseModel.
        """
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types(self):
        """
        Test the types of the Amenity instance attributes.
        """
        self.assertEqual(type(self.amenity.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "Skip db storage")
    def test_save(self):
        """
        Test the save method for file storage.
        """
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method.
        """
        self.assertTrue('to_dict' in dir(self.amenity))


if __name__ == "__main__":
    unittest.main()
