import urllib

from django.contrib.auth import authenticate, login
from rest_framework import serializers, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
import json

from edtech.apis.api_error_response import APIErrorResponse
from edtech.apis.edtech_api import EdtechAPI
from edtech.models.test_series import TestSeries


class _LoginRequestDTO(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class LoginAPI(EdtechAPI):
    authentication_classes = (BasicAuthentication,)

    def options(self, request, *args, **kwargs):
        return APIErrorResponse.method_not_allowed()

    def post(self, request):
        lr_dto = _LoginRequestDTO(data=request.data)

        if not lr_dto.is_valid():
            return Response(lr_dto.errors, status.HTTP_400_BAD_REQUEST)

        lr_data = lr_dto.data
        user = authenticate(username=lr_data['username'], password=lr_data['password'])
        if user and user.is_active:
            login(request, user)

            response = Response({
                'status': 'success',
                'msg': 'User logged in successfully',
                'userId': user.id,
                'email': user.email,
            })
            authenticated_user_cookie_map = {
                "userId": user.id,
                "email": user.email,
            }

            request.session['test_series_id'] = TestSeries.objects.order_by('?').first().id
            request.session['question_no'] = 1

            response.set_cookie('authenticated_user', urllib.quote(json.dumps(authenticated_user_cookie_map)))
            return response
        else:
            return APIErrorResponse.invalid_login_credentials(lr_data['username'])
