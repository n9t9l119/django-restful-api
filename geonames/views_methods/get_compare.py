import re

from transliterate import translit
from typing import Union, Dict, Any, Tuple, List

from geonames.models import GeoNames, NameId, Timezones


def info_comparison(geo_1: str, geo_2: str):
    validation = input_validation(geo_1, geo_2)
    if validation:
        return make_compare_dict(geo_1, geo_2)
    return validation


def make_compare_dict(geo_1: str, geo_2: str) -> Dict[str, Any]:
    geo_1, geo_2 = get_obj_by_name(geo_1), get_obj_by_name(geo_2)
    lt = {'geo_1': geo_1, 'geo_2': geo_2,
          'compares': get_comparison(geo_1, geo_2)}
    return lt


def input_validation(geo_1: str, geo_2: str) -> Union[bool, str]:
    if re.match(r'[А-Яа-я0-9\s]*$', geo_1) \
            and re.match(r'[А-Яа-я0-9\s]*$', geo_2) is not None:
        return True
    return "Names can only contain cyrillic letters and numbers!"


def translit_request(geo_1: str, geo_2: str) -> Tuple[str, str]:
    geo_1 = translit(geo_1, reversed=True)
    geo_2 = translit(geo_2, reversed=True)
    return geo_1, geo_2


def get_obj_by_name(name: str) -> GeoNames:
    ids = find_all_ids(name)
    items = get_items_by_ids(ids)
    return chose_item(items)


def chose_item(items: List[GeoNames]) -> Union[GeoNames, None]:
    if items:
        chosen_item = items[0]
        for item in items:
            if item.population > chosen_item.population:
                chosen_item = item
        return chosen_item
    return None


def get_items_by_ids(ids: List[int]) -> List[GeoNames]:
    if ids:
        items = []
        for id in ids:
            item = GeoNames.objects.filter(id=id).first()
            if item is not None:
                items.append(item)
        return items
    return []


def find_all_ids(name: str) -> List[int]:
    ru_ids = get_ids_by_name(name)
    print(name)
    name = translit(name, 'ru', reversed=True)
    alt_ids = get_ids_by_name(name)
    for id in ru_ids:
        if id not in alt_ids:
            alt_ids.append(id)
    return alt_ids


def get_ids_by_name(name: str) -> List[int]:
    items = NameId.objects.filter(name=name)
    if items:
        ids = []
        for item in items:
            ids.append(item.geonameid.id)
        return ids
    return []


def get_comparison(geo_1: GeoNames, geo_2: GeoNames) -> Union[Dict[str, Any], None]:
    if geo_1 is not None and geo_2 is not None:
        northern_item = compare_geo(geo_1, geo_2)
        compare_dct = {'Northern geo': northern_item.name,
                       'Northern latitude': northern_item.latitude,
                       'Timezones_difference': compare_timezone(geo_1, geo_2)}
        return compare_dct
    return None


def compare_geo(geo_1: GeoNames, geo_2: GeoNames) -> GeoNames:
    if geo_1.latitude > geo_2.latitude:
        return geo_1
    return geo_2


def compare_timezone(geo_1: GeoNames, geo_2: GeoNames) -> float:
    if geo_1.timezone == geo_2.timezone:
        return 0.0
    return timezones_difference(geo_1.timezone, geo_1.timezone)


def timezones_difference(time_1: Timezones, time_2: Timezones) -> Union[str, float]:
    # time_1 = get_timezone(timezone_1)
    # time_2 = get_timezone(timezone_2)
    if time_1 == "Timezone is not defined!" or time_2 == "Timezone is not defined!":
        return "Undefinded"
    return time_1 - time_2


def get_timezone(timezone: str) -> Union[str, Timezones]:
    if timezone == "":
        return "Timezone is not defined!"
    else:
        return Timezones.objects.filter(time_zone=timezone).first().gmt
