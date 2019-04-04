### second app url ##
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # similar to @app.route('/') in flask
    url(r'^add/(?P<my_val>\d+)$', views.add),
    url(r'^cart$', views.cart),
    url(r'^shop$', views.shop),
    url(r'^single_product$', views.single_product),
    url(r'^contact$', views.contact),
    url(r'^blog$', views.blog),
    url(r'^login$', views.login),
	url(r'^userreg$', views.register_user),
	url(r'^userlog$', views.login_user),
	url(r'^address$', views.address),
	url(r'^success$', views.success),
	url(r'^clear$', views.clear),

]