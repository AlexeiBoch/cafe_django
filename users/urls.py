from django.urls import path

from users.views import ProfileView, LoginExtendedView, RegisterView, logout_func
from users.views import ChangePasswordView, ChangePasswordDoneView
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginExtendedView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_func, name='logout'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password-change/done/', ChangePasswordDoneView.as_view(), name='password_change_done'),
]