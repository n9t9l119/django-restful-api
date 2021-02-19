from django.apps import AppConfig
from geonames.db.create_db import *

from geonames.models import GeoNames


class GeonamesConfig(AppConfig):
    name = 'geonames'

    def ready(self):


        pass
