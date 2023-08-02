from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:id>", views.recipients, name="recipients"),
    path("recipients/", views.recipientGroups, name="recipientGroups"),
    path('send/', views.send, name='send'),
]
