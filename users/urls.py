from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView, ChangePasswordView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/', BlacklistTokenUpdateView.as_view(), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    ]
