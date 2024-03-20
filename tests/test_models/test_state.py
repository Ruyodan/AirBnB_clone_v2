#!/usr/bin/python3
"""Test for State"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8
from os import getenv


class TestState(unittest.TestCase):
    """This will test the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test this will tear it down"""
        del cls.state

    def tearDown(self):
        """Teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Tests pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstring(self):
        """Checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes(self):
        """Checking if State has attributes"""
        state_attrs = ["id", "created_at", "updated_at", "name"]
        for attr in state_attrs:
            self.assertTrue(attr in self.state.__dict__)

    def test_subclass(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types(self):
        """Test attribute type for State"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "db storage")
    def test_save(self):
        """Test if the save works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """Test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
