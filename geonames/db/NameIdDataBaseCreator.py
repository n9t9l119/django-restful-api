from geonames.models import NameId, GeoNames


class NameIdDataBaseCreator:
    def __init__(self, processed_nameid=[]):
        self.processed_nameid = processed_nameid

    def create_nameid(self, name, item):
        nameid = NameId(name=name,
                        geonameid=item)

        self.processed_nameid.append(nameid)
        return nameid

    def convert_alternames_to_nameid(self, names, item):
        for name in names:
            self.create_nameid(name, item)

    def get_all_names(self, name, asciiname, alternatenames):
        names = [name]
        if names[0] != asciiname:
            names.append(asciiname)
        if alternatenames != "":
            alternatenames = alternatenames.split(',')
            for alternatename in alternatenames:
                if alternatename not in names and alternatename != '':
                    names.append(alternatename)
        return names

    def create_nameid_from_geonames(self):
        geonames_items = GeoNames.objects.all()
        for item in geonames_items:
            all_names = self.get_all_names(item.name, item.asciiname, item.alternatenames)
            for name in all_names:
                self.create_nameid(name, item)

    def add_nameid_to_db(self):
        NameId.objects.bulk_create(self.processed_nameid)
