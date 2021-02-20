import logging

from django.db import connection

from geonames.db.DataBaseCreators.GeoNamesDataBaseCreator import GeoNamesDataBaseCreator
from geonames.db.DataBaseCreators.TimezonesDataBaseCreator import TimezoneDBCreator
from geonames.db.DataBaseCreators.NameIdDataBaseCreator import NameIdDataBaseCreator
from geonames.models import GeoNames
from geonames.db.ConfigDataBase import ConfigDataBase


def create_db(ru_txt, timezones_txt):
    tz = TimezoneDBCreator(timezones_txt)
    gn = GeoNamesDataBaseCreator(tz, ru_txt)
    ni = NameIdDataBaseCreator()

    gn.convert_txt_file_to_geonames_objects()
    gn.add_geonames_objects_to_db()

    ni.create_nameid_objects_from_geonames()
    ni.add_nameid_objects_to_db()


logging.basicConfig(level='INFO')

if "geonames_geonames" in connection.introspection.table_names() and GeoNames.objects.count() == 0:
    logging.info("Database creation is started")

    try:
        with open(ConfigDataBase.ru_txt_path, 'r', encoding="utf8") as ru_txt, \
                open(ConfigDataBase.timezones_txt_path, 'r', encoding="utf8") as timezones_txt:
            create_db(ru_txt, timezones_txt)
    except IOError as e:
        logging.critical(f"Can't open file: {e.strerror}")
    else:
        logging.info("Database creation was completed successfully")
else:
    logging.info("Database is already exist!")
