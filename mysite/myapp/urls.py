from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path("hello/<int:my_id>/", views.indexItem, name="detail"),
    path('contacts/', views.contacts, name='contacts')

]