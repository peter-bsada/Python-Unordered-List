#!/usr/bin/env python3
# coding=utf8

""" Module for unittests """

import unittest
from unorderedlist import UnorderedList
class Testcase(unittest.TestCase):
    """
    My test class
    """

    def test_size(self):
        """
        testar Size funktion
        """
        ll = UnorderedList()
        ll.append(223)
        size = ll.append(223)
        self.assertEqual(ll.size(), size)

    def test_print(self):
        """
        testar print funktion
        """
        ll = UnorderedList()
        ll.append(321)
        print = ll.append(321)
        self.assertEqual(ll.print(), print)

    def test_asppend(self):
        """
        testar apppend funktion
        """
        ll = UnorderedList()
        hej = []
        for i in range(3, 15, 2):
            hej.append(i)
        self.assertEqual(hej[0], 3 )

    def test_remove(self):
        """
        testar remove funktion
        """
        ll = UnorderedList()
        ll.append(1)
        ll.append(2)
        print(ll.size())
        self.assertEqual(ll.remove(1), ll.size())

if __name__ == '__main__':
    unittest.main(verbosity=3)
