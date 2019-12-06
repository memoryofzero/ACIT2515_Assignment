import tkinter as tk
from tkinter import messagebox
import requests
import re


class DetailPopup(tk.Frame):
    """ Restaurant Detail Popup """

    def __init__(self, parent, close_callback, id):
        """ Constructor """
        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        headers = {"content-type": "application/json"}
        response = requests.get("http://127.0.0.1:5000/restaurantmanager/restaurants/" + id)
        if response.status_code != 200:
            return
        desc = response.json()

        self._name = tk.Label(self, text="Name: " + desc['name']).grid(row=1, column=1)
        self._num_employees = tk.Label(self, text="Number of employees: " + str(desc['num_employees'])).grid(row=2, column=1)
        self._location = tk.Label(self, text="Location: " + desc['location']).grid(row=3, column=1)
        self._yr_opened = tk.Label(self, text="Year opened: " + str(desc['name'])).grid(row=4, column=1)
        if desc['type'] == 'fast food':
            self._num_locations = tk.Label(self, text="Number of locations: " + str(desc['num_locations'])).grid(row=5, column=1)
            if desc['has_drivethrough']:
                self._has_drivethrough = tk.Label(self, text="Has drivethrough").grid(row=6, column=1)
            else:
                self._has_drivethrough = tk.Label(self, text="Doesn't have drivethrough").grid(row=6, column=1)
        else:
            self._num_m_stars = tk.Label(self, text="Number of Michelin Stars: " + str(desc['num_michelin_stars'])).grid(row=5, column=1)
            self._chef_name = tk.Label(self, text="Chef's Name: " + desc['chef_name']).grid(row=6, column=1)

        tk.Button(self, text="Close", command=self._close_cb).grid(row=7, column=1)

