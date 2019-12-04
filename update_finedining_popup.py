import tkinter as tk
from tkinter import messagebox
import requests
import re


class UpdateFinediningPopup(tk.Frame):
    """ Popup Frame to Add a Fast Food Restaurant """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="ID:").grid(row=1, column=1)
        self._id = tk.Entry(self)
        self._id.grid(row=1, column=2)
        tk.Label(self, text="Name:").grid(row=2, column=1)
        self._name = tk.Entry(self)
        self._name.grid(row=2, column=2)
        tk.Label(self, text="Number of employees:").grid(row=3, column=1)
        self._num_employees = tk.Entry(self)
        self._num_employees.grid(row=3, column=2)
        tk.Label(self, text="Location:").grid(row=4, column=1)
        self._location = tk.Entry(self)
        self._location.grid(row=4, column=2)
        tk.Label(self, text="Year opened:").grid(row=5, column=1)
        self._year_opened = tk.Entry(self)
        self._year_opened.grid(row=5, column=2)
        tk.Label(self, text="Number of Michelin Stars:").grid(row=6, column=1)
        self._num_michelin_stars = tk.Entry(self)
        self._num_michelin_stars.grid(row=6, column=2)
        tk.Label(self, text="Chef's Name:").grid(row=7, column=1)
        self._chef_name = tk.Entry(self)
        self._chef_name.grid(row=7, column=2)

        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=8, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=8, column=2)

    def _submit_cb(self):
        """ Submit the Add Phone """

        # Validate the non-string data values
        if re.match("^\d{4}$", self._year_opened.get()) is None:
            messagebox.showerror("Error", "Year opened date must have format yyyy")
            return

        if re.match("^\d+$", self._id.get()) is None:
            messagebox.showerror("Error", "ID must be a valid integer")
            return

        if re.match("^\d+$", self._num_michelin_stars.get()) is None:
            messagebox.showerror("Error", "Number of locations must be a valid integer")
            return

        if re.match("^\d+$", self._num_employees.get()) is None:
            messagebox.showerror("Error", "Number of employees must be a valid integer")
            return

        data = {}
        data['id'] = self._id.get()
        data['name'] = self._name.get()
        data['num_employees'] = int(self._num_employees.get())
        data['location'] = self._location.get()
        data['year_opened'] = int(self._year_opened.get())
        data['num_michelin_stars'] = int(self._num_michelin_stars.get())
        data['chef_name'] = self._chef_name.get()

        headers = {"content-type": "application/json"}
        response = requests.put("http://127.0.0.1:5000/restaurantmanager/restaurants/" + self._id.get(), json=data, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Update Fine Dining Restaurant Request Failed" + response.text)
