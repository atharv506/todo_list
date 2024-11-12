
from . import views
from .views import tasklist
from django.urls import path


urlpatterns = [
    path('', tasklist.as_view(),name ='tasklist'),
]
