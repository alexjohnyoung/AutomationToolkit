from os.path import isdir, isfile, join
from os import mkdir, listdir
from importlib import import_module


class EventManager:
    def __init__(self):
        self.events = {}
        self.tag = "[Event Manager]"
        self.path = "events"

    def load_events(self):
        if isdir(self.path):
            print(f"{self.tag} Loading {self.path}...")

            for filename in listdir(self.path):
                if filename.endswith(".py"):
                    event_name = filename[:-3]
                    event_module = import_module(f"events.{event_name}")

                    if hasattr(event_module, "run"):
                        self.events[event_name] = event_module.run
                        print(f"{self.tag} Loaded {event_name.upper()} event")
                    else:
                        print(f"{event_name.upper()}: No 'run' method found!")

        print(f"{self.tag} Loaded {len(self.events)} {self.path}")

    def execute_event(self, event_name, data=None):
        if event_name in self.events:

            if data is not None:
                print(f"{self.tag} Executing '{event_name}' with data: '{data}'")
                self.events[event_name](data)
            else:
                print(f"{self.tag} Executing '{event_name}")
                self.events[event_name]()

            print(f"{self.tag} Executed '{event_name}'!")
        else:
            print(f"{self.tag} Event '{event_name}' not found")

    def get_event(self, name):
        return self.events[name]

    def get_events(self):
        return self.events

