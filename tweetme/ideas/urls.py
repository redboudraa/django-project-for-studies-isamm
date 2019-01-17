



from django.conf.urls import url, include
from django.urls import path

from .views import TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # url(r'^$', tweet_list_view, name='list'),
    #url(r'^1/$', tweet_detail_view, name='detail'),
    # url(r'^1/$', TweetDetailView.as_view(), name='detail2'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^create$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
    
 ]