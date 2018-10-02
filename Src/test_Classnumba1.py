"""
Nicholas Newman
CS551SE
09/30/2018
Class Analytics Engine Test File
"""
import unittest
from Classnumba1 import classnumba1 

class Testclassnumba1(unittest.TestCase):
    def test_init(self):
        TheMainClass = classnumba1()
        self.assertEqual(len(TheMainClass.data), 89)

    def test_total_avg(self):
        TheMainClass = classnumba1()
        self.assertEqual(TheMainClass.total_avg(), 3.0)

    def test_total_mid_avg(self):
        TheMainClass = classnumba1()
        self.assertEqual(TheMainClass.total_mid_avg(), 2.0)

    def test_total_change(self):
        TheMainClass = classnumba1()
        self.assertEqual(TheMainClass.total_change(), -1.0)

    def test_total_grade_count(self):
        TheMainClass = classnumba1()
        self.assertEqual(TheMainClass.total_grade_count(), [43, 25, 13, 2, 6])

    def test_total_sex(self):
        TheMainClass = classnumba1()
        self.assertEqual(TheMainClass.total_sex(), [72, 17])

if __name__ == '__main__':
    unittest.main()