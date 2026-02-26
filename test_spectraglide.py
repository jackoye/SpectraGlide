# test_spectraglide.py
"""
Tests for SpectraGlide module.
"""

import unittest
from spectraglide import SpectraGlide

class TestSpectraGlide(unittest.TestCase):
    """Test cases for SpectraGlide class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SpectraGlide()
        self.assertIsInstance(instance, SpectraGlide)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SpectraGlide()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
