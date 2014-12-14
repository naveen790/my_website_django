from django.conf.urls import patterns, include, url
from website import views

urlpatterns = patterns('',
    url(r'^$',views.index),
    url(r'^contact/',views.contact),
    url(r'^resume/',views.resume),
    url(r'^courses/',views.courses),
)