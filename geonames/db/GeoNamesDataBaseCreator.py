from geonames.models import GeoNames, Timezones


class GeoNamesDataBaseCreator:
    def __init__(self, timezone_creator, processed_geonames=[]):
        self.timezone_creator = timezone_creator
        self.processed_geonames = processed_geonames

    def create_geoname_object(self, cells):
        geoname = GeoNames(
            geonameid=cells[0],
            name=cells[1],
            asciiname=cells[2],
            alternatenames=cells[3],
            latitude=cells[4],
            longitude=cells[5],
            feature_class=cells[6],
            feature_code=cells[7],
            country_code=cells[8],
            cc2=cells[9],
            admin1_code=cells[10],
            admin2_code=cells[11],
            admin3_code=cells[12],
            admin4_code=cells[13],
            population=cells[14],
            elevation=cells[15] if cells[15] != '' else None,
            dem=cells[16],
            timezone=self.timezone_creator.get_timezone_object(cells[17]),
            modification_date=cells[18])
        self.processed_geonames.append(geoname)
        return geoname

    def make_list_from_string(self, string):
        cells = string.split('\t')
        cells[-1] = cells[-1].replace("\n", "")
        return cells

    def convert_txt_file_to_geonames_objects(self):
        geonames_txt = open("geonames\RU.txt", 'r', encoding="utf8")
        for string in geonames_txt.readlines():
            cells = self.make_list_from_string(string)
            self.create_geoname_object(cells)

    def add_geonames_objects_to_db(self):
        GeoNames.objects.bulk_create(self.processed_geonames)
