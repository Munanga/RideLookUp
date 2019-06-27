"""ProjectAuto URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from AppAuto import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.Index.as_view(),name='index'),
    url(r'^search/$',views.search, name='search'),
    url(r'^create/$',views.create, name='create'),
    url(r'^email-sent/$',views.email_sent, name='email_sent'),
    url(r'^purchase/(?P<url_id>[0-9]+)/$',views.purchase,name='purchase'),
    url(r'^delete/(?P<url_id>[0-9]+)/$',views.delete,name='delete'),
    url(r'^about/$',views.about.as_view(),name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^bob/$',views.bob.as_view(),name='bob'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [ url(r'^__debug__/', include(debug_toolbar.urls)),] + urlpatterns