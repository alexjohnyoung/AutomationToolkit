import tkinter as tk
from tkinter import ttk, StringVar
from menu import Menu
from util import Util
from eventmanager import EventManager
from proceduremanager import ProcedureManager
from resourcemanager import ResourceManager
from os.path import isdir, isfile, join
from os import mkdir, listdir, remove


def open_menu(event_manager, procedure_manager, resource_manager):
    menu = Menu("335x350")

    menu.create_tab("Procedures")
    menu.create_tab("Manage")
    menu.create_tab("Resources")
    menu.create_tab("Logs")

    menu.add_font("hel10", "Helvetica", 10)
    menu.add_font("hel15", "Helvetica", 15)

    textbox = menu.create_textbox("Procedures", x=3, y=35, width=325, height=284)

    menu.create_label("Procedures", "Select procedure", "hel10", x=5, y=7)

    combo = menu.create_combobox("Procedures", procedure_manager.get_procedures(), x=110, y=8, width=80)

    def load_procedure(proc):
        proc = f"{proc}.txt"
        proc = join("procedures", proc)

        if isfile(proc):
            handle = open(proc, "r")
            textbox.delete("1.0", "end")
            textbox.insert("1.0", handle.read())
            handle.close()

    def save_procedure(text):
        save_menu = Menu("150x80", False)
        save_menu.add_font("hel10", "Helvetica", 10)
        save_menu.create_label(None, "Enter name", "hel10", x=5, y=5, width=140, height=20)
        entry = save_menu.create_entry(None, x=5, y=25, width=140, height=20)

        def save_procedure_to_file(name):
            if not isdir("procedures"):
                mkdir("procedures")

            procedure_manager.save_procedure(name, text)
            save_menu.close_window()

            current_values = list(combo["values"])
            current_values.append(name)
            combo["values"] = current_values
            combo.set("")

        save_menu.create_button(None, "Save", lambda: save_procedure_to_file(entry.get()), x=25, y=50, width=100,
                                height=20)
        save_menu.start()

    def delete_procedure(name):
        if name == "":
            return

        path = join("procedures", f"{name}.txt")

        if isfile(path):
            remove(path)
            textbox.delete("1.0", "end")

            current_values = list(combo["values"])
            current_values.remove(name)
            combo["values"] = current_values
            combo.set("")

    def run_procedure(data):
        if data == "":
            return

        data = data.split("\n")

        for line in data:
            line = line.split(" ")
            event = line[0]
            data = line[1]

            event_manager.execute_event(event, data)

    menu.create_button("Procedures", "Load", lambda: load_procedure(combo.get()), x=196, y=7)
    menu.create_button("Procedures", "Save", lambda: save_procedure(textbox.get("1.0", "end-1c")), x=238, y=7)
    menu.create_button("Procedures", "Delete", lambda: delete_procedure(combo.get()), x=280, y=7)
    menu.create_button("Procedures", "Run", lambda: run_procedure(textbox.get("1.0", "end-1c")), x=292, y=290)

    # Manage Tab
    menu.create_listbox("Manage", procedure_manager.get_procedures(), x=0, y=0, width=330, height=150)
    menu.create_label("Manage", "Set Procedure Options", "hel15", x=60, y=150)

    # Start the Menu
    menu.start()


def main():
    util = Util()
    util.create_folders()

    event_manager = EventManager()
    event_manager.load_events()

    procedure_manager = ProcedureManager()
    procedure_manager.load_procedures()

    resource_manager = ResourceManager()
    resource_manager.load_resources()

    open_menu(event_manager, procedure_manager, resource_manager)



if __name__ == "__main__":
    main()

