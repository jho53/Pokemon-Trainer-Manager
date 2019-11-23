import tkinter as tk
import requests
from PIL import Image


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="Trainer Manager", font=("Arial", 26)).grid(
            row=1, column=5)
        self._trainers_listbox = tk.Listbox(self, width=60)
        self._trainers_listbox.grid(
            row=2, column=1, columnspan=6)

        self._trainers_stats_listbox = tk.Listbox(self, width=25)
        self._trainers_stats_listbox.grid(
            row=2, column=7, columnspan=3)

        tk.Button(self, text="All Trainers").grid(row=3, column=4)
        tk.Button(self, text="Regular Trainers").grid(row=3, column=5)
        tk.Button(self, text="Gym Leaders").grid(row=3, column=6)
        tk.Button(self, text="Trainer Details").grid(row=3, column=8)

        tk.Button(self, text="Add Trainer").grid(row=4, column=4)
        tk.Button(self, text="Update Trainer").grid(row=4, column=5)
        tk.Button(self, text="Delete Trainer").grid(row=4, column=6)
        tk.Button(self, text="Quit").grid(row=4, column=8)

        # load the image file
        image = Image.open("surprised_pikachu.gif")
        image = image.resize((760, 420), Image.ANTIALIAS)
        pika = tk.PhotoImage(file=r"surprised_pikachu.gif")
        # prevent garbage colleciton
        root.pika = pika
        # create the canvas
        self._canvas = tk.Canvas(self, width=760, height=420,
                                 background="white", bd=1, relief=tk.RAISED)
        # put gif image on canvas
        self._canvas.create_image(350, 100, image=pika)
        self._canvas.grid(row=5, column=1, columnspan=10)


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
