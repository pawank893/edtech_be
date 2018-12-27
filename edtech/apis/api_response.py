from rest_framework import status
from rest_framework.response import Response


class APIResponse(object):

    @classmethod
    def __prep_response(cls, message, response_code):
        response = {
            "message": message
        }

        response = Response(data=response, status=response_code)
        return response

    @classmethod
    def no_content(cls, ):
        return cls.__prep_response(message="no content",
                                   response_code=status.HTTP_204_NO_CONTENT)
