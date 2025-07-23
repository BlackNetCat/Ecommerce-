from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("hello/<int:my_id>/", views.indexItem, name="indexItem"),
    path('contacts/', views.contacts, name='contacts')

]