"""
Unit tests for the calculator library
"""

import test_Circle_CI
import unittest

class TestCalculator(unittest.TestCase):
#class desc
    
    def test_addition(self):
    #func desc    
        
        self.assertEqual(4, test_Circle_CI.add(2, 2))

    def test_subtraction(self):
    #func desc    
        
        self.assertEqual(2, test_Circle_CI.subtract(4, 2))

if __name__ == "__main__":
    unittest.main()
    
