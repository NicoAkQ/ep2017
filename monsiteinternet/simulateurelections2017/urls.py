# coding: utf-8
from django.conf.urls import url,include
from django.contrib import admin
from . import views 

urlpatterns = [
	url(r'^$',views.accueil,name="accueil"),
	url(r'^resultats/$',views.resultats,name="resultats"),
	url(r'^google5b0aef4ac639f252.html',views.google,name="google"),
]
