from unittest import TestCase
from uc3m_consulting import EnterpriseManager


class TestEnterpriseManager(TestCase):
    def test_TC1(self):
        obj = EnterpriseManager()
        value = obj.register_project('A58818501', 'PR001', 'Test to validate', 'HR',
                                     '2026-01-01', '75000')
        self.assertEqual(value, "MD5hash")