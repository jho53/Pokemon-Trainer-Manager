import tkinter as tk
from tkinter import messagebox
import requests
import re


class ShowDetailsPopup(tk.Frame):
    """ Show Details Popup """

    def __init__(self, parent, close_callback, data):
        """ constructor """

        tk.Frame.__init__(self, parent)
        self._close_cb = close_callback
        self.grid(rowspan=2, columnspan=2)

        trainer_type = data["type"]

        tk.Label(self, text=trainer_type, font=(
            "Arial", 18)).grid(row=1, column=1)

        if trainer_type == "Regular Trainer":
            trainer_id = data["trainer_id"]
            tk.Label(self, text="Trainer Id: {}".format(
                trainer_id)).grid(row=2, column=1)
            name = data["name"]
            tk.Label(self, text="Trainer Name: {}".format(
                name)).grid(row=3, column=1)
            pokemon_team = str(data["pokemon_team"])
            pokemon_team = re.sub('[{}\']', '', pokemon_team)
            tk.Label(self, text="Pokemon Team: {}".format(
                pokemon_team)).grid(row=4, column=1)
            trainer_class = data["trainer_class"]
            tk.Label(self, text="Trainer Class: {}".format(
                trainer_class)).grid(row=5, column=1)
            pokecoins = str(data["pokecoins"])
            tk.Label(self, text="Pokecoins: {}".format(
                pokecoins)).grid(row=6, column=1)
            location = data["location"]
            tk.Label(self, text="Location: {}".format(
                location)).grid(row=7, column=1)
            movement_type = data["movement_type"]
            tk.Label(self, text="Movement Type: {}".format(
                movement_type)).grid(row=8, column=1)
            if data["phone_num"] == 0:
                phone_num = "False"
            else:
                phone_num = "True"
            tk.Label(self, text="Phone Number: {}".format(
                phone_num)).grid(row=9, column=1)
            if data["have_partner"] == 0:
                have_partner = "False"
            else:
                have_partner = "True"
            tk.Label(self, text="Have Partner: {}".format(
                have_partner)).grid(row=10, column=1)

        if data["type"] == "Gym Leader":
            trainer_id = data["trainer_id"]
            tk.Label(self, text="Trainer Id: {}".format(
                trainer_id)).grid(row=2, column=1)
            name = data["name"]
            tk.Label(self, text="Gym Leader Name: {}".format(
                name)).grid(row=3, column=1)
            pokemon_team = str(data["pokemon_team"])
            pokemon_team = re.sub('[{}\']', '', pokemon_team)
            tk.Label(self, text="Pokemon Team: {}".format(
                pokemon_team)).grid(row=4, column=1)
            trainer_class = data["trainer_class"]
            tk.Label(self, text="Trainer Class: {}".format(
                trainer_class)).grid(row=5, column=1)
            pokecoins = str(data["pokecoins"])
            tk.Label(self, text="Pokecoins: {}".format(
                pokecoins)).grid(row=6, column=1)
            location = data["location"]
            tk.Label(self, text="Location: {}".format(
                location)).grid(row=7, column=1)
            badge = data["badge"]
            tk.Label(self, text="Badge: {}".format(
                badge)).grid(row=8, column=1)
            element = data["element"]
            tk.Label(self, text="Element: {}".format(
                element)).grid(row=9, column=1)
            prize = data["prize"]
            tk.Label(self, text="Prize: {}".format(
                prize)).grid(row=10, column=1)

        tk.Button(self, text="Close", command=self._close_cb).grid(
            row=12, column=1)

        print("Showing detailed page for {} | Trainer ID#: {}".format(
            data["name"], data["trainer_id"]))
