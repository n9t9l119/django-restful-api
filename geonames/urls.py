from django.urls import path, include
from geonames.views import *
from geonames.models import GeoNames

app_name = 'geonames'
urlpatterns = [
    path('all/<int:pk>/', GeoNamesDetailView.as_view()),

    path('geonameid/', GeoNamesInfoView.as_view()),
    path('page/', GeoNamesPageView.as_view()),
    path('compare/', GeoNamesCompareView.as_view()),
    path('hint/', GeoNamesHintView.as_view()),
]

from geonames.db.create_db import *

if GeoNames.objects.count() == 0:
    print("Database creation is started")

    ru_txt = open("geonames\RU.txt", 'r', encoding="utf8")
    timezones_txt = open("geonames\\timezones.txt", 'r', encoding="utf8")
    # ru_txt = open(ru_txt_path, 'r', encoding="utf8")
    # timezones_txt = open(timezones_txt_path, 'r', encoding="utf8")

    create_db(ru_txt, timezones_txt)
    ru_txt.close()
    timezones_txt.close()

    print("Database creation was completed successfully")
else:
    print("Database is already exist!")

# ru_txt = open("geonames\RU.txt", 'r', encoding="utf8")
# timezones_txt = open("geonames\\timezones.txt", 'r', encoding="utf8")
# print("Hei")
# create_db(ru_txt, timezones_txt)
