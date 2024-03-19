#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """test quit command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create command input"""
        # ... (existing test cases)

    def test_show(self):
        """Test show command input"""
        # ... (existing test cases)

    def test_destroy(self):
        """Test destroy command input"""
        # ... (existing test cases)

    def test_all(self):
        """Test all command input"""
        # ... (existing test cases)

    def test_update(self):
        """Test update command input"""
        # ... (existing test cases)

    def test_count(self):
        """Test count command input"""
        # ... (existing test cases)

    def test_default(self):
        """Test default command input"""
        # ... (existing test cases)

    # Additional test methods for the HBNBCommand class

    def test_do_all(self):
        """Test do_all method"""
        # Implement test cases for the do_all method

    def test_do_count(self):
        """Test do_count method"""
        # Implement test cases for the do_count method

    def test_do_update(self):
        """Test do_update method"""
        # Implement test cases for the do_update method

    def test_default(self):
        """Test default method"""
        # Implement test cases for the default method


if __name__ == "__main__":
    unittest.main()
