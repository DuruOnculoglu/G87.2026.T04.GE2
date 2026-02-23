"""class for testing the regsiter_order method"""
import unittest
from datetime import datetime

import uc3m_consulting
from uc3m_consulting import EnterpriseManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_something( self ):
        """dummy test"""
        self.assertTrue(True, True)

    def test_tc1(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","PRO01", "car automatic development",
        "HR", "01/01/2027", 600000.00)
        self.assertTrue(obj,"af6c439801893f25b2d1d023ea9fe470" )

    def test_tc2(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","890478", "valid texts",
        "Finance", str(datetime.today().strftime("%d/%m/%Y")), 50000.01)
        self.assertTrue(obj,"af6c439801893f25b2d1d023ea9fe470" )

    def test_tc3(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","PR0000002", "valid textvalid textvalid tex",
        "Legal", "31/12/2027", 999999.99)
        self.assertTrue(obj,"af6c439801893f25b2d1d023ea9fe470" )

    def test_tc4(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678","PRCF538FG0", "valid text",
        "Logistics", "31/12/2026", 1000000.00)
        self.assertTrue(obj,"af6c439801893f25b2d1d023ea9fe470" )

if __name__ == '__main__':
    unittest.main()
