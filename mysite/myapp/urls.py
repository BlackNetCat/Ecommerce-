from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:my_id>/", views.indexItem, name="detail"),


]