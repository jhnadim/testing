import unittest
import math
from trigonometry import Trigonometry

class TestTrigonometry(unittest.TestCase):
    """
    A class for testing the Trigonometry class.
    """

    def setUp(self):
        self.trig = Trigonometry()

    def test_sin(self):
        self.assertAlmostEqual(self.trig.sin(math.pi/4), 0.7071067811865476)
        self.assertAlmostEqual(self.trig.sin(math.pi/2), 1.0)

    def test_sin_2(self):
        self.assertAlmostEqual(self.trig.sin(0), 0.0)
        self.assertAlmostEqual(self.trig.sin(math.pi), 0.0)

    def test_sin_3(self):
        self.assertAlmostEqual(self.trig.sin(3*math.pi/4), 0.7071067811865475)

    def test_cos(self):
        self.assertAlmostEqual(self.trig.cos(math.pi/4), 0.7071067811865476)
        self.assertAlmostEqual(self.trig.cos(math.pi/2), 0.0)

    def test_cos_2(self):
        self.assertAlmostEqual(self.trig.cos(0), 1.0)
        self.assertAlmostEqual(self.trig.cos(math.pi), -1.0)

    def test_cos_3(self):
        self.assertAlmostEqual(self.trig.cos(3*math.pi/4), -0.7071067811865475)

    def test_tan(self):
        self.assertAlmostEqual(self.trig.tan(math.pi/4), 0.9999999999999999)
        self.assertAlmostEqual(self.trig.tan(0), 0.0)


    def test_tan_2(self):
        self.assertAlmostEqual(self.trig.tan(math.pi), -1.2246467991473532e-16)
   
        
    def test_tan_3(self):
        self.assertAlmostEqual(self.trig.tan(3*math.pi/4), -0.9999999999999999)

    def test_sec(self):
        self.assertAlmostEqual(self.trig.sec(math.pi/4), 1.4142135623730951)
        self.assertAlmostEqual(self.trig.sec(0), 1.0)

        
    def test_sec_2(self):
        self.assertAlmostEqual(self.trig.sec(math.pi), -1.0)

        
    def test_sec_3(self):
        self.assertAlmostEqual(self.trig.sec(3*math.pi/4), -1.4142135623730951)

    def test_csc(self):
        self.assertAlmostEqual(self.trig.csc(math.pi/4), 1.4142135623730951)
       

    def test_csc_2(self):
        self.assertAlmostEqual(self.trig.csc(math.pi/2), 1.0)
       

    def test_csc_3(self):
        self.assertAlmostEqual(self.trig.csc(3*math.pi/4), 1.4142135623730951)

if __name__ == '__main__':
    unittest.main()