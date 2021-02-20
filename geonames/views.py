from rest_framework import generics, status
from rest_framework.response import Response

from geonames.serializers import *
from geonames.views_services.get_compare import info_comparison
from geonames.views_services.get_hint import hint
from geonames.views_services.get_page import page


class GeoNamesInfoView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        elem = GeoNames.objects.get(geonameid=int(request.data['geonameid']))
        return Response(self.get_serializer(elem).data)


class GeoNamesPageView(generics.ListAPIView):
    def post(self, request):
        items = page(request.data['page_number'], request.data['items_value'])
        serializer = GeoNamesSerializer(data=items, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class GeoNamesCompareView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        data = info_comparison(request.data['geo_1'], request.data['geo_2'])

        data['geo_1'] = self.get_serializer(data['geo_1']).data
        data['geo_2'] = self.get_serializer(data['geo_2']).data

        return Response(data)


class GeoNamesHintView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer()

    def post(self, request):
        result = {'hint': hint(request.data['hint'])}
        return Response(result)
