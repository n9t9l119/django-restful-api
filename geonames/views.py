import json

from rest_framework import generics
from rest_framework.response import Response

from geonames.models import GeoNames
from geonames.serializers import *
from geonames.views_methods.get_compare import info_comparison
from geonames.views_methods.get_hint import hint


class GeoNamesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GeoNamesSerializer
    queryset = GeoNames.objects.all()


class GeoNamesInfoView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        elem = GeoNames.objects.get(geonameid=int(request.data['geonameid']))
        return Response(self.get_serializer(elem).data)


class GeoNamesPageView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        start_id = int(request.data['page_number']) * int(request.data['items_value']) + 1
        items = []
        for value in range(int(request.data['items_value'])):
            items.append(self.get_serializer(GeoNames.objects.get(pk=(start_id + value))).data)
        return Response(items)


class GeoNamesCompareView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        return Response(json.dumps(info_comparison(request.data['geo_1'], request.data['geo_2'])['compares']))


class GeoNamesHintView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        return Response(json.dumps(hint(request.data['hint'])))
