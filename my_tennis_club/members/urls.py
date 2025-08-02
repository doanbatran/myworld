from django.urls import path
from . import views

urlpatterns = [
    # path('', views.404, name='404'),
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]