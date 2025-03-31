from django.urls import path
from mainpage import views

urlpatterns = [
    path('mainpage/', views.UserList.as_view()),
]
