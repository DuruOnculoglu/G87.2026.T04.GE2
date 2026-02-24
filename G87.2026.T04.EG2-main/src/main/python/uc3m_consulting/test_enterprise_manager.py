from unittest import TestCase
from uc3m_consulting import EnterpriseManager


class TestEnterpriseManager(TestCase):
    def test_TC1(self):
        obj = EnterpriseManager()
        value = obj.register_project("A58818501", "PR001", 'Test to validate', 'HR',
                                     '01/01/2027', 75000.00)
        self.assertEqual(value, "MD5hash")