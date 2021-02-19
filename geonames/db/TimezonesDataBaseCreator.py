from geonames.models import Timezones
from typing import List, Union, IO


class TimezoneDBCreator:
    def __init__(self, processed_timezones={}, processed_timezones_obj=[]):
        self.processed_timezones = processed_timezones
        self.processed_timezones_obj = processed_timezones_obj

    def create_timezone_object(self, cells):
        timezone = Timezones(country_code=cells[0],
                             timezone_id=cells[1],
                             gmt=cells[3])
        self.processed_timezones[cells[1]] = timezone
        self.processed_timezones_obj.append(timezone)
        timezone.save()  # ???
        return timezone

    def add_timezones_objects_to_db(self):
        Timezones.objects.bulk_create(self.processed_timezones_obj)

    def get_timezone_object(self, timezone_name, file_path="geonames\\timezones.txt"):
        timezones_txt = open(file_path, 'r', encoding="utf8")
        for cells in timezones_txt.readlines():
            cells = cells.split('\t')
            if cells[1] == timezone_name:
                if cells[1] in self.processed_timezones:
                    return self.processed_timezones[cells[1]]
                return self.create_timezone_object(cells)
