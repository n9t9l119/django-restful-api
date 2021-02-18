import os.path
from typing import IO

# from config import db_path, ru_txt_path, timezones_txt_path
# from geonames.db.convert_timezones_to_db import convert_timezones_txt_to_db
# from geonames.db.сreate_info_nameid_db import convert_ru_txt_to_db #, add_to_db
from geonames.db.GeoNamesDataBaseCreator import GeoNamesDataBaseCreator
from geonames.db.TimezonesDataBaseCreator import TimezoneDBCreator
from geonames.db.NameIdDataBaseCreator import NameIdDataBaseCreator

ru_txt_path = '../RU.txt'
timezones_txt_path = '../timezones.txt'
db_path = '/sqlite/geo_info_ru.db'
ru_txt_sample_path = '../tests/test_txt_validation/ru_sample.txt'


# def make_cells(string):
#     cells = string.split('\t')
#     cells[-1] = cells[-1].replace("\n", "")
#     return cells


# def all_names_in_str(cells):
#     names = [cells[1]]
#     if names[0] != cells[2]:
#         names.append(cells[2])
#     if cells[4] != "":
#         alternatenames = cells[3].split(',')
#         for alternatename in alternatenames:
#             if alternatename not in names and alternatename != '':
#                 names.append(alternatename)
#     return names


def create_db(ru_txt: IO, timezones_txt: IO):
    tz = TimezoneDBCreator()
    gn = GeoNamesDataBaseCreator(tz)
    ni = NameIdDataBaseCreator()
    # geonames_txt = open("geonames\RU.txt", 'r', encoding="utf8")
    gn.convert_txt_to_geonames()
    #
    gn.add_geonames_to_db()
    ni.create_nameid_from_geonames()
    print(ni.processed_nameid)
    ni.add_nameid_to_db()

    # convert_ru_txt_to_db(ru_txt)
    # convert_timezones_txt_to_db(timezones_txt)


if __name__ == '__main__':
    if not os.path.exists('..' + db_path):
        print("Database creation is started")

        ru_txt = open(ru_txt_path, 'r', encoding="utf8")
        timezones_txt = open(timezones_txt_path, 'r', encoding="utf8")

        create_db(ru_txt, timezones_txt)
        ru_txt.close()
        timezones_txt.close()

        print("Database creation was completed successfully")
    else:
        print("Database is already exist!")
