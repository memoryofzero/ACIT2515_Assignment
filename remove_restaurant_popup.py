import tkinter as tk
from tkinter import messagebox
import requests


class RemoveRestaurant(tk.Frame):
    """ Popup Frame to Complete a Repair """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="ID:").grid(row=1, column=1)
        self._id = tk.Entry(self)
        self._id.grid(row=1, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(row=2, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(row=2, column=2)

    def _submit_cb(self):
        """ Submit Complete Repair """
        id = self._id.get()

        headers = {"content-type": "application/json"}
        response = requests.delete("http://127.0.0.1:5000/restaurantmanager/restaurants/" + id, headers=headers)

        if response.status_code == 200:
            self._close_cb()
        else:
            messagebox.showerror("Error", "Remove restaurant fail " + response.text)


