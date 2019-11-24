import tkinter as tk
import requests
import re
import ast
from PIL import Image

from add_regular_trainer_popup import AddRegularTrainerPopup
from add_gym_leader_popup import AddGymLeaderPopup
from remove_trainer_popup import RemoveTrainerPopup
from update_gym_leader_popup import UpdateGymLeaderPopup
from update_regular_trainer_popup import UpdateRegularTrainerPopup


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._view_setting = "all"

        tk.Label(self, text="Trainer Manager", font=("Arial", 26)).grid(
            row=1, column=5)
        self._trainers_listbox = tk.Listbox(self, width=60)
        self._trainers_listbox.grid(
            row=2, column=1, columnspan=6)

        self._trainers_stats_listbox = tk.Listbox(self, width=25)
        self._trainers_stats_listbox.grid(
            row=2, column=7, columnspan=3)

        tk.Button(self, text="Show Regular Trainers",
                  command=self._update_trainer_list_regular_trainers).grid(row=3, column=4)
        tk.Button(self, text="Show Gym Leaders",
                  command=self._update_trainer_list_gym_leaders).grid(row=3, column=5)
        tk.Button(self, text="Show All Trainers",
                  command=self._update_trainer_list_all).grid(row=3, column=6)

        tk.Button(self, text="Add Regular Trainer",
                  command=self._add_regular_trainer).grid(row=4, column=4)
        tk.Button(self, text="Add Gym Leader",
                  command=self._add_gym_leader).grid(row=4, column=5)
        tk.Button(self, text="Remove Trainer",
                  command=self._remove_trainer).grid(row=4, column=8)

        tk.Button(self, text="Update Regular Trainer",
                  command=self._update_regular_trainer).grid(row=5, column=4)
        tk.Button(self, text="Update Gym Leader",
                  command=self._update_gym_leader).grid(row=5, column=5)
        tk.Button(self, text="Quit", command=self._quit_callback).grid(
            row=5, column=8)

        # load the image file
        image = Image.open("./images/surprised_pikachu.gif")
        image = image.resize((760, 420), Image.ANTIALIAS)
        pika = tk.PhotoImage(file="./images/surprised_pikachu.gif")
        # prevent garbage colleciton
        root.pika = pika
        # create the canvas
        self._canvas = tk.Canvas(self, width=760, height=420,
                                 background="white", bd=1, relief=tk.RAISED)
        # put gif image on canvas
        self._canvas.create_image(350, 100, image=pika)
        self._canvas.grid(row=6, column=1, columnspan=10)

        # load trainers and statistics
        self._show_statistics()
        if self._view_setting == "all":
            self._update_trainer_list_all()
        if self._view_setting == "regular_trainers":
            self._update_trainer_list_regular_trainers()
        if self._view_setting == "gym_leaders":
            self._update_trainer_list_gym_leaders()

    def _quit_callback(self):
        """ Quit Immediately """
        self.quit()

    def _add_regular_trainer(self):
        """ Add Trainer Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddRegularTrainerPopup(
            self._popup_win, self._close_add_cb)

    def _add_gym_leader(self):
        """ Add Gym Leader Popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddGymLeaderPopup(
            self._popup_win, self._close_add_cb)

    def _close_add_cb(self):
        """ close Add Trainer Popups """
        self._popup_win.destroy()
        self._show_statistics()
        if self._view_setting == "all":
            self._update_trainer_list_all()
        if self._view_setting == "regular_trainers":
            self._update_trainer_list_regular_trainers()
        if self._view_setting == "gym_leaders":
            self._update_trainer_list_gym_leaders()

    def _update_regular_trainer(self):
        """ Add Gym Leader Popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdateRegularTrainerPopup(
            self._popup_win, self._close_update_cb)

    def _update_gym_leader(self):
        """ Add Gym Leader Popup """
        self._popup_win = tk.Toplevel()
        self._popup = UpdateGymLeaderPopup(
            self._popup_win, self._close_update_cb)

    def _close_update_cb(self):
        """ close Update Trainer Popups """
        self._popup_win.destroy()
        self._show_statistics()
        if self._view_setting == "all":
            self._update_trainer_list_all()
        if self._view_setting == "regular_trainers":
            self._update_trainer_list_regular_trainers()
        if self._view_setting == "gym_leaders":
            self._update_trainer_list_gym_leaders()

    def _remove_trainer(self):
        """ Remove Trainer Popup """
        self._popup_win = tk.Toplevel()
        self._popup = RemoveTrainerPopup(
            self._popup_win, self._close_remove_cb)

    def _close_remove_cb(self):
        """ close Remove Trainer Popup """
        self._popup_win.destroy()
        self._show_statistics()
        if self._view_setting == "all":
            self._update_trainer_list_all()
        if self._view_setting == "regular_trainers":
            self._update_trainer_list_regular_trainers()
        if self._view_setting == "gym_leaders":
            self._update_trainer_list_gym_leaders()

    def _update_trainer_list_all(self):
        """ Update the List of Trainers  """
        self._view_setting = "all"

        response = requests.get(
            "http://127.0.0.1:5000/trainermanager/trainers/all/type/regular_trainer")

        if response.status_code != 200:
            tk.messagebox.showwarning(
                "Warning", "Could not retrieve the trainers.")
            return

        self._trainers_listbox.delete(0, tk.END)

        trainer_descs = response.json()
        for trainer in trainer_descs:
            self._trainers_listbox.insert(tk.END, trainer)

        response = requests.get(
            "http://127.0.0.1:5000/trainermanager/trainers/all/type/gym_leader")

        if response.status_code != 200:
            tk.messagebox.showwarning(
                "Warning", "Could not retrieve the trainers.")
            return

        gym_leader_descs = response.json()
        for trainer in gym_leader_descs:
            self._trainers_listbox.insert(tk.END, trainer)

    def _update_trainer_list_regular_trainers(self):
        """ Update the List of Trainers  """

        self._view_setting = "regular_trainers"

        response = requests.get(
            "http://127.0.0.1:5000/trainermanager/trainers/all/type/regular_trainer")

        if response.status_code != 200:
            tk.messagebox.showwarning(
                "Warning", "Could not retrieve the trainers.")
            return

        self._trainers_listbox.delete(0, tk.END)

        trainer_descs = response.json()
        for trainer in trainer_descs:
            self._trainers_listbox.insert(tk.END, trainer)

    def _update_trainer_list_gym_leaders(self):
        """ Update the List of Trainers  """

        self._view_setting = "gym_leaders"

        response = requests.get(
            "http://127.0.0.1:5000/trainermanager/trainers/all/type/gym_leader")

        if response.status_code != 200:
            tk.messagebox.showwarning(
                "Warning", "Could not retrieve the trainers.")
            return

        self._trainers_listbox.delete(0, tk.END)

        gym_leader_descs = response.json()
        for trainer in gym_leader_descs:
            self._trainers_listbox.insert(tk.END, trainer)

    def _show_statistics(self):
        """ Get Trainer Stats """
        response = requests.get(
            "http://127.0.0.1:5000/trainermanager/trainers/stats")

        if response.status_code != 200:
            tk.messagebox.showwarning(
                "Warning", "Could not retrieve the trainer stats.")
            return

        self._trainers_stats_listbox.delete(0, tk.END)

        trainer_stats = response.json()

        # list stats
        for i in range(len(trainer_stats) - 1):
            self._trainers_stats_listbox.insert(tk.END, trainer_stats[i])
        self._trainers_stats_listbox.insert(tk.END, "Trainers per location:")

        # extract dictionary from string
        location_dict = ast.literal_eval(
            re.search('({.+})', trainer_stats[4]).group(0))

        # list trainers by location based on extracted dictionary
        for key in location_dict:
            location_string = "    {}: {}".format(key, location_dict[key])
            self._trainers_stats_listbox.insert(tk.END, location_string)


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
