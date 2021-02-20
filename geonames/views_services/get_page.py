import re
from typing import Union, List
from rest_framework import status
from rest_framework.response import Response

from geonames.models import GeoNames


def page(page_number: int, items_value: int) -> Union[Response, List]:
    """Getting data for a given page."""
    validation = input_validation(page_number, items_value)
    if validation is True:
        start_id = items_value * page_number + 1
        return make_items_lst(items_value, start_id)
    return validation


def input_validation(page_number: int, items_value: int) -> Union[bool, Response]:
    """ Checking the data received from the server."""
    if re.match(r'[0-9]{1,6}$', str(page_number)) \
            and re.match(r'[0-9]{1,6}$', str(items_value)) is not None:
        return numerical_range_validation(page_number, items_value)
    return Response("'Page' and 'Items_value' must be a positiv number no less than 1 and no more than 6 digits!",
                    status=status.HTTP_400_BAD_REQUEST)


def numerical_range_validation(page_number: int, items_value: int) -> Union[bool, Response]:
    """Checking if a page exists at given values."""
    max_value = len(GeoNames.objects.all())
    if items_value > max_value:
        return Response("There is not so many values in database!", status=status.HTTP_400_BAD_REQUEST)
    if (page_number + 1) * items_value > max_value or items_value == 0:
        return Response("That page is empty!", status=status.HTTP_404_NOT_FOUND)
    return True


def make_items_lst(items_value: int, start_id: int) -> List[GeoNames]:
    """Getting a list of objects located on a given page."""
    items = []
    for value in range(items_value):
        items.append(GeoNames.objects.get(pk=(start_id + value)))
    return items
