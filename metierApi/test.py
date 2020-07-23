from django.test import TestCase
from metierApi.calc import add, sous


class TestCalc(TestCase):

    def test_add_number(self):
        """Test pour ajouter deux chiffres"""
        self.assertEqual(add(10,1),11)

    def test_soustract_number(self):
        """Test pour soustraire deux chiffres"""
        self.assertEqual(sous(10,1),9)