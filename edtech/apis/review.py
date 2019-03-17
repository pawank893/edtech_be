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


class _QuestionRequestDTO(serializers.Serializer):
    action = serializers.CharField(max_length=50, allow_null=True, required=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ReviewAPI(EdtechAPI):
    authentication_classes = (BasicAuthentication, SessionAuthentication)

    def post(self, request, format=None):
        try:
            if not request.user.is_authenticated():
                raise UserNotAuthenticated()

            test_series_id = request.session.get('review_test_series_id')
            if test_series_id is None:
                return APIResponse.no_last_test_done()
            question_no = request.session['question_no']

            test_series = TestSeries.objects.get(id=test_series_id)
            questions = test_series.questions.all()

            if request.data.get('action') == "next":
                question_no += 1
            elif request.data.get('action') == "prev":
                question_no -= 1

            request.session['question_no'] = question_no

            try:
                selected_q = questions[question_no - 1]
            except Exception as e:
                logger.info("No question available. Error {error}".format(error=e.message))
                return APIResponse.no_content()

            options = selected_q.options.all().values('id', 'choice', 'type', 'is_choice_correct')

            options_list = []

            try:
                answered_choice = UserQuestionAnswer.objects.filter(user=request.user,
                                                                    question=selected_q,
                                                                    session_end=True,
                                                                    ).latest('id')
            except:
                answered_choice = None

            for option in options:
                tmp = {
                    'id': option['id'],
                    'choice': option['choice'],
                    'answered': False,
                    'type': option['type'],
                    'is_choice_correct': option['is_choice_correct']
                }
                if answered_choice and option['id'] == answered_choice.choice.id:
                    tmp['answered'] = True
                options_list.append(tmp)

            data = {
                "question_no": question_no,
                "topic": selected_q.topic.name,
                "question": selected_q.description,
                "options": options_list,

                "image": selected_q.diagram
            }
            return Response(data)
        except UserNotAuthenticated:
            return APIErrorResponse.forbidden_action()

        except Exception as e:
            logger.exception(e.message)
            return APIErrorResponse.internal_server_error(e.message)
