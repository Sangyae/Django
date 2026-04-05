from django.urls import path

from . import views

urlpatterns =[
    path('home', views.HomeViews.as_view()),
    path('authorized', views.AuthorizedViews.as_view()),
]
    