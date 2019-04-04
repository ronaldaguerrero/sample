### app url ##
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orders/show$', views.order),
    url(r'^products$', views.products),
    url(r'^orders$', views.orders),
    url(r'^cart$', views.cart),
    url(r'^shaq$', views.shaq),
    url(r'^carter$', views.index),
    url(r'^mourning$', views.zo),
    url(r'^$', views.index), # similar to @app.route('/') in flask
]