#!/usr/bin/python3
"""Test for Review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8
from os import getenv


class TestReview(unittest.TestCase):
    """This will test the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.review = Review()
        cls.review.place_id = "4321-dcba"
        cls.review.user_id = "123-bca"
        cls.review.text = "The strongest in the Galaxy"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test this will tear it down"""
        del cls.review

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Tests pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring(self):
        """Checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Checking if Review has attributes C=Created U=Updated"""
        review_attrs = ["id", "C_at", "U_at", "place_id", "user_id", "text"]
        for attr in review_attrs:
            self.assertTrue(attr in self.review.__dict__)

    def test_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute type for Review"""
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "db storage")
    def test_save(self):
        """Test if the save works"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.review), True)


if __name__ == "__main__":
    unittest.main()
