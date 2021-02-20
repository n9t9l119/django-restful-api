from django.urls import path

from geonames.db.create_db import create_db
from geonames.views import *


app_name = 'geonames'

urlpatterns = [
    path('geonameid/', GeoNamesInfoView.as_view()),
    path('page/', GeoNamesPageView.as_view()),
    path('compare/', GeoNamesCompareView.as_view()),
    path('hint/', GeoNamesHintView.as_view()),
]




# ru_txt = open("geonames\RU.txt", 'r', encoding="utf8")
# timezones_txt = open("geonames\\timezones.txt", 'r', encoding="utf8")
# print("Hei")
# create_db(ru_txt, timezones_txt)
