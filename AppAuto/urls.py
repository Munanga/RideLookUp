from django.conf.urls import url
from AppAuto import views

app_name = 'AppAuto'

urlpatterns = [
    url(r'^search/$', views.search, name='search'),
    url(r'^create/$', views.create, name='create'),
    url(r'^purchase/(?P<url_id>[0-9]+)/$', views.purchase, name='purchase'),
    url(r'^delete/(?P<url_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^api/$', views.vehicle_list, name='api'),
]
