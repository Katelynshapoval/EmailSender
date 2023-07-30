from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.list, name="list"),
    path("recipients/", views.index, name="index"),
    path('', views.home, name='home'),
    path('send/', views.send, name='send'),
]
