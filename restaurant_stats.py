class RestaurantStats:
    """stats on restaurants"""

    def __init__(self, total_num_restaurants, num_fine_dining, num_fast_food, avg_year_opened):
        """ Initialize the data values """

        if total_num_restaurants is None or type(total_num_restaurants) != int:
            raise ValueError("Invalid pending total num of restaurants")
        self._total_num_restaurants = total_num_restaurants

        if num_fine_dining is None or type(num_fine_dining) != int:
            raise ValueError("Invalid completed num of fine dining")
        self._num_fine_dining = num_fine_dining

        if num_fast_food is None or type(num_fast_food) != int:
            raise ValueError("Invalid completed fast good")
        self._num_fast_food = num_fast_food

        if avg_year_opened is None or type(avg_year_opened) != float:
            raise ValueError("Invalid completed repairs value")
        self._avg_year_opened = avg_year_opened

    def get_total_num_restaurants(self):
        """returns total number of restaurants"""
        return self._total_num_restaurants

    def get_num_fine_dining(self):
        """returns total number of fine dining"""
        return self._num_fine_dining

    def get_num_fast_food(self):
        """returns total number of fast food"""
        return self._num_fast_food

    def get_avg_year_opened(self):
        """returns average year that restaurant was opened"""
        return self._avg_year_opened
