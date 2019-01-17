"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from hashtags.views import HashTagView
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import UserRegisterView
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('tweet/', include('ideas.urls')),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^tweet/',  include(('ideas.urls', 'tweet'), namespace='tweet')),
    url(r'^api/tweet/', include(('ideas.api.urls', 'tweet-api'), namespace='tweet-api')),
    url(r'^register/$', UserRegisterView.as_view(), name='register'),
    url(r'^', include(('accounts.urls', 'profiles'), namespace='profiles')),
    url(r'^api/', include(('accounts.api.urls', 'profiles-api'), namespace='profiles-api')),
    url(r'^auth/', include('django.contrib.auth.urls')),
     #/
 ]


if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))