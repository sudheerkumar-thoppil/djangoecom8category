
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.category,name="category"),
]