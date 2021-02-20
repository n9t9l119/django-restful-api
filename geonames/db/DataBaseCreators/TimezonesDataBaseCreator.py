from geonames.models import Timezones


class TimezoneDBCreator:
    def __init__(self, timezones_txt, processed_timezones={}, processed_timezones_obj=[]):
        self.timezones_txt = timezones_txt
        self.processed_timezones = processed_timezones
        self.processed_timezones_obj = processed_timezones_obj

    def create_and_save_timezone_object(self, cells):
        timezone = Timezones(country_code=cells[0],
                             timezone_id=cells[1],
                             gmt=cells[3])
        self.processed_timezones[cells[1]] = timezone
        self.processed_timezones_obj.append(timezone)
        timezone.save()
        return timezone

    def add_timezones_objects_to_db(self):
        Timezones.objects.bulk_create(self.processed_timezones_obj)

    def find_timezone_in_file(self, timezone_name):
        self.timezones_txt.seek(0)
        for cells in self.timezones_txt.readlines():
            cells = cells.split('\t')
            if cells[1] == timezone_name:
                return self.create_and_save_timezone_object(cells)
        return None

    def get_timezone_object(self, timezone_name):
        if timezone_name in self.processed_timezones:
            return self.processed_timezones[timezone_name]
        return self.find_timezone_in_file(timezone_name)

