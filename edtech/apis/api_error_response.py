from rest_framework import status
from rest_framework.response import Response


class APIErrorResponse(object):

    @classmethod
    def __prep_error_response(cls, error_code, message, response_code):
        error_response = {
            "errors": [{
                "code": error_code,
                "message": message
            }]
        }

        response = Response(data=error_response, status=response_code)
        return response

    @classmethod
    def invalid_login_credentials(cls, user):
        return cls.__prep_error_response(error_code=1200,
                                         message="Invalid credentials for user {user}".format(user=user),
                                         response_code=status.HTTP_401_UNAUTHORIZED)
