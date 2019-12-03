from sqlalchemy import Column, String, Integer
from base import Base

class AbstractRestaurant(Base):
    """abstract restaurant"""

    BOOLEAN_TRUE = 1

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    num_employees = Column(Integer)
    location = Column(String(100))
    year_opened = Column(Integer)
    restaurant_type = Column(String(15))

    def __init__(self, name, num_employees, location, year_opened, restaurant_type):
        """construct abstract restaurant"""
        if type(name) != str or name == '' or name == None:
            raise ValueError('Invalid name')
        if type(num_employees) != int or num_employees == None:
            raise ValueError('Invalid num_employees')
        if type(location) != str or location == '' or location == None:
            raise ValueError('Invalid location')
        if type(year_opened) != int or year_opened == None:
            raise ValueError('Invalid year_opened')
        if type(restaurant_type) != str or restaurant_type == '' or restaurant_type == None:
            raise ValueError('Invalid type')
        self.id = None
        self.name = name
        self.num_employees = num_employees
        self.location = location
        self.year_opened = year_opened
        self.restaurant_type = restaurant_type

    def get_details(self):
        """returns brief description of the restaurant"""
        raise NotImplementedError

    def get_type(self):
        """returns type of the restaurant"""
        raise NotImplementedError

    def to_dict(self):
        """return a dictionary respresentation of the object"""
        raise NotImplementedError
