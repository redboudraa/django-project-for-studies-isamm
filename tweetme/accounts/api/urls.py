from django.conf.urls import url

from django.views.generic.base import RedirectView

from ideas.api.views import (
    TweetListAPIView,
    )

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
]