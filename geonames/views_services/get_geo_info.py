from rest_framework import status
from rest_framework.response import Response
from typing import Union

from geonames.models import GeoNames


def info(geonameid: int) -> Union[GeoNames, Response]:
    validation = geonameid_validation(geonameid)
    if validation is True:
        return get_item_by_geonameid(geonameid)
    return validation


def geonameid_validation(geonameid: int) -> Union[bool, Response]:
    if 451747 <= int(geonameid) <= 12123288:
        return True
    return Response("Wrong range!\nIt should be no less than 451747 and no more than 12123288",
                    status=status.HTTP_400_BAD_REQUEST)


def get_item_by_geonameid(geonameid: int) -> Union[GeoNames, Response]:
    item = GeoNames.objects.get(geonameid=geonameid)
    if item is None:
        return Response("Such id does not exist!", status=status.HTTP_404_NOT_FOUND)
    return item
