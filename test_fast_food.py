from fast_food import FastFood
import unittest
import inspect

class TestFastFood(unittest.TestCase):
    """Unit tests for RestaurantManager class"""

    def setUp(self):
        """Create a test fixture and call logPoint before each test method is run"""
        self.logPoint()
        self.fastFood = FastFood('Fast Food', 10, 'Burnaby', 2010, 20, True)
        self.assertIsNotNone(self.fastFood)
        self.fastFood.set_id(0)

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
        test_fast_food = FastFood('Test', 10, 'YXX', 2009, 20, False)
        self.assertIsNotNone(self.fastFood, 'should create a fast food obj')

    def test_contructor_invalid_params(self):
        """010B: Invalid parameters"""
        self.assertRaisesRegex(ValueError, 'Invalid num_location', FastFood, 'Test', 10,'yvr', 2006, '', True)
        self.assertRaisesRegex(ValueError, 'Invalid has_drivethrough', FastFood, 'Test', 10,'yvr', 2006, 10, 90)

    def test_set_id(self):
        """020A: Set valid id"""
        self.fastFood.set_id(1)
        self.assertEquals(1, self.fastFood.get_id(), 'should return 1')

    def test_set_id_invalid(self):
        """020B: Invalid id param"""
        self.assertRaisesRegex(ValueError, 'Invalid id', self.fastFood.set_id, '')

    def test_get_id(self):
        """030A: Get valid id"""
        self.assertEquals(0, self.fastFood.get_id(), 'should return 0')

    def test_get_name(self):
        """040A: get valid name"""
        self.assertEquals('Fast Food', self.fastFood.get_name(), 'should return Fast Food')

    def test_get_num_employees(self):
        """050A: Get valid num employees"""
        self.assertEquals(10, self.fastFood.get_num_employees(), 'should return 10')

    def test_get_location(self):
        """060A: Get valid location"""
        self.assertEquals('Burnaby', self.fastFood.get_location(), 'should return Burnaby')

    def test_get_year_opened(self):
        """070A: get year opened"""
        self.assertEquals(2010, self.fastFood.get_year_opened(), 'should return 2006')

    def test_get_num_locations(self):
        """080A: Valid get num locations"""
        self.assertEquals(20, self.fastFood.get_num_locations(), 'Should return 20')

    def test_get_has_drivethrough(self):
        """090A: Valid get_has_drivethrough"""
        self.assertEquals(True, self.fastFood.get_has_drivethrough(), 'Should return true')
    def test_get_type(self):
        """100A: Get valid type"""
        self.assertEquals('fast food', self.fastFood.get_type(), 'should return fast food')

    def test_get_details(self):
        """110A: Get valid details"""
        self.assertIn('(has drive-through) was opened in 2010', self.fastFood.get_details(), 'should return matching string')

    def test_to_dict(self):
        """120A: Get valid dict"""
        self.assertIsInstance(self.fastFood.to_dict(), dict)

if __name__ == '__main__':
    unittest.main()
