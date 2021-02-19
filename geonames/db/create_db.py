from geonames.db.GeoNamesDataBaseCreator import GeoNamesDataBaseCreator
from geonames.db.TimezonesDataBaseCreator import TimezoneDBCreator
from geonames.db.NameIdDataBaseCreator import NameIdDataBaseCreator
from geonames.models import GeoNames

ru_txt_path = '../RU.txt'
timezones_txt_path = '../timezones.txt'
db_path = '/sqlite/geo_info_ru.db'
ru_txt_sample_path = '../tests/test_txt_validation/ru_sample.txt'


def create_db(ru_txt, timezones_txt):
    tz = TimezoneDBCreator()
    gn = GeoNamesDataBaseCreator(tz)
    ni = NameIdDataBaseCreator()

    gn.convert_txt_file_to_geonames_objects()
    gn.add_geonames_objects_to_db()

    ni.create_nameid_objects_from_geonames()
    ni.add_nameid_objects_to_db()

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
    print("Database is already exist!!!!!!!!!!!!!!!!!!!!")
