import tkinter as tk
from add_fastfood_popup import AddFastFoodPopup
from add_finedining_popup import AddFineDiningPopup
from update_fastfood_popup import UpdateFastfoodPopup
from update_finedining_popup import  UpdateFinediningPopup
from remove_restaurant_popup import RemoveRestaurant
import requests



class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Restaurants").grid(row=1, column=2)
        self._restaurants_listbox = tk.Listbox(self, width=100)
        self._restaurants_listbox.grid(row=2, column=1, columnspan=5)

        tk.Label(self, text="Restaurant Stats").grid(row=4, column=2)
        self._restaurants_stats = tk.Listbox(self, width=100)
        self._restaurants_stats.grid(row=5, column=1, columnspan=5)

        tk.Button(self, text="Add Fast-Food", command=self._add_fastfood).grid(row=6, column=1)
        tk.Button(self, text="Add Fine-Dining", command=self._add_finedining).grid(row=6, column=2)
        tk.Button(self, text="Update Fast-Food", command=self._update_fastfood).grid(row=7, column=1)
        tk.Button(self, text="Update Fine-Dining", command=self._update_finedining).grid(row=7, column=2)
        tk.Button(self, text="Remove Restaurant", command=self._remove_restaurant).grid(row=7, column=3)

        self._update_restaurant_list()

    def _add_fastfood(self):
        self._popup_win = tk.Toplevel()
        self._popup = AddFastFoodPopup(self._popup_win, self._close_fastfood_cb)

    def _close_fastfood_cb(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats_list()

    def _add_finedining(self):
        self._popup_win = tk.Toplevel()
        self._popup = AddFineDiningPopup(self._popup_win, self._close_finedining_cb)

    def _close_finedining_cb(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats_list()

    def _update_finedining(self):
        self._popup_win = tk.Toplevel()
        self._popup = UpdateFinediningPopup(self._popup_win, self._close_update_finedining_cb)

    def _close_update_finedining_cb(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats_list()

    def _update_fastfood(self):
        self._popup_win = tk.Toplevel()
        self._popup = UpdateFastfoodPopup(self._popup_win, self._close_update_fastfood_cb)

    def _close_update_fastfood_cb(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats_list()

    def _remove_restaurant(self):
        self._popup_win = tk.Toplevel()
        self._popup = RemoveRestaurant(self._popup_win, self._close_remove_restaurant_cb)

    def _close_remove_restaurant_cb(self):
        self._popup_win.destroy()
        self._update_restaurant_list()
        self._update_restaurant_stats_list()

    def _update_restaurant_list(self):
        """ Update the List of Restaurants Descriptions """
        self._restaurants_listbox.delete(0, tk.END)
        restaurants = ['fine dining', 'fast food']

        for restaurant in restaurants:
            response = requests.get("http://127.0.0.1:5000/restaurantmanager/restaurants/all/" + restaurant)
            if response.status_code != 200:
                return
            descs = response.json()
            for desc in descs:
                self._restaurants_listbox.insert(tk.END, desc)

    def _update_restaurant_stats_list(self):
        """ Update the List of Device Descriptions """
        self._restaurants_stats.delete(0, tk.END)

        response = requests.get("http://127.0.0.1:5000/restaurantmanager/restaurants/stats")
        if response.status_code != 200:
            return
        descs = response.json()
        for desc in descs:
            self._update_restaurant_stats_list().insert(tk.END, desc)



if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
