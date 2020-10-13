import unittest
from fun_with_collections import sort_and_search_list as ss


class MyTestCase(unittest.TestCase):
    def test_itemFound(self):
        self.assertEqual(ss.search_list(), 2)

    def test_itemNotFound(self):
        self.assertEqual(ss.search_list(), "-1")


if __name__ == '__main__':
    unittest.main()
