#HW6 unittest

import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}
        
        add_inventory(inventory, "Widget1", 10)
        self.assertEqual(inventory["Widget1"], 10)
        add_inventory(inventory, "Widget1", 25)
        self.assertEqual(inventory["Widget1"], 35)
        add_inventory(inventory, "Widget1", -10)
        self.assertEqual(inventory["Widget1"], 25)

    def test_remove_inventory_widget(self):
        inventory = {}
        
        add_inventory(inventory, "Widget1", 10)
        add_inventory(inventory, "Widget2", 25)
        remove_inventory_widget(inventory, "Widget1")
        self.assertEqual(inventory.__len__(), 1)
        self.assertEqual(inventory["Widget2"], 25)
