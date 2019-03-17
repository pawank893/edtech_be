import logging

from rest_framework import serializers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response

from edtech.apis.api_error_response import APIErrorResponse
from edtech.apis.api_response import APIResponse
from edtech.apis.edtech_api import EdtechAPI
from edtech.exceptions import UserNotAuthenticated
from edtech.models import UserQuestionAnswer, Choice
from edtech.models.test_series import TestSeries

logger = logging.getLogger(__name__)


class ResultAPI(EdtechAPI):
    authentication_classes = (BasicAuthentication, SessionAuthentication)

    def get(self, request, format=None):
        try:
            if not request.user.is_authenticated():
                raise UserNotAuthenticated()

            test_series_id = request.session['test_series_id']

            test_series = TestSeries.objects.get(id=test_series_id)

            questions = test_series.questions.all().values_list('id', flat=True)

            answered_choices = UserQuestionAnswer.objects.filter(user=request.user,
                                                                 question__id__in=questions,
                                                                 session_end=False,
                                                                 ).order_by('-id')
            question_ans_mapping = dict()
            correct_choices = 0
            wrong_choices = 0

            for ac in answered_choices:
                if not question_ans_mapping.get(ac.question.id):
                    question_ans_mapping[ac.question.id] = ac.is_correct
                    if ac.is_correct:
                        correct_choices += 1
                    else:
                        wrong_choices += 1

            data = dict(
                total_question=len(questions),
                total_answered=len(question_ans_mapping.keys()),
                correct_choices=correct_choices,
                wrong_choices=wrong_choices
            )

            qs = UserQuestionAnswer.objects.filter(user=request.user)
            qs.update(session_end=True)

            # request.session['test_series_id'] = 0
            request.session['review_test_series_id'] = request.session['test_series_id']
            request.session['question_no'] = 1

            return Response(data)
        except UserNotAuthenticated:
            return APIErrorResponse.forbidden_action()

        # except Exception as e:
        #     logger.exception(e.message)
        #     return APIErrorResponse.internal_server_error()
