from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('manage-users/', views.ManageUsersView.as_view(), name='manage_users'),
    path('admin-manage-users/', views.AdminManageUsersView.as_view(), name='admin_manage_users'),
]
