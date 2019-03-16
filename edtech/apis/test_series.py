import logging

from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response

from edtech.apis.api_error_response import APIErrorResponse
from edtech.apis.api_response import APIResponse
from edtech.apis.edtech_api import EdtechAPI
from edtech.exceptions import UserNotAuthenticated, TestSeriesNotSelected, ValidTestSeriesNotSelected
from edtech.models import UserQuestionAnswer, Choice
from edtech.models.test_series import TestSeries

logger = logging.getLogger(__name__)


class TestSeriesAPI(EdtechAPI):
    authentication_classes = (BasicAuthentication, SessionAuthentication)

    def get(self, request, format=None):
        try:
            if not request.user.is_authenticated():
                raise UserNotAuthenticated()

            test_series = TestSeries.objects.all()

            test_series_list = []
            for ts in test_series:
                test_series_list.append(dict(
                    id=ts.id,
                    name=ts.name
                ))

            data = dict(
                test_series=test_series_list
            )
            return Response(data)
        except UserNotAuthenticated:
            return APIErrorResponse.forbidden_action()


    def post(self, request, format=None):
        try:
            if not request.user.is_authenticated():
                raise UserNotAuthenticated()

            ts_id = request.data.get('ts_id')

            if ts_id is None:
                raise TestSeriesNotSelected()

            try:
                ts = TestSeries.objects.get(id=int(ts_id))
                request.session['test_series_id'] = ts.id
                request.session['question_no'] = 1
                return Response({'success': True})
            except TestSeries.DoesNotExist:
                raise ValidTestSeriesNotSelected()

        except ValidTestSeriesNotSelected:
            return APIErrorResponse.valid_test_series_not_selected()
        except TestSeriesNotSelected:
            return APIErrorResponse.test_series_not_selected()
        except UserNotAuthenticated:
            return APIErrorResponse.forbidden_action()
        except Exception as e:
            return APIErrorResponse.internal_server_error(e.message)
