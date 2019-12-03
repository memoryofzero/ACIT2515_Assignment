from restaurant_manager import RestaurantManager
from fast_food import FastFood
from fine_dining import FineDining
from restaurant_stats import RestaurantStats
from sqlalchemy import create_engine
from base import Base
import unittest
import inspect
import os

class TestRestaurantManager(unittest.TestCase):
    """Unit tests for RestaurantManager class"""

    def setUp(self):
        """Create a test fixture and call logPoint before each test method is run"""
        engine = create_engine('sqlite:///test_restaurants.sqlite')
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.restaurantManager = RestaurantManager('test_restaurants.sqlite')
        self.assertIsNotNone(self.restaurantManager)
        self.fastFood = FastFood('Fast Food', 10, 'Burnaby', 2010, 20, True)
        self.fineDining = FineDining('Fine Dining', 15, 'Vancouver', 2014, 3, 'John')
        self.fastFood.id = 0
        self.fineDining.id = 1
        self.restaurantManager.add(self.fastFood)
        self.restaurantManager.add(self.fineDining)
        self.logPoint()

    def tearDown(self):
        """Call logPoint after each test method"""
        os.remove('test_restaurants.sqlite')
        self.logPoint()

    def logPoint(self):
        """log current test and function"""
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_constructor(self):
        """TRM-010A: Valid Construction"""
        test_manager = RestaurantManager('test_restaurants.sqlite')
        self.assertIsNotNone(test_manager, "RestaurantManager must be defined")

    def test_invalid_constructor(self):
        """TRM-010B: Invalid filepath"""
        self.assertRaisesRegex(ValueError, 'Invalid db_name', RestaurantManager, None)

    def test_add(self):
        """TRM-020A: Valid add restaurant"""
        test_fine_dining = FineDining('Test', 20, 'YKK', 1980, 2, 'Bob')
        test_fine_dining.id = 2
        test_fast_food = FastFood('Test', 10, 'YXX', 1990, 30, False)
        test_fast_food.id = 3
        self.assertEquals(2, self.restaurantManager.add(test_fine_dining), 'Should return 2')
        self.assertEquals(3, self.restaurantManager.add(test_fast_food), 'Should return 3')

    def test_add_invalid_restaurant(self):
        """TRM-020B: Invalid restaurant obj"""
        self.assertRaisesRegex(ValueError, 'not a restaurant', self.restaurantManager.add, None)

    def test_get_restaurant_by_id(self):
        """TRM-030A: Valid get restaurant by id"""
        self.assertEquals(0, self.restaurantManager.get_restaurant_by_id(0).id, 'Should return the fastFood object')
        self.assertEquals(1, self.restaurantManager.get_restaurant_by_id(1).id, 'Should return the fineDining object')

    def test_get_restaurant_by_id_invalid_id(self):
        """TRM-030B: Invalid id"""
        self.assertRaisesRegex(ValueError, 'Invalid id', self.restaurantManager.get_restaurant_by_id, 'hi')

    def test_get_restaurant_by_id_no_restaurant(self):
        """TRM-030C: No restaurant with id"""
        self.assertRaisesRegex(ValueError, 'Restaurant doesnt exist', self.restaurantManager.get_restaurant_by_id, 5)

    def test_get_all(self):
        """TRM-040A: Valid get all"""
        self.assertIs(list, type(self.restaurantManager.get_all()), 'Should return type list')

    def test_get_all_by_type(self):
        """TRM-050A: Valid get all by type"""
        self.assertEquals([self.fastFood], self.restaurantManager.get_all_by_type('fast food'), 'should return list with fastFood obj')

    def test_get_all_by_type(self):
        """TRM-050B: Invalid type"""
        self.assertRaisesRegex(ValueError, 'Invalid type', self.restaurantManager.get_all_by_type, '')

    def test_restaurant_exists(self):
        """TRM-060A: Valid restaurant exists"""
        self.assertEquals(True, self.restaurantManager.restaurant_exists(0), 'Should return true')
        self.assertEquals(False, self.restaurantManager.restaurant_exists(10), 'Should return false')

    def test_restaurant_exists_invalid_id(self):
        """TRM-060B: Invalid id param"""
        self.assertRaisesRegex(ValueError, 'Invalid id', self.restaurantManager.restaurant_exists, '')

    def test_delete(self):
        """TRM-070A: Valid delete"""
        self.restaurantManager.delete(0)
        self.restaurantManager.delete(1)

        self.assertEquals([], self.restaurantManager.get_all(), 'Should return empty list')

    def test_delete_invalid_id(self):
        """TRM-070B: Invalid id"""
        self.assertRaisesRegex(ValueError, 'Invalid id', self.restaurantManager.delete, '')

    def test_update(self):
        """TRM-080A: Valid update"""
        test_fast_food = FastFood('Test', 10, 'YXX', 1990, 30, False)
        test_fast_food.id = 0
        self.restaurantManager.update(test_fast_food)
        self.assertEquals('Test', self.restaurantManager.get_restaurant_by_id(0).name, 'should return the test_fast_food obj')

    def test_update_invalid_restaurant(self):
        """TRM-080A: Invalid restaurant"""
        self.assertRaisesRegex(ValueError, 'not a restaurant', self.restaurantManager.update, '')

    def test_get_restaurant_stats(self):
        """TRM-090A: Return RestaurantStats object"""
        self.assertIsInstance(self.restaurantManager.get_restaurant_stats(), RestaurantStats, 'should return RestaurantStats object')

if __name__ == '__main__':
    unittest.main()

