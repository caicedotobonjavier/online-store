from django.urls import path, re_path, include
#
from . import views

app_name = 'users_app'


urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('activate/<pk>/', views.ActivateUserView.as_view(), name='activate'),
    path('login/', views.LoginView.as_view(), name='login'),  
    path('verify-user/<pk>/', views.VerifyLoginView.as_view(), name='verify'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update-info-user/<pk>/', views.UpdateInfoUser.as_view(), name='update_info'),      
]