from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from users import views

urlpatterns = [
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('user/', views.Register.as_view({'post': 'create'})),
    path('refresh/', TokenRefreshView.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('profile/', views.Profile.as_view()),
    path('users/', views.Users.as_view()),
    path('user/<int:id>/', views.UserDetail.as_view()),
]