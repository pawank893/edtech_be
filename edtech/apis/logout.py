from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout

from edtech.apis.edtech_api import EdtechAPI


class LogoutAPI(EdtechAPI):
    authentication_classes = (SessionAuthentication,)

    def get(self, request, format=None):
        raise MethodNotAllowed("GET")

    def post(self, request, format=None):
        try:
            logout(request)
            response = Response({"success": {
                'msg': "user logged out"
            }
            },
                status=status.HTTP_200_OK)
            response.set_cookie('authenticated_user', 'false')
            return response
        except Exception as e:
            return Response({
                "error": {
                    "msg": "Unable to logout user",
                    "code": "1001"
                }
            }, status=status.HTTP_400_BAD_REQUEST)
