#we need to create a new module in the same directory as our project.
import unittest
import unit_testing_ex1

#Now we need to create test cases.
#for this we need to create a test class that inherits from unittest.testcase
#Look up documentation to find out about Asserts and what they check for.

class TestCalc(unittest.TestCase):

    #if a method's name doesn't start with test it won't be recognized.
    def test_add(self):
        result = unit_testing_ex1.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(unit_testing_ex1.add(-1, 1), 0) #edge case
        self.assertEqual(unit_testing_ex1.add(-1, -1), -2) #edge case
        
    
    def test_subtract(self):
        self.assertEqual(unit_testing_ex1.subtract(-1, 1), -2)
        self.assertEqual(unit_testing_ex1.subtract(10, 5), 5)
        
    def test_multiply(self):
        self.assertEqual(unit_testing_ex1.multiply(-1, 1), -1)
        self.assertEqual(unit_testing_ex1.multiply(10, 5), 50)
        self.assertEqual(unit_testing_ex1.multiply(0, 1), 0)

    def test_divide(self):
        self.assertEqual(unit_testing_ex1.divide(-1, 1), -1)
        self.assertEqual(unit_testing_ex1.divide(0, 1), 0)
        self.assertEqual(unit_testing_ex1.divide(-1, -1), 1)
        self.assertEqual(unit_testing_ex1.divide(5, 2), 2.5)

        self.assertRaises(ValueError, unit_testing_ex1.divide, 10, 0) #checking value error.

        with self.assertRaises(ValueError): #testing Value Errors using context managers.
            unit_testing_ex1.divide(10, 0)
    
#python -n unittest test_calc.py --> command to run our test

if __name__ == '__main__':
    unittest.main()
#by using above if statement we just need to run test_calc.py to run our tests.


        