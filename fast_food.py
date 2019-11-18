from abstract_restaurant import AbstractRestaurant



class FastFood(AbstractRestaurant):
    """specific type of restaurant, fine dining"""

    RESTAURANT_TYPE = 'fast food'

    def __init__(self, name, num_employees, location, year_opened, num_locations, has_drivethrough):
        """construct fast food restaurant"""
        super().__init__(name, num_employees, location, year_opened)
        if type(num_locations) != int or num_locations == None:
            raise ValueError('Invalid num_location')
        if type(has_drivethrough) != bool or has_drivethrough == None:
            raise ValueError('Invalid has_drivethrough')
        self._num_locations = num_locations
        self._has_drivethrough = has_drivethrough

    def get_num_locations(self):
        """returns num of locations"""
        return self._num_locations

    def get_has_drivethrough(self):
        """returns if restaurant has drivethough"""
        return self._has_drivethrough

    def get_type(self):
        """returns type of restaurant"""
        return self.RESTAURANT_TYPE

    def get_details(self):
        """returns brief description"""
        if self._has_drivethrough:
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
        fast_food = {"id": self.get_id(),
                    "name": self._name,
                     "num_employees": self._num_employees,
                     "location": self._location,
                     "year_opened": self._year_opened,
                     "num_locations": self._num_locations,
                     "has_drivethrough": self._has_drivethrough,
                     "type": self.get_type()}
        return fast_food
