from django.conf.urls import url
from .views import SiteListView, SiteDetailView, SiteCreateView
from .import views

urlpatterns=[
    url('^$', SiteListView.as_view(), name='welcome'),
    url('^site/<int:pk>/', SiteDetailView.as_view(), name='site-detail'),
    url('^site/new/', SiteCreateView.as_view(), name='site-create'),
    ]
