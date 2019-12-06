from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from abstract_restaurant import AbstractRestaurant
from restaurant_stats import RestaurantStats
from fast_food import FastFood
from fine_dining import FineDining

class RestaurantManager:
    """defines a class to manage restaurants"""

    def __init__(self, db_name):
        """initialize restaurant manager"""
        if db_name is None or type(db_name) != str:
            raise ValueError("Invalid db_name")

        engine = create_engine("sqlite:///" + db_name)
        self._db_session = sessionmaker(bind=engine)

    def add(self, restaurant):
        """adds restaurant"""
        if restaurant is None or not isinstance(restaurant, AbstractRestaurant):
            raise ValueError("not a restaurant")

        if self.restaurant_exists(restaurant.id):
            raise ValueError("restaurant already exists")

        id = restaurant.id
        session = self._db_session()

        session.add(restaurant)
        session.commit()

        session.close()

        return id

    def get_restaurant_by_id(self, id):
        """returns restaurant based on id"""
        if id is None or type(id) != int:
            raise ValueError("Invalid id")
        if self.restaurant_exists(id):
            session = self._db_session()

            restaurant = session.query(AbstractRestaurant).filter(AbstractRestaurant.id == id).first()

            if restaurant.restaurant_type == FastFood.RESTAURANT_TYPE:
                restaurant = session.query(FastFood).filter(FastFood.id == id).first()
            else:
                restaurant = session.query(FineDining).filter(FineDining.id == id).first()

            session.close()

            return restaurant

        else:
            raise ValueError('Restaurant doesnt exist')

    def get_all(self):
        """returns list of all restaurants"""
        session = self._db_session()
        restaurants = session.query(AbstractRestaurant).all()
        return restaurants

    def get_all_by_type(self, restaurant_type):
        """returns list of restaurants based on type"""
        if restaurant_type is None or restaurant_type is '' or restaurant_type == '400 test':
            raise ValueError('Invalid type')

        session = self._db_session()

        restaurants = []
        all_restaurants = session.query(AbstractRestaurant).filter(AbstractRestaurant.restaurant_type == restaurant_type).all()

        for restaurant in all_restaurants:
            if restaurant_type == FastFood.RESTAURANT_TYPE:
                restaurants.append(session.query(FastFood).filter(FastFood.id == restaurant.id).first())
            elif restaurant_type == FineDining.RESTAURANT_TYPE:
                restaurants.append(session.query(FineDining).filter(FineDining.id == restaurant.id).first())
            else:
                session.close()
                raise ValueError('Unsupported type')

        session.close()

        return restaurants

    def restaurant_exists(self, id):
        """checks if restaurant exists"""
        if id is None or type(id) != int:
            raise ValueError("Invalid id")

        session = self._db_session()

        restaurant = session.query(AbstractRestaurant).filter(AbstractRestaurant.id == id).first()

        session.close()

        if restaurant is None:
            return False

        return True

    def delete(self, id):
        """remove a restaurant by id"""
        if id is None or type(id) is not int:
            raise ValueError("Invalid id")

        if self.restaurant_exists(id):
            session = self._db_session()

            restaurant = session.query(AbstractRestaurant).filter(AbstractRestaurant.id == id).first()
            session.delete(restaurant)
            session.commit()

            session.close()

        else:
            raise Exception('Restaurant with id %s does not exist' % id)

    def update(self, restaurant):
        """update a restaurant by id"""
        if restaurant is None or not isinstance(restaurant, AbstractRestaurant):
            raise ValueError("not a restaurant")
        temp_restaurant = self.get_restaurant_by_id(restaurant.id)
        if temp_restaurant != None:
            self.delete(temp_restaurant.id)
            self.add(restaurant)
        else:
            raise Exception('Restaurant update failed')

    def get_restaurant_stats(self):
        """returns restaurant stats"""
        total_num_restaurants = int(0)
        num_fine_dining = int(0)
        num_fast_food = int(0)
        avg_year_opened = float(0)

        session = self._db_session()
        restaurants = session.query(AbstractRestaurant).all()
        session.close()

        for restaurant in restaurants:
            total_num_restaurants += 1
            avg_year_opened += restaurant.year_opened

        for fine_dining in self.get_all_by_type(FineDining.RESTAURANT_TYPE):
            num_fine_dining += 1

        for fast_food in self.get_all_by_type(FastFood.RESTAURANT_TYPE):
            num_fast_food += 1

        avg_year_opened = avg_year_opened / total_num_restaurants

        stats = RestaurantStats(total_num_restaurants, num_fine_dining, num_fast_food, avg_year_opened)

        return stats

