# when you want to run the file using "python -m unittest {file_path}"


import unittest
import pandas as pd

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
    def test_dataframe(self) :
        pd.testing.assert_frame_equal(pd.DataFrame([0,0,0,0]), pd.DataFrame([0,0,0,0]))

if __name__ == '__main__':
    unittest.main()