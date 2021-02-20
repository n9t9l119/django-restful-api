import re
from typing import Union, List, Dict, Any
from geonames.models import GeoNames


def page(page_number: int, items_value: int):
    validation = input_validation(page_number, items_value)
    if validation is True:
        start_id = items_value * page_number + 1
        return make_items_lst(items_value, start_id)
    return validation


def input_validation(page_number: int, items_value: int):
    if re.match(r'[0-9]{1,6}$', str(page_number)) \
            and re.match(r'[0-9]{1,6}$', str(items_value)) is not None:
        return numerical_range_validation(page_number, items_value)
    return "'Page' and 'Items_value' must be a positiv number no less than 1 and no more than 6 digits!"


def numerical_range_validation(page_number: int, items_value: int):
    max_value = len(GeoNames.objects.all())
    if items_value > max_value:
        return "There is not so many values in database!"
    if (page_number + 1) * items_value > max_value or items_value == 0:
        return "That page is empty!"
    return True


def make_items_lst(items_value: int, start_id: int) -> List[Dict[str, Any]]:
    items = []
    print(start_id)
    print(GeoNames.objects.get(pk=1))
    for value in range(items_value):
        items.append(GeoNames.objects.get(pk=(start_id + value)))
    return items
