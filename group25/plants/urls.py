from django.conf.urls import include,url
from . import views
urlpatterns = [
	url(r'^$', views.check ,name = "check"),
    url(r'^index/$', views.index ,name = "index") ,#here linking the urls for displaying in the webpages.
    url(r'^get/$', views.getdata ,name ="getdata"),
    url(r'^index/addplant/$', views.addplant ,name = "addplant"),
    #url(r'^check/$', views.check ,name ="check"),
]