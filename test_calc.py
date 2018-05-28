import unittest
import calc

class TestCalc(unittest.TestCase):

  def test_add(self):
    result = calc.add(10,5)
    self.assertEqual(result, 15)

  def test_divide(self):
    resultD = calc.divide(15,5)
    self.assertEqual(resultD, 3)

  def test_substract(self):
    resultS = calc.subtract(10,5)
    self.assertEqual(resultS, 5)

if __name__ == '__main__':
  unittest.main()