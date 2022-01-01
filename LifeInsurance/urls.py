from django.urls import path
from .views import LifeInsuranceView

app_name = "LifeInsurance"

urlpatterns = [
    path("create/", LifeInsuranceView.as_view(), name='create_insurance')
]