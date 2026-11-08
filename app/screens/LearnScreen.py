import json
import os
from traceback import print_tb

from kivy.loader import Loader
from kivy.properties import StringProperty
from kivy.uix.screenmanager import SlideTransition
from kivymd.uix.screen import Screen
import random

from app import switch_to
from app.screens import BaseScreen


class LearnScreen(BaseScreen):
    name = StringProperty("learn_screen")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
        self.current_pos = 0
        self.current_set = None
        self.on_data_loaded = None
        self._total_load = 0
        self._total_loaded_count = 0
        self.load_data()

    def on_switch_bind(self):
        self.render_card()

    def back_to_main_screen(self):

        switch_to(self.manager, "main_screen", transition=SlideTransition(direction="right"))

    def _image_loaded(self, proxyImage, ind):
        self.data[ind]["res_preprocessed"].append(proxyImage.texture)
        self._total_loaded_count += 1

        if self._total_loaded_count == self._total_load and self.on_data_loaded is not None:
            self.on_data_loaded()

    def load_data(self):
        with open("./app/resources/json/res_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        for key, d in data.items():
            out = {
                "name": d["name"],
                "group": d["group"],
                "res": [f"app/resources/images/{key}/{i}" for i in os.listdir(f"app/resources/images/{key}")],
                "res_preprocessed": [],
            }

            for i in os.listdir(f"app/resources/images/{key}"):
                proxy = Loader.image(f"app/resources/images/{key}/{i}")
                proxy.bind(on_load=lambda a, i=len(self.data): self._image_loaded(a, i))
            self._total_load += len(out["res"])
            self.data.append(out)

    def shake_set(self):
        self.current_set = random.sample(self.data, len(self.data))
        self.current_pos = 0

    def render_card(self):

        self.ids.show_answer_button.disabled = False
        self.ids.next_card.disabled = True
        self.ids.card_text.text = ""
        if self.current_set is None or self.current_pos >= len(self.data):
            self.current_set = random.sample(self.data, len(self.data))
            self.current_pos = 0
        self.ids.card.source = ""
        if self.current_set[self.current_pos]["res_preprocessed"]:
            self.ids.card.texture = random.choice(self.current_set[self.current_pos]["res_preprocessed"])
        else:
            self.ids.card.source = random.choice(self.current_set[self.current_pos]["res"])

    def next_card(self):
        self.current_pos += 1
        self.render_card()

    def show_answer(self):

        self.ids.card_text.text = self.current_set[self.current_pos].get("name")
        self.ids.show_answer_button.disabled = True
        self.ids.next_card.disabled = False
