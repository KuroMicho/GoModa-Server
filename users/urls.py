from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from users import views

urlpatterns = [
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('register/', views.Register.as_view({'post': 'create'})),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('user/', views.Profile.as_view()),
    path('users/', views.Users.as_view()),
    path('users/<int:user_id>', views.UserDetail.as_view()),
]