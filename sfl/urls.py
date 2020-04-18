from django.urls import path
from .views import InvokeProvisioning

urlpatterns = [
    path('sfl/invoke/provisioning',InvokeProvisioning.as_view()),
]
