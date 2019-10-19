
class AbstractRestaurant:
    """abstract restaurant"""

    def __init__(self, name, num_employees, location, year_opened):
        """construct abstract restaurant"""
        if type(name) != str or name == '' or name == None:
            raise ValueError('Invalid name')
        if type(num_employees) != int or num_employees == None:
            raise ValueError('Invalid num_employees')
        if type(location) != str or location == '' or location == None:
            raise ValueError('Invalid location')
        if type(year_opened) != int or year_opened == None:
            raise ValueError('Invalid year_opened')

        self._id = None
        self._name = name
        self._num_employees = num_employees
        self._location = location
        self._year_opened = year_opened

    def set_id(self, id):
        """sets id of restaurant"""
        if type(id) != int or id is None:
            raise ValueError('Invalid id')
        self._id = id

    def get_id(self):
        """returns id of restaurant"""
        return self._id

    def get_name(self):
        """returns name of restaurant"""
        return self._name

    def get_num_employees(self):
        """returns num of employees"""
        return self._num_employees

    def get_location(self):
        """returns location of restaurant"""
        return self._location

    def get_year_opened(self):
        """returns year that restaurant was opened"""
        return self._year_opened

    def get_details(self):
        """returns brief description of the restaurant"""
        raise NotImplementedError

    def get_type(self):
        """returns type of the restaurant"""
        raise NotImplementedError
