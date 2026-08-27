# test_driftgateway.py
"""
Tests for DriftGateway module.
"""

import unittest
from driftgateway import DriftGateway

class TestDriftGateway(unittest.TestCase):
    """Test cases for DriftGateway class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DriftGateway()
        self.assertIsInstance(instance, DriftGateway)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DriftGateway()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
