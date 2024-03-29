# pages/urls.py
from django.urls import path
from .views import homeview
from . import views
from pages import views
from django.views.generic.edit import FormView
from .views import OrderFormView, OrderCreateView
from django import forms

app_name = "pages"
urlpatterns = [
    path('', views.homeview, name='home'),
    path('supplier.html', views.supplier_view, name='supplier'),
    path('orderform', OrderCreateView.as_view(), name='orderform'),
    path('calendar.html', views.calendar_view, name='calendar'),
    path('blog.html', views.blog_view, name='blog'),
    path('social.html', views.social_view, name='social'),
    path('FAQ.html', views.FAQ_view, name='FAQ'),
    path('press.html', views.press_view, name='press'),
]
