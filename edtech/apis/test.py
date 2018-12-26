from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response

from edtech.apis.edtech_api import EdtechAPI


class TestAPI(EdtechAPI):
    # authentication_classes = (BasicAuthentication, )

    def post(self, request, format=None):
        return Response({"status": "true"})
