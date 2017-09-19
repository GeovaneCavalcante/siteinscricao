from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^inscricao$', views.inscricao),
    url(r'^confirmacao$', views.confirmacao)
]
