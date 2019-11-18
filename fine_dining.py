from abstract_restaurant import AbstractRestaurant



class FineDining(AbstractRestaurant):
    """specific type of restaurant, fine dining"""

    RESTAURANT_TYPE = 'fine dining'

    def __init__(self, name, num_employees, location, year_opened, num_michelin_stars, chef_name):
        """construct fine dining restaurant"""
        super().__init__(name, num_employees, location, year_opened)
        if type(num_michelin_stars) != int or num_michelin_stars == None:
            raise ValueError('Invalid num_michelin_stars')
        if type(chef_name) != str or chef_name == None or chef_name == '':
            raise ValueError('Invalid chef_name')

        self._num_michelin_stars = num_michelin_stars
        self._chef_name = chef_name

    def get_num_michelin_stars(self):
        """returns num of michelin stars"""
        return self._num_michelin_stars

    def get_chef_name(self):
        """returns name of the chef"""
        return self._chef_name

    def get_type(self):
        """returns type of restaurant"""
        return self.RESTAURANT_TYPE

    def get_details(self):
        """returns brief description"""
        return "{} ({} Michelin Stars) was opened in {} at {}. It has {} employees, with {} as chef.".format(self._name,
                                                                                                             str(self._num_michelin_stars),
                                                                                                             str(self._year_opened),
                                                                                                             self._location,
                                                                                                             str(self._num_employees),
                                                                                                             self._chef_name)

    def to_dict(self):
        """return a dictionary representation of the restaurant"""
        fine_dining = {"id": self.get_id(),
                       "name": self._name,
                       "num_employees": self._num_employees,
                       "location": self._location,
                       "year_opened": self._year_opened,
                       "num_michelin_stars": self._num_michelin_stars,
                       "chef_name": self._chef_name,
                       "type": self.get_type()}
        return fine_dining
