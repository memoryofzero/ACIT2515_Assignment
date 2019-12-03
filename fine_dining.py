from abstract_restaurant import AbstractRestaurant
from sqlalchemy import Column, Integer, String

class FineDining(AbstractRestaurant):
    """specific type of restaurant, fine dining"""

    RESTAURANT_TYPE = 'fine dining'

    num_michelin_stars = Column(Integer)
    chef_name = Column(String(100))

    def __init__(self, name, num_employees, location, year_opened, num_michelin_stars, chef_name):
        """construct fine dining restaurant"""
        super().__init__(name, num_employees, location, year_opened, FineDining.RESTAURANT_TYPE)
        if type(num_michelin_stars) != int or num_michelin_stars == None:
            raise ValueError('Invalid num_michelin_stars')
        if type(chef_name) != str or chef_name == None or chef_name == '':
            raise ValueError('Invalid chef_name')

        self.num_michelin_stars = num_michelin_stars
        self.chef_name = chef_name

    def get_details(self):
        """returns brief description"""
        return "{} ({} Michelin Stars) was opened in {} at {}. It has {} employees, with {} as chef.".format(self.name,
                                                                                                             str(self.num_michelin_stars),
                                                                                                             str(self.year_opened),
                                                                                                             self.location,
                                                                                                             str(self.num_employees),
                                                                                                             self.chef_name)

    def to_dict(self):
        """return a dictionary representation of the restaurant"""
        fine_dining = {"id": self.id,
                       "name": self.name,
                       "num_employees": self.num_employees,
                       "location": self.location,
                       "year_opened": self.year_opened,
                       "num_michelin_stars": self.num_michelin_stars,
                       "chef_name": self.chef_name,
                       "type": self.RESTAURANT_TYPE}
        return fine_dining
