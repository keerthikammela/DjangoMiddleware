from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (UserListView, UserCreateView, UserUpdateView,
                UserDeleteView, UserDetailView, RegisterView, LogoutConfirmView,
                LogoutSubmitView, LogListView)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path("", LoginView.as_view(template_name="myapp/registration/login.html"), name="login"),
    path("logout/", LogoutConfirmView.as_view(), name="logout_confirm"),
    path("logout/submit/", LogoutSubmitView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path('logs/', LogListView.as_view(), name='view_logs'),
]