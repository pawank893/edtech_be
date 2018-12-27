class UserNotAuthenticated(Exception):
    def __init__(self):
        message = "user is not authenticated"
        super(UserNotAuthenticated, self).__init__(message)


class TestSeriesEnd(Exception):
    def __init__(self):
        message = "test series ends"
        super(TestSeriesEnd, self).__init__(message)


class QuestionNotAnswered(Exception):
    def __init__(self):
        message = "question is not answered"
        super(QuestionNotAnswered, self).__init__(message)


class TestSeriesNotSelected(Exception):
    def __init__(self):
        message = "test series not selected"
        super(TestSeriesNotSelected, self).__init__(message)


class ValidTestSeriesNotSelected(Exception):
    def __init__(self):
        message = "valid test series not selected"
        super(ValidTestSeriesNotSelected, self).__init__(message)

