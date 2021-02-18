from geonames.models import Timezones
from typing import List, Union, IO


class TimezoneDBCreator:
    def __init__(self, processed_timezones={}, processed_timezones_obj=[]):
        self.processed_timezones = processed_timezones
        self.processed_timezones_obj = processed_timezones_obj

    def create_timezone(self, cells):
        timezone = Timezones(country_code=cells[0],
                             timezone_id=cells[1],
                             gmt=cells[3])
        self.processed_timezones[cells[1]] = timezone
        self.processed_timezones_obj.append(timezone)
        timezone.save()
        return timezone

    def add_timezones_to_db(self):
        Timezones.objects.bulk_create(self.processed_timezones_obj)

    def find_timezone_in_file(self, timezone_name, file_path="geonames\\timezones.txt"):
        timezones_txt = open(file_path, 'r', encoding="utf8")
        for cells in timezones_txt.readlines():
            cells = cells.split('\t')
            if cells[1] == timezone_name:
                if cells[1] in self.processed_timezones:
                    return self.processed_timezones[cells[1]]
                return self.create_timezone(cells)

# def convert_timezones_txt_to_db(timezones_txt: IO) -> List[Timezones]:
#     timezones_db_lst = []
#     timezones_lst = get_timezones()
#     for cells in timezones_txt.readlines():
#         cells = cells.split('\t')
#         timezones_db_lst = append_timezone_to_db(timezones_lst, timezones_db_lst, cells)
#     print(timezones_db_lst)
#     Timezones.objects.bulk_create(timezones_db_lst)
#
#
# def append_timezone_to_db(timezones_list: List[str], timezones_db_list: List[Timezones],
#                           cells: List[Union[float, str]]) -> List[Timezones]:
#     if cells[1] in timezones_list:
#         timezones_db_list.append(Timezones(time_zone=cells[1], offset=cells[3]))
#     return timezones_db_list
#
#
# def get_timezones() -> List[str]:
#     timezones_list = []
#     for item in GeoNames.objects.all():
#         if item.timezone not in timezones_list:
#             timezones_list.append(item.timezone)
#     return timezones_list
