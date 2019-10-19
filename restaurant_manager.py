from abstract_restaurant import AbstractRestaurant
from restaurant_stats import RestaurantStats

class RestaurantManager:

    def __init__(self):
        """initialize restaurant manager"""
        self._restaurants = []
        self._next_available_id = int(0)

    def add(self, restaurant):
        """adds restaurant to list of restaurants"""
        if restaurant is None or not isinstance(restaurant, AbstractRestaurant):
            raise ValueError("wrong value")

        restaurant.set_id(self._next_available_id)
        self._next_available_id += 1
        self._restaurants.append(restaurant)

        return restaurant.get_id()

    def get_restaurant_by_id(self, id):
        """returns restaurant based on id"""
        if id is None or type(id) != int:
            raise ValueError("Invalid id")
        if self.restaurant_exists(id):
            for restaurant in self._restaurants:
                if restaurant.get_id() == id:
                    return restaurant
        else:
            return None

    def get_all(self):
        """returns list of all restaurants"""
        return self._restaurants

    def get_all_by_type(self, type):
        """returns list of restaurants based on type"""
        if type is None or type is '' or type(type) is not str:
            raise ValueError('Invalid type')

        restaurants_by_type = []
        for restaurant in self._restaurants:
            if restaurant.get_type() == type:
                restaurants_by_type.append(restaurant)
        return restaurants_by_type

    def restaurant_exists(self, id):
        """checks if restaurant in the list already"""
        if id is None or type(id) != int:
            raise ValueError("Invalid id")

        for restaurant in self._restaurants:
            if restaurant.get_id() == id:
                return True
        return False

    def delete(self, id):
        """remove a restaurant by id"""
        if id is None or type(id) is not int:
            raise ValueError("Invalid id")

        if self.restaurant_exists(id):
            self._restaurants.remove(self.get_restaurant_by_id(id))
        else:
            raise Exception('Restaurant with id %s does not exist' % id)

    def update(self, restaurant):
        """update a restaurant by id"""
        if restaurant is None or not isinstance(restaurant, AbstractRestaurant):
            raise ValueError("wrong value")
        temp_restaurant = self.get_restaurant_by_id(restaurant.get_id())

        if temp_restaurant != None:
            self._restaurants.remove(temp_restaurant)
            self._restaurants.append(restaurant)
        else:
            raise Exception('Restaurant update failed')

    def get_restaurant_stats(self):
        """returns restaurant stats"""
        total_num_restaurants = int(0)
        num_fine_dining = int(0)
        num_fast_food = int(0)
        avg_year_opened = float(0)

        for restaurant in self._restaurants:
            total_num_restaurants += 1
            avg_year_opened += restaurant.get_year_opened()

        for fine_dining in self.get_all_by_type('fine dining'):
            num_fine_dining += 1

        for fast_food in self.get_all_by_type('fast food'):
            num_fast_food += 1

        avg_year_opened = avg_year_opened / total_num_restaurants

        stats = RestaurantStats(total_num_restaurants, num_fine_dining, num_fast_food, avg_year_opened)
        return stats
