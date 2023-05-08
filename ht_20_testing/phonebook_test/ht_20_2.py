import phonebook
import unittest
import json

class TestPhonebook(unittest.TestCase):
    def test_read_data(self):
        self.assertEqual(phonebook.read_data('empty_data.json'), {})

    def test_change_data(self):pass
