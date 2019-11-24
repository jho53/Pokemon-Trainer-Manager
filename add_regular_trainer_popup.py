import tkinter as tk
from tkinter import messagebox
import requests
import re


class AddRegularTrainerPopup(tk.Frame):
    """ Popup Frame to Add Trainer """

    def __init__(self, parent, close_callback):
        """ constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        tk.Label(self, text="Trainer Name").grid(row=1, column=1)
        self._name = tk.Entry(self)
        self._name.grid(row=1, column=2)
        tk.Label(
            self, text="Pokemon #1 - Required - Format: Pokemon, Level").grid(row=2, column=1)
        self._pokemon1 = tk.Entry(self)
        self._pokemon1.grid(row=2, column=2)
        self._pokemon1_level = tk.Entry(self)
        self._pokemon1_level.grid(row=2, column=3)
        tk.Label(
            self, text="Pokemon #2 - Optional - Format: Pokemon, Level").grid(row=3, column=1)
        self._pokemon2 = tk.Entry(self)
        self._pokemon2.grid(row=3, column=2)
        self._pokemon2_level = tk.Entry(self)
        self._pokemon2_level.grid(row=3, column=3)
        tk.Label(
            self, text="Pokemon #3 - Optional - Format: Pokemon, Level").grid(row=4, column=1)
        self._pokemon3 = tk.Entry(self)
        self._pokemon3.grid(row=4, column=2)
        self._pokemon3_level = tk.Entry(self)
        self._pokemon3_level.grid(row=4, column=3)
        tk.Label(
            self, text="Pokemon #4 - Optional - Format: Pokemon, Level").grid(row=5, column=1)
        self._pokemon4 = tk.Entry(self)
        self._pokemon4.grid(row=5, column=2)
        self._pokemon4_level = tk.Entry(self)
        self._pokemon4_level.grid(row=5, column=3)
        tk.Label(
            self, text="Pokemon #5 - Optional - Format: Pokemon, Level").grid(row=6, column=1)
        self._pokemon5 = tk.Entry(self)
        self._pokemon5.grid(row=6, column=2)
        self._pokemon5_level = tk.Entry(self)
        self._pokemon5_level.grid(row=6, column=3)
        tk.Label(
            self, text="Pokemon #6 - Optional - Format: Pokemon, Level").grid(row=7, column=1)
        self._pokemon6 = tk.Entry(self)
        self._pokemon6.grid(row=7, column=2)
        self._pokemon6_level = tk.Entry(self)
        self._pokemon6_level.grid(row=7, column=3)
        tk.Label(self, text="Trainer Class").grid(row=8, column=1)
        self._trainer_class = tk.Entry(self)
        self._trainer_class.grid(row=8, column=2)
        tk.Label(self, text="Pokecoins").grid(row=9, column=1)
        self._pokecoins = tk.Entry(self)
        self._pokecoins.grid(row=9, column=2)
        tk.Label(self, text="Location").grid(row=10, column=1)
        self._location = tk.Entry(self)
        self._location.grid(row=10, column=2)
        tk.Label(
            self, text="Movement Type - Required - Choose 1").grid(row=11, column=1)
        self._movement_type = tk.StringVar()
        self._movement_type.set("Walking")
        tk.OptionMenu(self, self._movement_type, "Walking",
                      "Biking", "Swimming").grid(row=11, column=2)
        tk.Label(self, text="Phone Number - Optional").grid(row=12, column=1)
        self._phone_number = tk.BooleanVar()
        tk.Checkbutton(self, text="True", variable=self._phone_number,
                       onvalue="true", offvalue="false").grid(row=12, column=2)
        tk.Label(self, text="Have Partner - Optional").grid(row=13, column=1)
        self._have_partner = tk.BooleanVar()
        tk.Checkbutton(self, text="True", variable=self._have_partner,
                       onvalue="true", offvalue="false").grid(row=13, column=2)
        tk.Button(self, text="Submit", command=self._submit_cb).grid(
            row=15, column=2, pady=(10, 0))
        tk.Button(self, text="Close", command=self._close_cb).grid(
            row=15, column=3, pady=(10, 0))

    def _submit_cb(self):
        """ Submit the Add Phone """

        if re.match("^\d+$", self._pokemon1_level.get()) is None:
            messagebox.showerror(
                "Error", "Pokemon level must be a valid integer")
            return

        if re.match("^\d+$", self._pokecoins.get()) is None:
            messagebox.showerror(
                "Error", "Pokecoins amount must be a valid integer")
            return

        # declaring a temp variable to store pokemon team
        pokemon_team = {}

        # putting the trainer pokemon into a dict
        if self._pokemon1.get() != "":
            try:
                pokemon = self._pokemon1.get()
                level = int(self._pokemon1_level.get())
                pokemon_team[pokemon] = level
            except:
                messagebox.showerror(
                    "Error", "Pokemon #1 - level must be an integer")
                return
        else:
            messagebox.showerror(
                "Error", "Trainer must have at least one pokemon")
            return

        if self._pokemon2.get() != "":
            try:
                pokemon = self._pokemon2.get()
                level = int(self._pokemon2_level.get())
                pokemon_team[pokemon] = level
            except:
                messagebox.showerror(
                    "Error", "Pokemon #2 - level must be an integer")
                return

        if self._pokemon3.get() != "":
            try:
                pokemon = self._pokemon3.get()
                level = int(self._pokemon3_level.get())
                pokemon_team[pokemon] = level
            except:
                messagebox.showerror(
                    "Error", "Pokemon #3 - level must be an integer")
                return

        if self._pokemon4.get() != "":
            try:
                pokemon = self._pokemon4.get()
                level = int(self._pokemon4_level.get())
                pokemon_team[pokemon] = level
            except:
                messagebox.showerror(
                    "Error", "Pokemon #4 - level must be an integer")
                return

        if self._pokemon5.get() != "":
            try:
                pokemon = self._pokemon5.get()
                level = int(self._pokemon5_level.get())
                pokemon_team[pokemon] = level
            except:
                messagebox.showerror(
                    "Error", "Pokemon #5 - level must be an integer")
                return

        if self._pokemon6.get() != "":
            try:
                pokemon = self._pokemon6.get()
                level = int(self._pokemon6_level.get())
                pokemon_team[pokemon] = level
            except:
                messagebox.showerror(
                    "Error", "Pokemon #6 - level must be an integer")
                return

        if pokemon_team == {}:
            messagebox.showerror(
                "Error", "Trainer must have at least one pokemon")
            return

        # Create the dictionary for the JSON request body
        data = {}
        data['name'] = self._name.get()
        data['pokemon_team'] = pokemon_team
        data['trainer_class'] = self._trainer_class.get()
        data['pokecoins'] = int(self._pokecoins.get())
        data['location'] = self._location.get()
        data['movement_type'] = self._movement_type.get()
        data['phone_num'] = self._phone_number.get()
        data['have_partner'] = self._have_partner.get()
        data['type'] = "Regular Trainer"

        headers = {"content-type": "application/json"}
        response = requests.post("http://127.0.0.1:5000/trainermanager/trainers",
                                 json=data, headers=headers)

        print(data)

        if response.status_code == 200:
            messagebox.showinfo("Success", "Trainer has been added")
            self._close_cb()
        else:
            messagebox.showwarning(
                "Error", "Trainer could not be added because of invalid data")
