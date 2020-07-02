import unittest
from unittest.mock import patch #TO CHECK OUR WEBSITE.
from employee_unitte import Employee

class TestEmployee(unittest.TestCase):

    #The class methods for setUpClass and tearDownClass run only once before and after the full test
    #class respectively.

    # Best Practices,
    # Tests should be isolated and not rely on other tests.
    # Test Driven Development --> Write tests before writing main code.

    # Another module called pytest is also available to perform tests.

    @classmethod
    def setUpClass(cls):
        print('Setup Class \n')
    
    @classmethod
    def tearDownClass(cls):
        print('TEAR DOWN CLASS \n')

    def setUp(self): #To avoid redundancy in creating new employess.
        self.emp1 = Employee('Corey', 'Schafer', 50000)
        self.emp2 = Employee('Thor', 'Odinson', 100000)
        #But we now need to add self to each instance/occurance.

    def tearDown(self): #have a clean slate. Delete files that you may or may not have created during the test.
        print('TearDown\n')

    #Both setUp and tearDown run before and after each test.

    def test_email(self):
        # emp1 = Employee('Corey', 'Schafer', 50000)
        # emp2 = Employee('Thor', 'Odinson', 100000)

        self.assertEqual(self.emp1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Thor.Odinson@email.com')

        self.emp1.first = 'John'
        self.emp2.first = 'Loki'

        self.assertEqual(self.emp1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp2.email, 'Loki.Odinson@email.com')

    def test_fullname(self):
        # emp1 = Employee('Corey', 'Schafer', 50000)
        # emp2 = Employee('Thor', 'Odinson', 100000)

        self.assertEqual(self.emp1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp2.fullname, 'Thor Odinson')

        self.emp1.first = 'John'
        self.emp2.first = 'Loki'

        self.assertEqual(self.emp1.fullname, 'John Schafer')
        self.assertEqual(self.emp2.fullname, 'Loki Odinson')

    def test_apply_raise(self):
        # emp1 = Employee('Corey', 'Schafer', 50000)
        # semp2 = Employee('Thor', 'Odinson', 100000)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 105000)

    
    # A gentle introduction to mocking.
    def test_monthly_schedule(self):
        with patch('employee_unitte.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Odinson/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

        