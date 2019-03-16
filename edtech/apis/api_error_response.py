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

    @classmethod
    def method_not_allowed(cls,):
        return cls.__prep_error_response(error_code=1201,
                                         message="method not supported",
                                         response_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    @classmethod
    def forbidden_action(cls, ):
        return cls.__prep_error_response(error_code=1202,
                                         message="method not supported",
                                         response_code=status.HTTP_403_FORBIDDEN)

    @classmethod
    def test_series_not_selected(cls, ):
        return cls.__prep_error_response(error_code=1202,
                                         message="test series not selected",
                                         response_code=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def valid_test_series_not_selected(cls, ):
        return cls.__prep_error_response(error_code=1202,
                                         message="valid test series not selected",
                                         response_code=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def internal_server_error(cls, msg=""):
        return cls.__prep_error_response(error_code=1203,
                                         message=msg,
                                         response_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
