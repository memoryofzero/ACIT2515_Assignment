import tkinter as tk
from add_fastfood_popup import AddFastFoodPopup
from add_finedining_popup import AddFineDiningPopup
from update_fastfood_popup import UpdateFastfoodPopup
from update_finedining_popup import UpdateFinediningPopup
from remove_restaurant_popup import RemoveRestaurant
from details_popup import DetailPopup
from tkinter import messagebox
import requests



class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._total_num_restaurants = tk.StringVar(self)
        self._avg_year_opened = tk.StringVar(self)
        self._num_fast_food = tk.StringVar(self)
        self._num_fine_dining = tk.StringVar(self)
        self._total_num_restaurants.set('0')
        self._avg_year_opened.set('0')
        self._num_fast_food.set('0')
        self._num_fine_dining.set('0')

        tk.Label(self, text="Restaurants").grid(row=2, column=1, columnspan=4)
        self._restaurants_listbox = tk.Listbox(self, width=50)
        self._restaurants_listbox.grid(row=3, column=1, columnspan=4, rowspan=3)

        self._restaurant_type = tk.StringVar()
        self._restaurant_type.set('fast food')
        tk.Radiobutton(self, text="Fast Food", variable=self._restaurant_type, value='fast food', command=self._update_restaurant_list).grid(row=1, column=1, columnspan=2)
        tk.Radiobutton(self, text="Fine Dining", variable=self._restaurant_type, value='fine dining', command=self._update_restaurant_list).grid(row=1, column=3, columnspan=2)

        tk.Label(self, text="Total Restaurants: ").grid(row=2, column=5)
        tk.Label(self, textvar=self._total_num_restaurants).grid(row=2, column=6)
        tk.Label(self, text="Avg. Year Opened: ").grid(row=3, column=5)
        tk.Label(self, textvar=self._avg_year_opened).grid(row=3, column=6)
        tk.Label(self, text="Fast Food Restaurants: ").grid(row=4, column=5)
        tk.Label(self, textvar=self._num_fast_food).grid(row=4, column=6)
        tk.Label(self, text="Fine Dining Restaurants: ").grid(row=5, column=5)
        tk.Label(self, textvar=self._num_fine_dining).grid(row=5, column=6)
        tk.Button(self, text="Add", command=self._add).grid(row=6, column=1)
        tk.Button(self, text="Update", command=self._update).grid(row=6, column=2)
        tk.Button(self, text="Details", command=self._details).grid(row=6, column=3)

        tk.Button(self, text="Remove Restaurant", command=self._remove_restaurant).grid(row=6, column=4)

        self._update_restaurant_list()
        self._update_restaurant_stats()


    def _details(self):
        try:
            restaurant = self._restaurants_listbox.get(self._restaurants_listbox.curselection())
            self._popup_win = tk.Toplevel()
            id = list(restaurant.split(" "))[0]
            self._popup = DetailPopup(self._popup_win, self._close, id)
        except:
            messagebox.showerror('Error', "Select a restaurant")

    def _add(self):
        self._popup_win = tk.Toplevel()
        if self._restaurant_type.get() == 'fast food':
            self._popup = AddFastFoodPopup(self._popup_win, self._close)
        else:
            self._popup = AddFineDiningPopup(self._popup_win, self._close)

    def _close(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats()

    def _update(self):
        try:
            restaurant = self._restaurants_listbox.get(self._restaurants_listbox.curselection())
            self._popup_win = tk.Toplevel()
            id = list(restaurant.split(" "))[0]
            if self._restaurant_type.get() == 'fast food':
                self._popup = UpdateFastfoodPopup(self._popup_win, self._close, id)
            else:
                self._popup = UpdateFinediningPopup(self._popup_win, self._close, id)
        except:
            messagebox.showerror('Error', "Select a restaurant")

    def _remove_restaurant(self):
        self._popup_win = tk.Toplevel()
        self._popup = RemoveRestaurant(self._popup_win, self._close_remove_restaurant_cb)

    def _close_remove_restaurant_cb(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats()

    def _update_restaurant_list(self):
        """ Update the List of Restaurants Descriptions """
        self._restaurants_listbox.delete(0, tk.END)
        restaurant_type = self._restaurant_type.get()
        response = requests.get("http://127.0.0.1:5000/restaurantmanager/restaurants/all/" + restaurant_type)
        if response.status_code != 200:
            return
        descs = response.json()
        for desc in descs:
            self._restaurants_listbox.insert(tk.END, str(desc['id']) + ' ' + desc['name'])

    def _update_restaurant_stats(self):
        """ Update the restaurant stats """
        response = requests.get("http://127.0.0.1:5000/restaurantmanager/restaurants/stats")
        if response.status_code != 200:
            return
        stats = response.json()
        self._total_num_restaurants.set(stats['total_num_restaurants'])
        self._avg_year_opened.set(stats['avg_year_opened'])
        self._num_fast_food.set(stats['num_fast_food'])
        self._num_fine_dining.set(stats['num_fine_dining'])

        self.update()


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
