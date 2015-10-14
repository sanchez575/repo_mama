from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
	url(r'^contacto/$', views.contacto, name='contacto'),
	url(r'^servicios/$', views.servicios, name='servicios'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]

