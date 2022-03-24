from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index),
    path('name_wheel',views.name_wheel),
    path('number_wheel',views.number_wheel)

]
