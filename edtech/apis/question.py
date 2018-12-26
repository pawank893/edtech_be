from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response

from edtech.apis.api_error_response import APIErrorResponse
from edtech.apis.edtech_api import EdtechAPI
from edtech.models.test_series import TestSeries


class QuestionAPI(EdtechAPI):
    authentication_classes = (BasicAuthentication, SessionAuthentication)

    def post(self, request, format=None):
        if not request.user.is_authenticated():
            return APIErrorResponse.forbidden_action()
        test_series_id = request.session['test_series_id']
        question_no = request.session['question_no']

        test_series = TestSeries.objects.get(id=test_series_id)

        questions = test_series.questions.all()


        if request.data.get('action') == "next":
            request.session['question_no'] = question_no + 1
            question_no += 1
        elif request.data.get('action') == "prev":
            request.session['question_no'] = question_no - 1
            question_no -= 1

        try:
            selected_q = questions[question_no - 1]
        except Exception as e:
            return APIErrorResponse.forbidden_action()

        data = {
            "question_no": question_no,
            "topic": selected_q.topic.name,
            "question": selected_q.description,
            "options": list((selected_q.options.all().values_list('choice', flat=True))),
            "image": selected_q.diagram
        }
        return Response(data)
