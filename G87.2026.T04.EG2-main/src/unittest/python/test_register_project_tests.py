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

    # INVALID TEST CASES
    # ECNV5
    def test_tc5(self):
        manager = EnterpriseManager()
        obj = manager.register_project("12345678", "PR001", "car automatic development",
                                       "HR", "1/1/2027", 50000.00)
        # self.assertTrue(obj, "")

    # ECNV3, BLNV1
    def test_tc6(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B1234567", "PR0000002", "valid texts",
                                       "Legal", "31/12/2026", 75000.00)
        # self.assertTrue(obj, "")

    # ECNV4, BLNV2
    def test_tc7(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B123456789", "PR001", "valid texts",
                                           "Legal", "31/12/2026", 75000.00)
        # self.assertTrue(obj, "")

    # ECNV4? ==> CHECK THIS IN THE EXCEL SHEET - THERE IS A MISTAKE WITH THE NUMBERING - FIX IT
    def test_tc8(self):
        manager = EnterpriseManager()
        obj = manager.register_project("712345678", "PR001", "valid texts",
                                       "Legal", "31/12/2026", 50000.00)
        # self.assertTrue(obj, "")

    # ECNV6, BLNV3
    def test_tc9(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678", "PR07", "car automatic development",
                                       "HR", "31/12/2026", 50000.00)
        # self.assertTrue(obj, "")

    # ECNV6, BLNV4
    def test_tc10(self):
        manager = EnterpriseManager()
        obj = manager.register_project("B12345678", "PRCF538FG07", "car automatic development",
                                       "HR", "31/12/2026", 50000.00)
        # self.assertTrue(obj, "")


if __name__ == '__main__':
    unittest.main()
