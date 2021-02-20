import re
from typing import List

from geonames.models import NameId


def hint(request: str):
    if request_validation(request):
        return make_hint_list(request)


def request_validation(request: str) -> bool:
    if re.match(r'[\wА-Яа-я\d]', request) is None:
        print(400)
    return True


def make_hint_list(request: str) -> List[str]:
    print(request)
    hint_list = []
    all_names = NameId.objects.order_by('name')
    for item in all_names:
        if re.match(request, item.name) is not None:
            if item.name not in hint_list:
                hint_list.append(item.name)
    return hint_list
