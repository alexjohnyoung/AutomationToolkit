import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

BACKGROUND_COL = "#222224"


class Menu:

    def __init__(self, size, is_main=True):
        if is_main:
            self.root = tk.Tk()
        else:
            self.root = tk.Toplevel()

        self.root.title("Automation")
        self.root.geometry(size)
        self.root["bg"] = BACKGROUND_COL

        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background=BACKGROUND_COL)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")
        self.tabs = {}
        self.fonts = {}
        self.texts = {}

    def close_window(self):
        self.root.destroy()

    def add_font(self, name, font, size):
        font = tkFont.Font(family=font, size=size)
        self.fonts[name] = font

    def get_font(self, name):
        return self.fonts[name]

    def create_textbox(self, parent, **pos):
        if parent is not None:
            textbox = tk.Text(self.get_tab(parent))
        else:
            textbox = tk.Text(self.root)

        textbox.place(**pos)
        return textbox

    def create_listbox(self, parent, items=None, **pos):
        tab = self.root

        if parent is not None:
            tab = self.get_tab(parent)

        listbox = tk.Listbox(tab)

        if items is not None:
            for item in items:
                listbox.insert(tk.END, item)

        listbox.place(**pos)
        return listbox

    def create_entry(self, parent, **pos):
        tab = self.root

        if parent is not None:
            tab = self.get_tab(parent)

        entry = tk.Entry(tab)
        entry.place(**pos)
        return entry

    def create_tab(self, name):
        new_tab = ttk.Frame(self.notebook)
        self.tabs[name] = new_tab
        self.notebook.add(new_tab, text=name)

    def create_label(self, parent, text, font, **pos):
        tab = self.root

        if parent is not None:
            tab = self.get_tab(parent)

        label = tk.Label(tab, text=text, fg="white", bg=BACKGROUND_COL, font=self.get_font(font))
        label.place(**pos)

    def create_combobox(self, parent, values, **pos):
        combo = ttk.Combobox(self.get_tab(parent), values=values, background=BACKGROUND_COL)
        combo.place(**pos)
        return combo

    def create_button(self, parent, text, command, **pos):
        tab = self.root

        if parent is not None:
            tab = self.get_tab(parent)

        button = tk.Button(tab, text=text, command=command, bg=BACKGROUND_COL, fg="white")
        button.place(**pos)

    def get_tab(self, name):
        return self.tabs[name]

    def start(self):
        self.root.mainloop()