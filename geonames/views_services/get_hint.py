import re
from typing import List, Union
from rest_framework import status
from rest_framework.response import Response

from geonames.models import NameId


def hint(request: str) -> Union[List, Response]:
    """Getting hints for a received request."""
    validation = request_validation(request)
    if validation is True:
        return make_hint_list(request)
    return validation


def request_validation(request: str) -> Union[bool, Response]:
    """ Checking the data received from the server """
    if re.match(r'[\wА-Яа-я\d]', request) is None:
        Response("Invalid characters for hints!", status=status.HTTP_400_BAD_REQUEST)
    return True


# Нужен бинарный поиск
def make_hint_list(request: str) -> List[str]:
    """Getting a list of required prompts."""
    hint_list = []
    all_names = NameId.objects.order_by('name')
    for item in all_names:
        if re.match(request, item.name) is not None:
            if item.name not in hint_list:
                hint_list.append(item.name)
    return hint_list
