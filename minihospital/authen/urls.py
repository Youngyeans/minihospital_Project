from django.urls import path

from authen.views import LoginView, LogoutView

app_name = 'authen'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]