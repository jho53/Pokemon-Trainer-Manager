import tkinter as tk
from tkinter import messagebox
import requests
import re


class RemoveTrainerPopup(tk.Frame):
    """ Remove Trainer Popup Window """

    def __init__(self, parent, close_callback):
        """ Constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Trainer Id:").grid(row=1, column=1)
        self._trainer_id = tk.Entry(self)
        self._trainer_id.grid(row=1, column=2)
        tk.Button(self, text="Confirm", command=self._submit_cb).grid(
            row=7, column=1)
        tk.Button(self, text="Close", command=self._close_cb).grid(
            row=7, column=2)

    def _submit_cb(self):
        """ submit remove """

        # validate serial number and repair cost
        if re.match("^\d+$", self._trainer_id.get()) is None:
            messagebox.showerror(
                "Error", "Trainer Id must be a valid integer")
            return

        # create dictionary for JSON
        data = {}
        data['trainer_id'] = self._trainer_id.get()

        # implementation here
        headers = {"content-type": "application/json"}
        response = requests.delete("http://127.0.0.1:5000/trainermanager/trainers/" + str(data['trainer_id']),
                                   json=data, headers=headers)

        if response.status_code == 200:
            messagebox.showinfo(
                "Success", "Trainer has been sucessfully removed")
            self._close_cb()
        else:
            messagebox.showwarning("Error", "Remove Trainer Request Failed")
