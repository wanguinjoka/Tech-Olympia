from django.conf.urls import url
from .views import SiteListView, SiteDetailView, SiteCreateView
from .import views

urlpatterns=[
    url(r'^$', SiteListView.as_view(), name='welcome'),
    url(r'^site/(?P<pk>[0-9]+)/$', SiteDetailView.as_view(), name='site-detail'),
    url(r'^site/new/', SiteCreateView.as_view(), name='site-create'),
    ]
