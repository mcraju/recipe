from django.conf.urls import url
from . import views

app_name = 'foody'
urlpatterns = [
    url(r'^$', views.menu, name='menu'),
    url(r'^make/$', views.make_over, name='make_over'),
    url(r'^save/$', views.save, name='save'),
    url(r'^(?P<f_id>[0-9]+)/$', views.display, name='display')
]

