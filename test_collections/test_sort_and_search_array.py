import unittest
from array import array

from fun_with_collections import sort_and_search_array as ss


class MyTestCase(unittest.TestCase):
    def test_itemFound(self):
        self.assertEqual(ss.search_array(), 2)

    def test_itemNotFound(self):
        self.assertEqual(ss.search_array(), "-1")

    def test_sortList(self):
        self.assertEqual(ss.sort_array(), array('d', [11.5, 15.5, 20.5, 30.5]))


if __name__ == '__main__':
    unittest.main()
