from abstract_restaurant import AbstractRestaurant
from sqlalchemy import Column, Integer

class FastFood(AbstractRestaurant):
    """specific type of restaurant, fine dining"""

    RESTAURANT_TYPE = 'fast food'

    num_locations = Column(Integer)
    has_drivethrough = Column(Integer)

    def __init__(self, name, num_employees, location, year_opened, num_locations, has_drivethrough):
        """construct fast food restaurant"""
        super().__init__(name, num_employees, location, year_opened, FastFood.RESTAURANT_TYPE)
        if type(num_locations) != int or num_locations == None:
            raise ValueError('Invalid num_location')
        if type(has_drivethrough) != bool or has_drivethrough == None:
            raise ValueError('Invalid has_drivethrough')
        self.num_locations = num_locations
        self.has_drivethrough = has_drivethrough

    def get_details(self):
        """returns brief description"""
        if self._has_drivethrough == AbstractRestaurant.BOOLEAN_TRUE:
            return "{} (has drive-through) was opened in {} at {}. It has {} employees and {} locations.".format(
                self._name,
                str(self._year_opened),
                self._location,
                str(self._num_employees),
                str(self._num_locations), )
        else:
            return "{} (doesn't have drive-through) was opened in {} at {}. It has {} employees and {} locations.".format(
                self._name,
                str(self._year_opened),
                self._location,
                str(self._num_employees),
                str(self._num_locations), )

    def to_dict(self):
        """returns a dictionary representation of the restaurant"""
        fast_food = {"id": self.id,
                    "name": self.name,
                     "num_employees": self.num_employees,
                     "location": self.location,
                     "year_opened": self.year_opened,
                     "num_locations": self.num_locations,
                     "has_drivethrough": self.has_drivethrough,
                     "type": self.RESTAURANT_TYPE}
        return fast_food
