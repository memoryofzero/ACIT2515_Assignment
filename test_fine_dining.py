from fine_dining import FineDining
import unittest
import inspect

class TestFineDining(unittest.TestCase):
    """Unit tests for RestaurantManager class"""

    def setUp(self):
        """Create a test fixture and call logPoint before each test method is run"""
        self.logPoint()
        self.fineDining = FineDining('Fine Dining', 10, 'Burnaby', 2010, 3, 'Gordan')
        self.assertIsNotNone(self.fineDining)
        self.fineDining.set_id(0)

    def tearDown(self):
        """Call logPoint after each test method"""
        self.logPoint()

    def logPoint(self):
        """log current test and function"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor(self):
        """010A: Valid constructor"""
        test_fine_dining= FineDining('Test', 10, 'YXX', 2009, 1, 'Chef')
        self.assertIsNotNone(self.fineDining, 'should create a fine dining obj')

    def test_contructor_invalid_params(self):
        """010B: Invalid parameters"""
        self.assertRaisesRegex(ValueError, 'Invalid num_michelin_stars', FineDining, 'Test', 10,'yvr', 2006, '', 'HI')
        self.assertRaisesRegex(ValueError, 'Invalid chef_name', FineDining, 'Test', 10,'yvr', 2006, 2, 90)

    def test_set_id(self):
        """020A: Set valid id"""
        self.fineDining.set_id(1)
        self.assertEquals(1, self.fineDining.get_id(), 'should return 1')

    def test_set_id_invalid(self):
        """020B: Invalid id param"""
        self.assertRaisesRegex(ValueError, 'Invalid id', self.fineDining.set_id, '')

    def test_get_id(self):
        """030A: Get valid id"""
        self.assertEquals(0, self.fineDining.get_id(), 'should return 0')

    def test_get_name(self):
        """040A: get valid name"""
        self.assertEquals('Fine Dining', self.fineDining.get_name(), 'should return Fine Dining')

    def test_get_num_employees(self):
        """050A: Get valid num employees"""
        self.assertEquals(10, self.fineDining.get_num_employees(), 'should return 10')

    def test_get_location(self):
        """060A: Get valid location"""
        self.assertEquals('Burnaby', self.fineDining.get_location(), 'should return Burnaby')

    def test_get_year_opened(self):
        """070A: get year opened"""
        self.assertEquals(2010, self.fineDining.get_year_opened(), 'should return 2010')

    def test_get_num_michelin_stars(self):
        """080A: Valid get num michelin stars"""
        self.assertEquals(3, self.fineDining.get_num_michelin_stars(), 'Should return 3')

    def test_get_has_drivethrough(self):
        """090A: Valid get_chef_name"""
        self.assertEquals('Gordan', self.fineDining.get_chef_name(), 'Should return Gordan')
    def test_get_type(self):
        """100A: Get valid type"""
        self.assertEquals('fine dining', self.fineDining.get_type(), 'should return fine dining')

    def test_get_details(self):
        """110A: Get valid details"""
        self.assertIn('(3 Michelin Stars) was opened in 2010', self.fineDining.get_details(), 'should return matching string')

    def test_to_dict(self):
        """120A: Get valid dict"""
        self.assertIsInstance(self.fineDining.to_dict(), dict)

if __name__ == '__main__':
    unittest.main()
