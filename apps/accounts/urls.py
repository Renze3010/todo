from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import CustomLoginForm
from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html', authentication_form = CustomLoginForm), name = 'login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
