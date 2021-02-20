from rest_framework import generics, status
from rest_framework.response import Response

from geonames.serializers import *
from geonames.views_services.get_compare import info_comparison
from geonames.views_services.get_geo_info import info
from geonames.views_services.get_hint import hint
from geonames.views_services.get_page import page


class GeoNamesInfoView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        if 'geonameid' in request.data:
            server_response = info(request.data['geonameid'])
            if type(server_response) is Response:
                return server_response
            return Response(self.get_serializer(server_response).data)
        else:
            return Response("'geonameid' key not in request!", status=status.HTTP_400_BAD_REQUEST)


class GeoNamesPageView(generics.ListAPIView):
    def post(self, request):
        if 'page_number' in request.data and 'items_value' in request.data:
            server_response = page(request.data['page_number'], request.data['items_value'])
            if type(server_response) is Response:
                return server_response
            serializer = GeoNamesSerializer(data=server_response, many=True)
            serializer.is_valid()
            return Response(serializer.data)
        else:
            return Response("'page_number' or 'items_value' keys not in request!", status=status.HTTP_400_BAD_REQUEST)


class GeoNamesCompareView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer

    def post(self, request):
        if 'geo_1' in request.data and 'geo_2' in request.data:
            server_response = info_comparison(request.data['geo_1'], request.data['geo_2'])

            if type(server_response) is Response:
                return server_response

            server_response['geo_1'] = self.get_serializer(server_response['geo_1']).data
            server_response['geo_2'] = self.get_serializer(server_response['geo_2']).data

            return Response(server_response)
        else:
            return Response("'geo_1' or 'geo_2' keys not in request!", status=status.HTTP_400_BAD_REQUEST)


class GeoNamesHintView(generics.ListAPIView):
    serializer_class = GeoNamesSerializer()

    def post(self, request):
        if 'hint' in request.data:
            server_response = hint(request.data['hint'])
            if type(server_response) is Response:
                return server_response
            server_response = {'hint': server_response}
            return Response(server_response)
        else:
            return Response("'hint' key not in request!", status=status.HTTP_400_BAD_REQUEST)
