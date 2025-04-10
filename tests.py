# tests/test_your_code.py

import unittest
from rvd_ap import rvd_ap
from io import StringIO
from unittest.mock import patch

class TestYourCode(unittest.TestCase):
    def test_some_function(self):
        result = rvd_ap.some_function()
        self.assertEqual(result, expected_result)

    def test_some_class(self):
        obj = rvd_ap.SomeClass()
        self.assertTrue(obj.some_method())

    def test_tell_it(self):
        # Capture the output of the tell_it function
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rvd_ap.tell_it()
            self.assertEqual(fake_out.getvalue().strip(), "Git Integration is working pucca")

if __name__ == '__main__':
    unittest.main()
