from geonames.models import NameId, GeoNames


class NameIdDataBaseCreator:
    def __init__(self, processed_nameid=[]):
        self.processed_nameid = processed_nameid

    def create_nameid_object(self, name, item):
        nameid = NameId(name=name,
                        geonameid=item)

        self.processed_nameid.append(nameid)
        return nameid

    def convert_alternames_to_nameid_objects(self, names, item):
        for name in names:
            self.create_nameid_object(name, item)

    def convert_alternatename_cell_to_list(self, names, alternatenames):
        alternatenames = alternatenames.split(',')
        for alternatename in alternatenames:
            if alternatename not in names:
                names.append(alternatename)
        return names

    def get_all_names_of_geoname_object(self, name, asciiname, alternatenames):
        names = [name]
        names[0] != asciiname and names.append(asciiname)
        if alternatenames != "":
            names = self.convert_alternatename_cell_to_list(names, alternatenames)
        return names

    def create_nameid_objects_from_geonames(self):
        geonames_items = GeoNames.objects.all()
        for item in geonames_items:
            all_names = self.get_all_names_of_geoname_object(item.name, item.asciiname, item.alternatenames)
            for name in all_names:
                self.create_nameid_object(name, item)

    def add_nameid_objects_to_db(self):
        NameId.objects.bulk_create(self.processed_nameid)
