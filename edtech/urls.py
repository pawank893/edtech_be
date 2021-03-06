"""edtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from edtech.apis.login import LoginAPI
from edtech.apis.logout import LogoutAPI
from edtech.apis.question import QuestionAPI
from edtech.apis.result import ResultAPI
from edtech.apis.review import ReviewAPI
from edtech.apis.signup import SignupAPI
from edtech.apis.test import TestAPI
from edtech.apis.test_series import TestSeriesAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login/', LoginAPI.as_view()),
    url(r'^api/logout/', LogoutAPI.as_view()),
    url(r'^test/$', TestAPI.as_view()),
    url(r'^api/question/$', QuestionAPI.as_view()),
    url(r'^api/result/$', ResultAPI.as_view()),
    url(r'^api/test-series/$', TestSeriesAPI.as_view()),
    url(r'^api/review/$', ReviewAPI.as_view()),
    url(r'^api/signup/$', SignupAPI.as_view())
]
