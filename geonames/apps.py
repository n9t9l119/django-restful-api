from django.apps import AppConfig
from geonames.db.create_db import *


class GeonamesConfig(AppConfig):
    name = 'geonames'

    def ready(self):
        print("KKKKKK")
        # ru_txt = open("geonames\RU.txt", 'r', encoding="utf8")
        # timezones_txt = open("geonames\\timezones.txt", 'r', encoding="utf8")
        #
        # create_db(ru_txt, timezones_txt)
